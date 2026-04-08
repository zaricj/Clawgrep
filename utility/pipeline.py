import csv
import re
from pathlib import Path
from typing import Iterator

from utility.core import (
    load_patterns_json,
    compile_regex_patterns,
    get_files_in_folder,
    validate_input,
    create_directory,
)

from utility.parser import (
    yield_event_block,
    extract_matches_from_event_block,
    is_keyword_event,
    extract_log_date,
    yield_event_block_with_progress
)


# ========== Config ==========

def load_config(patterns_config: Path, pattern_key: str) -> re.Pattern | str:
    if not validate_input(patterns_config):
        raise FileNotFoundError(patterns_config)

    patterns_json = load_patterns_json(patterns_config)

    if pattern_key not in patterns_json:
        raise ValueError(f"Invalid key: {pattern_key}")

    compiled = compile_regex_patterns(patterns_json[pattern_key])
    header_regex = compiled["base"]["header"]

    return compiled, header_regex


# ========== Rows and headers Generator ==========

def collect_rows_and_headers(
    files: list,
    header_regex,
    compiled,
    keyword: str,
    show_progress: bool
):
    headers = []
    rows = []

    for file in files:
        log_date = extract_log_date(file)
        print(f"Processing: {file}")

        # Choose generator once
        block_iter = (
            yield_event_block_with_progress(file, header_regex)
            if show_progress
            else yield_event_block(file, header_regex)
        )

        for block in block_iter:
            if keyword and not is_keyword_event(keyword, block):
                continue

            row = extract_matches_from_event_block(block, compiled)
            if not row:
                continue

            # timestamp handling
            if "time" in row:
                row["timestamp"] = f"{log_date} {row['time']}".strip()
                del row["time"]
            else:
                row["timestamp"] = log_date

            # filter empty rows (ignore timestamp)
            if not any(
                v not in (None, "")
                for k, v in row.items()
                if k != "timestamp"
            ):
                continue

            # collect headers (ordered, no duplicates)
            for key in row:
                if key not in headers:
                    headers.append(key)

            rows.append(row)

    return rows, headers


# ========== CSV ==========

def write_csv(output: Path, headers: list[str], rows: Iterator[dict]) -> int:
    """Writes rows to a CSV file with the specified headers.

    Args:
        output (Path): The path to the output CSV file.
        headers (list[str]): A list of column headers for the CSV.
        rows (Iterator[dict]): An iterator over dictionaries representing each row.

    Returns:
        int: The number of rows written to the CSV file.
    """
    count = 0

    exists = validate_input(output)
    if not exists:
        create_directory(output)

    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=headers,
            delimiter=";",
            quotechar='"',
            quoting=csv.QUOTE_ALL
        )

        writer.writeheader()

        for row in rows:
            normalized = {k: row.get(k, "") for k in headers}
            writer.writerow(normalized)
            count += 1

    return count


# ========== Pipeline ==========

def run_pipeline(
        patterns_config: Path,
        pattern_key: str,
        files_directory: Path,
        file_pattern: str,
        output_csv: Path,
        event_keyword: str = "",
        show_progress: bool = False):

    compiled, header_regex = load_config(patterns_config, pattern_key)

    files = get_files_in_folder(files_directory, file_pattern)

    if not files:
        raise ValueError("No log files found")

    # Collect rows + headers in one pass
    rows, headers = collect_rows_and_headers(
        files, header_regex, compiled, event_keyword, show_progress
    )

    # Normalize headers
    headers = ["timestamp"] + \
        [h for h in headers if h not in ("time", "timestamp")]

    # Write CSV
    count = write_csv(output_csv, headers, rows)

    print(f"\nDone. {count} rows written to {output_csv}")
