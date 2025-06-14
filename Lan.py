from telebot import types
from pathlib import Path
from config import bot
from Localization.localization_loader import load_locales_from_folder
Alex_id = 1346718456

# ========================== Языки и флаги ==========================
language_display_names = {
    "русский": "🇷🇺Русский",
    "узбекский": "🇺🇿Oʻzbekcha",
}

lang_code_map = {
    "русский": "ru",
    "узбекский": "uz"
}

# ========================== Классы локализации ==========================
class LocalizedString:
    def __init__(self, key: str, format_queue=None):
        self.key = key
        self.__format_queue = format_queue or []

    def __str__(self):
        return self.localize()

    def localize(self, code: str = "ru"):
        string = translator.get_string(self.key, code)
        if string is None:
            return self.key
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
        self.default_locale = default_locale

    def get_string(self, key, code):
        return self.locales.get(code, {}).get(key)


# ========================== Инициализация ==========================
translator = Translator()
translator.locales = load_locales_from_folder("Localization")

user_language_preferences = {}
chat_language_preferences = {}

# ========================== Главная функция перевода ==========================
def lt(target_id: int, key: str, force_lang: str = None) -> str:
    if force_lang:
        code = force_lang
    else:
        lang = (chat_language_preferences.get(target_id, "русский")
                if target_id < 0 else
                user_language_preferences.get(target_id, "русский"))
        code = lang_code_map.get(lang, "ru")
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


# ========================== Команда /admin_locale ==========================
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
    kb = types.InlineKeyboardMarkup()
    for key in language_display_names:
        kb.add(types.InlineKeyboardButton(
            text=localized_language_name(key),
            callback_data=f"adminset_{key}"
        ))

    bot.reply_to(
        message,
        lt(chat_id, "current_group_language").format(lang=localized_language_name(current)),
        reply_markup=kb
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("adminset_"))
def handle_admin_language_buttons(call):
    chat_id = call.message.chat.id
    user_id = call.from_user.id

    if not is_user_admin(chat_id, user_id):
        bot.answer_callback_query(call.id, lt(user_id, "only_admin"))
        return

    selected = call.data.split("_", 1)[1].lower()
    chat_language_preferences[chat_id] = selected

    bot.answer_callback_query(
        call.id,
        lt(chat_id, "group_language_set").format(lang=localized_language_name(selected))
    )
    bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text=lt(chat_id, "current_group_language_set").format(lang=localized_language_name(selected))
    )


# ========================== Команда /set_l ==========================
@bot.message_handler(commands=["set_l"])
def set_language(message):
    if message.chat.type != "private":
        bot.reply_to(message, lt(message.chat.id, "private_only_language_change"))
        return

    user_id = message.from_user.id
    current = user_language_preferences.get(user_id, "русский")

    kb = types.InlineKeyboardMarkup()
    for key in language_display_names:
        kb.add(types.InlineKeyboardButton(
            text=localized_language_name(key),
            callback_data=key
        ))

    bot.send_message(
        user_id,
        lt(user_id, "current_user_language").format(lang=localized_language_name(current)),
        reply_markup=kb
    )


@bot.callback_query_handler(func=lambda call: call.data in language_display_names)
def handle_language_buttons(call):
    user_id = call.from_user.id
    selected = call.data.lower()

    user_language_preferences[user_id] = selected

    bot.answer_callback_query(
        call.id,
        lt(user_id, "language_set").format(lang=localized_language_name(selected))
    )
    bot.edit_message_text(
        chat_id=user_id,
        message_id=call.message.message_id,
        text=lt(user_id, "current_language_set").format(lang=localized_language_name(selected))
    )
