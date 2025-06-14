import os
import json
import yaml
from pathlib import Path

# Настройки синхронизации
SYNC_YAML_TO_JSON = True    # YAML → JSON
SYNC_JSON_TO_YAML = False    # JSON → YAML

SYNC_ENABLED = SYNC_YAML_TO_JSON or SYNC_JSON_TO_YAML
SUPPORTED_EXTS = [".yaml", ".yml", ".json"]


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def save_json(data: dict, path: Path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_yaml(data: dict, path: Path):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)


def sync_yaml_json(json_path: Path, yaml_path: Path) -> dict:
    json_data = load_json(json_path)
    yaml_data = load_yaml(yaml_path)

    if SYNC_YAML_TO_JSON and not SYNC_JSON_TO_YAML:
        merged = {**json_data, **yaml_data}
    elif SYNC_JSON_TO_YAML and not SYNC_YAML_TO_JSON:
        merged = {**yaml_data, **json_data}
    else:
        merged = {**json_data, **yaml_data}  # YAML приоритетен

    if SYNC_YAML_TO_JSON:
        save_json(merged, json_path)
    if SYNC_JSON_TO_YAML:
        save_yaml(merged, yaml_path)

    return merged


def load_localization_file(path: str) -> dict:
    ext = os.path.splitext(path)[1].lower()
    p = Path(path)

    if ext not in SUPPORTED_EXTS:
        raise ValueError(f"Unsupported localization file format: {ext}")

    alt_ext = ".json" if ext in [".yaml", ".yml"] else ".yaml"
    alt_path = p.with_suffix(alt_ext)

    if SYNC_ENABLED and alt_path.exists():
        return sync_yaml_json(p.with_suffix(".json"), p.with_suffix(".yaml"))

    return load_yaml(p) if ext in [".yaml", ".yml"] else load_json(p)


def load_locales_from_folder(folder: str) -> dict:
    folder_path = Path(folder)
    locales = {}

    for file_path in folder_path.rglob("*"):
        if file_path.suffix.lower() not in SUPPORTED_EXTS:
            continue

        lang_code = file_path.stem.split("_")[-1].lower()
        data = load_localization_file(str(file_path))

        if lang_code not in locales:
            locales[lang_code] = {}

        locales[lang_code].update(data)

    return locales