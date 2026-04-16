from pathlib import Path
from modules.core.pipeline import run_pipeline

if __name__ == "__main__":

    PATTERNS_CONFIG = Path("patterns/patterns.json")
    PATTERN_KEY = "sql_exceptions"
    FILE_PATTERN = "*.out"
    FILES_DIR = Path(r"C:\Users\ZaricJ\Downloads\Druckserver Auswertung\NESAS015")

    # CSV output
    OUTPUT_DIR = Path("output")
    CSV_FILE = OUTPUT_DIR / "Result.csv"

    # Test run config
    SAMPLE_FILE = Path("sample.log")
    
    # TODO Every single pattern key in patterns.json must contain a regex with multiple groups that will be used to search in an event block in log file.
    # TODO This makes sure that a single line contains all the matches from the same even block

    run_pipeline(
        patterns_config=PATTERNS_CONFIG,
        pattern_key=PATTERN_KEY,
        files_directory=FILES_DIR,
        file_pattern=FILE_PATTERN,
        output_csv=CSV_FILE,
        event_keyword="",
        show_progress=True
    )
