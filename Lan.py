from telebot import types
import json
import os

from pathlib import Path

from telebot import TeleBot

from Localization.localization_loader import load_locales_from_folder, load_localization_file

# Если хочешь использовать через бота — импортируй его
from config import bot
Alex_id = 1346718456
# ========================== Отображаемые имена языков (с флагами) ==========================
language_display_names = {
    "русский": "🇷🇺Русский",
    "узбекский": "uzO'zbekcha"
    #"английский": "🇬🇧English",
    #"украинский": "🇺🇦Українська",
}

# ========================== Локализация текстов из JSON ==========================

class LocalizedString:
    def __init__(self, key: str, format_queue=None):
        self.key = key
        self.__format_queue = format_queue or []

    def __str__(self):
        return self.localize()

    def localize(self, code: str = "ru"):
        string = translator.get_string(self.key, code)
        if string is None:
            string = self.key
        for fmt in self.__format_queue:
            string = fmt(string)
        return string

    def format(self, *args, **kwargs):
        def fmt(s): return s.format(*args, **kwargs)
        copy = LocalizedString(self.key, self.__format_queue.copy())
        copy.__format_queue.append(fmt)
        return copy


class Translator:
    def __init__(self, default_locale="ru"):
        self.locales = {}

    def load_locale(self, code, *paths):
        self.locales.setdefault(code, {})
        for p in paths:
            try:
                self.locales[code].update(load_localization_file(p))
            except Exception as e:
                print(f"[Translator] Failed to load {p}: {e}")

    def get_string(self, key, code):
        return self.locales.get(code, {}).get(key)


def auto_load_locales(translator, base_dir="Localization"):
    base = Path(base_dir)
    files = list(base.glob("*.*")) + list(base.rglob("*.*"))  # добавляем и корень, и вложенные

    seen = set()
    language_buckets = {}

    for file in files:
        if file.suffix.lower() not in [".yaml", ".yml", ".json"]:
            continue

        if file in seen:
            continue
        seen.add(file)

        name_without_ext = file.stem  # имя файла без расширения
        lang_code = name_without_ext.split("_")[-1].lower()  # берём последний элемент после "_"

        language_buckets.setdefault(lang_code, []).append(str(file))

    for lang_code, paths in language_buckets.items():
        translator.load_locale(lang_code, *paths)



# Используем авто-загрузку
translator = Translator()
auto_load_locales(translator, base_dir="Localization")


user_language_preferences = {}
chat_language_preferences = {}


def lt(target_id: int, key: str, force_lang: str = None) -> str:
    if force_lang:
        code = force_lang
    else:
        lang = (chat_language_preferences.get(target_id, "узбекский")
                if target_id < 0 else
                user_language_preferences.get(target_id, "узбекский"))
        code = {"русский": "ru", "узбекский": "uz"}.get(lang, "ru")
    return LocalizedString(key).localize(code)


def localized_language_name(lang_key: str) -> str:
    return language_display_names.get(lang_key, language_display_names["русский"])

# ========================== Проверка админа ==========================


def is_user_admin(chat_id, user_id):
    if user_id == Alex_id:
        return True
    try:
        return bot.get_chat_member(chat_id, user_id).status in ("administrator", "creator")
    except:
        return False

# ========================== /admin_locale ==========================

@bot.message_handler(commands=["admin_locale"])
def admin_set_language(message):
    user_id = message.from_user.id

    if message.chat.type == "private":
        bot.reply_to(message, lt(user_id, "only_in_groups"))
        return

    chat_id = message.chat.id
    if not is_user_admin(chat_id, user_id):
        bot.reply_to(message, lt(user_id, "only_admin"))
        return

    current = chat_language_preferences.get(chat_id, "русский")

    # Строим inline-клавиатуру с флагами
    kb = types.InlineKeyboardMarkup()
    for key in ["русский", "узбекский"]:
        kb.add(types.InlineKeyboardButton(
            text=localized_language_name(key),
            callback_data=f"adminset_{key}"
        ))

    # Текст заголовка локализуем по чату
    bot.reply_to(
        message,
        lt(chat_id, "current_group_language")
           .format(lang=localized_language_name(current)),
        reply_markup=kb
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("adminset_"))
def handle_admin_language_buttons(call):

    chat_id = call.message.chat.id
    user_id  = call.from_user.id
    username = call.from_user.username or ""

    if not is_user_admin(chat_id, user_id):
        bot.answer_callback_query(call.id, lt(user_id, "only_admin"))
        return

    selected = call.data.split("_", 1)[1].lower()
    chat_language_preferences[chat_id] = selected

    # Подтверждение по чату
    bot.answer_callback_query(
        call.id,
        lt(chat_id, "group_language_set")
           .format(lang=localized_language_name(selected))
    )
    bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text=lt(chat_id, "current_group_language_set").format(lang=localized_language_name(selected))
    )

    if selected == "узбекский":
        bot.send_message(chat_id, lt(chat_id, "uz_gratitude"))


# ========================== /set_l ==========================


@bot.message_handler(commands=["set_l"])
def set_language(message):
    if message.chat.type != "private":
        bot.reply_to(message, lt(message.chat.id, "private_only_language_change"))
        return

    user_id = message.from_user.id
    current = user_language_preferences.get(user_id, "русский")

    kb = types.InlineKeyboardMarkup()
    for key in ["русский", "узбекский"]:
        kb.add(types.InlineKeyboardButton(
            text=localized_language_name(key),
            callback_data=key
        ))

    bot.send_message(
        user_id,
        lt(user_id, "current_user_language").format(lang=localized_language_name(current)),
        reply_markup=kb
    )
    
@bot.callback_query_handler(func=lambda call: call.data in ["русский", "узбекский"])
def handle_user_language_buttons(call):
    user_id = call.from_user.id
    selected = call.data.lower()
    user_language_preferences[user_id] = selected

    # Подтверждение (всплывающее сообщение)
    bot.answer_callback_query(
        call.id,
        lt(user_id, "language_set").format(lang=localized_language_name(selected))
    )

    # Редактируем исходное сообщение
    bot.edit_message_text(
        chat_id=user_id,
        message_id=call.message.message_id,
        text=lt(user_id, "current_language_set").format(lang=localized_language_name(selected))
    )

    # Дополнительное сообщение при выборе узбекского (если нужно)
    if selected == "узбекский":
        bot.send_message(user_id, lt(user_id, "uz_gratitude"))

