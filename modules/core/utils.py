import json
import re
from pathlib import Path
from typing import Any
from rich import print as rprint

from modules.core.parser import (
    yield_event_block,
    extract_matches_from_event_block,
    is_keyword_event,
    yield_event_block_with_progress
)
from modules.core.thread_executor import run_with_threading
from modules.core.timestamp import build_timestamp
from modules.io.file_utils import get_file_info

# ========== Load & Compile Patterns ==========

def load_patterns_json(filepath: Path) -> dict[str, str]:
    with filepath.open("r", encoding="utf-8") as f:
        return json.load(f)


def get_pattern_keys(filepath: Path) -> list[str]:
    patterns = load_patterns_json(filepath)
    return list(patterns.keys())


def compile_regex(pattern: str, flags=0):
    return re.compile(pattern, flags)


def compile_regex_patterns(category_config: dict):
    """Compile base separator + patterns for one category"""
    compiled = {}
    compiled["base"] = {name: re.compile(
        p) for name, p in category_config.get("base", {}).items()}
    compiled["patterns"] = {name: re.compile(p, re.MULTILINE | re.DOTALL)
                            for name, p in category_config.get("patterns", {}).items()}
    return compiled

# ========== Rows and headers Generator ==========

def collect_rows_and_headers(
    files: list,
    separator_regex,
    compiled,
    keyword: str,
    show_progress: bool
):
    headers = []
    rows = []
    
    files_info: list[dict[str, Any]] = run_with_threading(get_file_info, files)

    for file in files_info:
        date_created: str = file["Created"].split("-")[0].strip()
        filepath: Path = file["Filepath"]
        total_lines: int = file["Lines"]
        
        # Work
        rprint(f"Processing: [blue][bold]{filepath.name}[/blue]")
        
        # Choose generator once
        block_iter = (
            yield_event_block_with_progress(filepath, separator_regex, total_lines)
            if show_progress
            else yield_event_block(filepath, separator_regex)
        )
        
        for block in block_iter:
            if keyword and not is_keyword_event(keyword, block):
                continue

            row = extract_matches_from_event_block(block, compiled)
            
            if not row:
                continue

            # Timestamp header handling
            if "time" in row:
                row["timestamp"] = build_timestamp(row["time"], filepath, date_created)
                del row["time"]
            else:
                row["timestamp"] = date_created

            # Filter empty rows (ignore timestamp)
            if not is_empty_row(row, "timestamp"):
                continue
            
            # collect headers (ordered, no duplicates)
            for key in row:
                if key not in headers:
                    headers.append(key)

            rows.append(row)

    return rows, headers


def is_empty_row(row: dict, ignore_key: str) -> bool:
    # Filter empty rows (ignore timestamp)
    return any(
        v not in (None, "")
        for k, v in row.items()
        if k != ignore_key)
