# Glint ✨

A file analysis and pattern extraction tool designed to search through any type of text files, ideally something like log files with repeating patterns and extract specific information using regex patterns.

## Core Functionality

- **Pattern-based Log Parsing**: Uses regex patterns to search through log files and extract specific information
- **Event Block Extraction**: Identifies complete event blocks from log files based on separator patterns
- **Multi-pattern Matching**: Can match multiple patterns within a single event block
- **CSV/Excel Export**: Outputs extracted data to CSV and Excel formats

## Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                    Glint ✨                                      │
├──────────────────────────────────────────────────────────────────┤
│  main.py                  │ Entry point, orchestrates pipeline   │
│                           │                                      │
│  modules/                 │                                      │
│  ├─ core/                 │                                      │
│  │  ├─ parser.py          │ Event block extraction & matching    │
│  │  ├─ pipeline.py        │ Main pipeline orchestration          │
│  │  ├─ thread_executor.py │ Threading utilities                  │
│  │  ├─ timestamp.py       │ Timestamp formatting                 │
│  │  ├─ ui.py              │ Holds rich module                    │
│  │  └─ utils.py           │                                      │
│  │                        │                                      │
│  ├─ io/                   │                                      │
│  │  ├─ converters.py      │ Path/epoch conversions               │
│  │  ├─ exporters.py       │ CSV & Excel output                   │
│  │  ├─ config.py          │ Pattern config loading & validation  │
│  │  └─ file_utils.py      │ File operations & validation         │
│                           │                                      │
├──────────────────────────────────────────────────────────────────┤
│  patterns/patterns.json   │ Regex patterns for different log     │
│  output/                  │   formats (SQL, DB pool, FTP, etc)   │
└──────────────────────────────────────────────────────────────────┘
```

### Design Philosophy

The application follows a **modular, pipeline-based architecture** with clear separation of concerns:

1. **Configuration Layer** (`modules/config/`)
   - Centralized configuration management
   - Environment-agnostic settings

2. **Core Processing Layer** (`modules/core/`)
   - Parsing logic
   - Pipeline orchestration
   - Thread management
   - UI components
   - Utility functions

3. **I/O Layer** (`modules/io/`)
   - File conversion utilities
   - Export functionality
   - File system operations

### Pipeline Concept

The `pipeline.py` module suggests a **processing pipeline** architecture where:
- Data flows through multiple stages
- Each stage can transform or filter data
- Results can be aggregated or exported
- Processing can be parallelized via `thread_executor.py`

### Parser System

The `parser.py` module indicates a **pattern-based parsing system** that:
- Loads pattern definitions from `patterns.json`
- Parses input data according to configured patterns
- Can handle multiple pattern types
- Likely uses regex or custom parsing logic

## Key Features

- **Threaded Processing**: Uses `ThreadPoolExecutor` for parallel file processing
- **Progress Tracking**: Optional progress bar with `tqdm`
- **Flexible Pattern Configuration**: JSON-based pattern definitions
- **Multiple Log Formats**: Supports various log formats:
  - SQL exceptions
  - Database pool size exceeded
  - FTP per profile logs
  - HTTP requests (Jasperserver)
  - Catalina output (Jasperserver)

## Usage

```python
run_pipeline(
    patterns_config=PATTERNS_CONFIG,  # patterns/patterns.json
    pattern_key=PATTERN_KEY,          # e.g., "sql_exceptions"
    files_directory=FILES_DIR,        # logs/
    file_pattern=FILE_PATTERN,        # *.log
    output_csv=CSV_FILE,              # output/Result_*.csv
    event_keyword="",                 # Optional filter
    show_progress=True
)
```

## Dependencies

- `tqdm` - Progress bars
- `xlsxwriter` - Excel export

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate it:
   ```bash
   # Windows
   .venv\Scripts\Activate.ps1
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # or install directly from pyproject.toml
   pip install -e .
   ```

## Project Structure

```
├── .git/                    # Version control
├── .gitignore               # Git ignore rules
├── .python-version          # Python version specification
├── .vscode/                 # VS Code configuration
├── logs/                    # Application logs
├── main-cli.py             # CLI entry point
├── main.py                 # Main application entry
├── gui/                    # GUI application folder
│   ├── main.py             # GUI main entry
│   └── modules.py          # GUI modules
├── modules/                # Core application modules
│   ├── __init__.py        # Module initialization
│   ├── config/            # Configuration management
│   │   └── config.py      # Configuration handler
│   ├── core/              # Core processing
│   │   ├── parser.py      # Parser logic
│   │   ├── pipeline.py    # Processing pipeline
│   │   ├── thread_executor.py  # Thread management
│   │   ├── timestamp.py   # Timestamp utilities
│   │   ├── ui.py          # UI components
│   │   └── utils.py       # Utility functions
│   └── io/                # I/O handling
│       ├── converters.py  # Format converters
│       ├── exporters.py   # Export functionality
│       └── file_utils.py  # File utilities
├── patterns/
│   └── patterns.json       # Pattern definitions
├── pyproject.toml          # Project configuration
├── uv.lock                 # Dependency lock file
└── README.md               # Documentation
```

## Configuration

### patterns/patterns.json

Define regex patterns for different log categories:

```json
{
  "sql_exceptions": {
    "base": {
      "separator": "^(?P<time>\\d{2}:\\d{2}:\\d{2})"
    },
    "patterns": {
      "sql_exception": "(?s)exception on sql statement:..."
    }
  },
  "db_pool_size_exceeded": { ... },
  "ftp_per_profile": { ... },
  "http_requests_jasperserver": { ... },
  "catalina_out_jasperserver": { ... }
}
```

### Available Pattern Keys

- `sql_exceptions` - Extract SQL query, error details, and cause
- `db_pool_size_exceeded` - Extract database pool connection info
- `ftp_per_profile` - Extract FTP job information
- `http_requests_jasperserver` - Extract HTTP request logs
- `catalina_out_jasperserver` - Extract Catalina output logs

## Running the Tool

```bash
# From project root
python main.py
```

## License

MIT License

## Author

Jovan 