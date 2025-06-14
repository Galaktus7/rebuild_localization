
import os
import json
import yaml
from pathlib import Path
from telebot.types import Message
from telebot import TeleBot

from Localization.localization_loader import load_locales_from_folder
# Если хочешь использовать через бота — импортируй его
from Config import bot
Alex_id = 1346718456
user_language = {}  # user_id: "ru" / "uz"

# Настройка: какие файлы подключать
language_files = {
    "ru": [
        "glossary_ru.yaml",
        "game_ru.yaml",
        "weapons_ru.yaml"
    ],
    "uz": [
        "glossary_uz.yaml",
        "game_uz.yaml",
        "weapons_uz.yaml"
    ]
}

def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def save_json(data: dict, path: Path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_yaml(data: dict, path: Path):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

def load_localization_file(path: str) -> dict:
    ext = os.path.splitext(path)[1].lower()
    p = Path(path)
    if ext == ".json":
        return load_json(p)
    elif ext in [".yaml", ".yml"]:
        return load_yaml(p)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

# Загружаем всё в один словарь
def load_language(lang_code: str) -> dict:
    result = {}
    for file in language_files.get(lang_code, []):
        path = Path("Localization") / file
        if path.exists():
            data = load_localization_file(str(path))
            if isinstance(data, dict):
                result.update(data)
    return result

# Загрузка всех языков
localizations = {
    lang: load_language(lang)
    for lang in language_files
}

# Получение языка пользователя (по умолчанию — ru)
def get_lang(user_id: int) -> str:
    return user_language.get(user_id, "ru")

# Получение локализованной строки
def lt(user_id: int, key: str, default: str = "") -> str:
    lang = get_lang(user_id)
    return localizations.get(lang, {}).get(key, default)

# Для отладки/информирования
def localized_language_name(code: str) -> str:
    return {
        "ru": "Русский 🇷🇺",
        "uz": "O‘zbek 🇺🇿"
    }.get(code, code)

# Команда для установки языка
@bot.message_handler(commands=["admin_locale"])
def set_locale(message: Message):
    uid = message.from_user.id
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Пример: /admin_locale ru или /admin_locale uz")
        return
    lang = args[1].strip().lower()
    if lang not in localizations:
        bot.reply_to(message, f"Язык '{lang}' не поддерживается.")
        return
    user_language[uid] = lang
    bot.reply_to(message, f"✅ Установлен язык: {localized_language_name(lang)}")

