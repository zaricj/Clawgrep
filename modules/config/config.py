import re
from pathlib import Path

from modules.utils.utilities import load_patterns_json, compile_regex_patterns
from modules.io.file_utils import validate_input

# ========== Config ==========

def load_config(patterns_config: Path, pattern_key: str) -> tuple[dict, re.Pattern]:
    # Validate if patterns config exists
    if not validate_input(patterns_config):
        raise FileNotFoundError(f"Patterns config file not found: {patterns_config}")

    # Load and validate patterns JSON
    patterns_json = load_patterns_json(patterns_config)
    validate_config(patterns_json)

    # Validate pattern_key exists
    if pattern_key not in patterns_json:
        raise ValueError(f"Invalid pattern key: '{pattern_key}'. Available keys: {list(patterns_json.keys())}")

    # Compile patterns for the selected category
    compiled = compile_regex_patterns(patterns_json[pattern_key])
    header_regex = compiled["base"]["header"]

    return compiled, header_regex


def validate_config(patterns_json: dict[str, dict[str, dict[str, str]]]):
    """
    Validate the structure and content of the patterns JSON.
    
    Expected structure:
    >>> {
        "category_name": {
            "base": {
                "header": "regex_string"
            },
            "patterns": {
                "pattern_name": "regex_string",
                ...
            }
        },
        ...
    }
    """
    if not isinstance(patterns_json, dict):
        raise TypeError("patterns_json must be a dictionary")
    
    for category_name, category_config in patterns_json.items():
        if not isinstance(category_config, dict):
            raise TypeError(f"Category '{category_name}' must be a dictionary")
        
        # Check required keys
        if "base" not in category_config:
            raise ValueError(f"Category '{category_name}' missing 'base' section")
        if "patterns" not in category_config:
            raise ValueError(f"Category '{category_name}' missing 'patterns' section")
        
        # Validate base section
        base = category_config["base"]
        if not isinstance(base, dict):
            raise TypeError(f"'base' in category '{category_name}' must be a dictionary")
        if "header" not in base:
            raise ValueError(f"'base' in category '{category_name}' missing 'header'")
        if not isinstance(base["header"], str):
            raise TypeError(f"'header' in category '{category_name}' must be a string")
        
        # Validate patterns section
        patterns = category_config["patterns"]
        if not isinstance(patterns, dict):
            raise TypeError(f"'patterns' in category '{category_name}' must be a dictionary")
        for pattern_name, pattern_regex in patterns.items():
            if not isinstance(pattern_regex, str):
                raise TypeError(f"Pattern '{pattern_name}' in category '{category_name}' must be a string")
        
        # Validate regex compilation
        try:
            re.compile(base["header"])
        except re.error as e:
            raise ValueError(f"Invalid regex in 'header' for category '{category_name}': {e}")
        
        for pattern_name, pattern_regex in patterns.items():
            try:
                re.compile(pattern_regex, re.MULTILINE | re.DOTALL)
            except re.error as e:
                raise ValueError(f"Invalid regex in pattern '{pattern_name}' for category '{category_name}': {e}")