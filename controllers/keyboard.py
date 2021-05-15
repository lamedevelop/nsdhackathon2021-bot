from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class Keyboard(object):

    @staticmethod
    def inline_option_picker() -> ReplyKeyboardMarkup:
        options = ['income', 'outcome', 'unread']

        buttons = [KeyboardButton(text=k, callback_data="btn") for k in options]
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1).add(*buttons)
        return keyboard
