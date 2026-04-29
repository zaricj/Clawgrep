# 🐙 Lobster Log Reporter

A powerful file analysis and pattern extraction tool designed to search through log files, extract structured information using regex patterns, and generate comprehensive reports.

## 🎯 What It Does

Lobster Log Reporter helps you:
- **Search and parse** various types of log files (application logs, SQL, FTP, HTTP, etc.)
- **Extract specific patterns** from log entries using regex-based definitions
- **Structure and organize** unstructured log data into actionable reports
- **Export results** to CSV/Excel for further analysis in spreadsheets
- **Process multiple files** concurrently with parallel threading

## ✨ Key Features

- **Pattern-Based Extraction**: Define regex patterns for different log formats
- **Event Block Extraction**: Identify and extract complete event blocks from logs
- **Multi-Pattern Support**: Match multiple patterns within a single event
- **Threading & Performance**: Parallel file processing with `ThreadPoolExecutor`
- **Progress Tracking**: Visual progress bars with `tqdm`
- **Flexible Configuration**: JSON-based pattern definitions
- **Multiple Export Formats**: CSV and Excel outputs
- **TUI Interface**: Text-based User Interface powered by `textual`

## 📦 Supported Log Formats

- SQL exceptions and errors
- Database pool size exceeded events
- FTP per-profile job logs
- HTTP requests (Jasperserver)
- Catalina output (Jasperserver)
- Custom patterns via JSON configuration

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                Lobster Log Reporter                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌───────────────┐                                              │
│  │   TUI Layer   │   → Rich text-based interface                 │
│  └───────────────┘                                              │
│                                                                  │
│  ┌───────────────────────┐                                      │
│  │   Core Processing     │  → Pipeline orchestration             │
│  │   ┌───────────────┐   │                                      │
│  │   │  parser.py    │  │  → Event extraction & pattern matching│
│  │   │  pipeline.py  │  │                                      │
│  │   │  thread_      │  │  → Parallel processing                │
│  │   │  executor.py  │  │                                      │
│  │   │  timestamp.py │  │  → Time formatting                    │
│  │   │  ui.py        │  │  → TUI components                     │
│  │   │  utils.py     │  │                                      │
│  │   └───────────────┘  │                                      │
│  └───────────────────────┘                                      │
│                                                                  │
│  ┌───────────────────────┐                                      │
│  │   I/O Layer           │  → File operations & exports          │
│  │   ┌───────────────┐   │                                      │
│  │   │  converters   │  │  → Path/epoch conversions              │
│  │   │  exporters.py │  │  → CSV/Excel generation                │
│  │   │  file_utils   │  │                                      │
│  │   └───────────────┘  │                                      │
│  └───────────────────────┘                                      │
│                                                                  │
│  ┌───────────────────────┐                                      │
│  │   Configuration       │  → Pattern definitions                │
│  │   ┌───────────────┐   │                                      │
│  │   │  config.py    │  │  → JSON config loading                │
│  │   └───────────────┘  │                                      │
│  └───────────────────────┘                                      │
│                                                                  │
│  ┌───────────────────────┐                                      │
│  │   Pattern Definitions │  → Regex patterns                     │
│  └───────────────────────┘                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## 📁 Project Structure

```
├── .git/                    # Version control
├── .gitignore               # Git ignore rules
├── .python-version          # Python version specification
├── .vscode/                 # VS Code configuration
├── logs/                    # Application logs
├── src/                     # Source code
│   ├── main.py             # Main application entry
│   └── ...                 # Core modules
├── gui/                     # GUI application (if applicable)
│   ├── main.py             # GUI main entry
│   └── modules.py          # GUI modules
├── modules/                 # Core application modules
│   ├── __init__.py
│   ├── config/             # Configuration management
│   │   └── config.py
│   ├── core/               # Core processing
│   │   ├── parser.py       # Pattern parsing
│   │   ├── pipeline.py     # Pipeline orchestration
│   │   ├── thread_executor.py # Parallel processing
│   │   ├── timestamp.py    # Time formatting
│   │   ├── ui.py          # TUI components
│   │   └── utils.py       # Utility functions
│   └── io/                 # I/O handling
│       ├── converters.py  # Format conversions
│       ├── exporters.py   # CSV/Excel export
│       └── file_utils.py  # File utilities
├── patterns/
│   └── patterns.json       # Pattern definitions
├── output/                 # Generated reports
├── pyproject.toml          # Project configuration
├── uv.lock                 # Dependency lock file
└── README.md               # Documentation
```

## 🚀 Quick Start

### Installation

1. **Prerequisites**: Python 3.13+
2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   ```
3. **Activate environment**:
   ```bash
   # Windows
   .venv\Scripts\Activate.ps1
   
   # Linux/Mac
   source .venv/bin/activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -e .
   ```

### Running the Tool

```bash
# Start from project root
python -m lobsterlogreporter
```

## 📖 Usage Examples

### Basic Pattern Matching

```python
from lobsterlogreporter import run_pipeline

result = run_pipeline(
    patterns_config="patterns/patterns.json",
    pattern_key="sql_exceptions",
    files_directory="logs/",
    file_pattern="*.log",
    output_csv="output/results.csv",
    event_keyword="ERROR",
    show_progress=True
)
```

### Processing Multiple Files

```bash
python src/main.py \
  --patterns patterns/patterns.json \
  --pattern sql_exceptions \
  --files logs/*.log \
  --output output/report.csv \
  --progress
```

## 🔧 Configuration

### Pattern Definitions

Edit `patterns/patterns.json` to define your extraction patterns:

```json
{
  "sql_exceptions": {
    "base": {
      "separator": "^(?P<time>\\d{2}:\\d{2}:\\d{2})"
    },
    "patterns": {
      "sql_exception": "(?s)exception on sql statement:.*?"
    }
  },
  "db_pool_size_exceeded": { ... },
  "ftp_per_profile": { ... }
}
```

### Available Pattern Keys

| Key | Description |
|-----|-------------|
| `sql_exceptions` | Extract SQL query, error details, stack trace |
| `db_pool_size_exceeded` | Extract database pool connection info |
| `ftp_per_profile` | Extract FTP job information |
| `http_requests_jasperserver` | Extract HTTP request logs |
| `catalina_out_jasperserver` | Extract Catalina output logs |
| *(custom)* | Define your own patterns |

## 📊 Output Formats

### CSV Export

Results are exported to CSV files with columns:
- Timestamp
- Pattern matched
- Extracted data
- File source
- Additional fields

### Excel Export

Generate formatted Excel reports with:
- Multiple sheets for different patterns
- Conditional formatting
- Data validation
- Professional styling

## 🛠️ Development

### Dependencies

- `pandas` >= 3.0.2 - Data manipulation
- `rich` >= 15.0.0 - Console formatting
- `textual` >= 8.2.4 - TUI interface
- `textual-dev` >= 1.8.0 - TUI development tools
- `xlsxwriter` >= 3.2.9 - Excel generation
- `tqdm` - Progress bars (if used)

### Adding New Patterns

1. Edit `patterns/patterns.json`
2. Add a new pattern key
3. Define your regex patterns
4. Test in `main.py`

## 🐛 Contributing

To contribute:
1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

## 📄 License

MIT License - Feel free to use and modify!

## 👤 Author

Jovan

---

**Need help?** Check the source code in `src/main.py` or create an issue on the repository.