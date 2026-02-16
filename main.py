from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Токен вашего бота, полученный от BotFather
TOKEN = '6781973654:AAH8YoIyE5YWBQkeooreZGeADLX01_SlMfI'

# Функция старта
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Запустить мини-приложение", web_app={'url': 'https://gushindany1997-wq.github.io/miniature-octo-invention/'})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет! Нажми на кнопку, чтобы запустить мини-приложение.', reply_markup=reply_markup)

# Основная функция
def main():
    # Создание объекта Updater для работы с API Telegram
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Добавление обработчика команды /start
    dp.add_handler(CommandHandler('start', start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()
