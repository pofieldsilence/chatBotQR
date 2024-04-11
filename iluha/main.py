import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from pyzbar.pyzbar import decode
from PIL import Image
from gtts import gTTS
from io import BytesIO


# Функция для обработки команды /start
def start(update, context):
    update.message.reply_text( "Привет! Отправь мне фотографию с QR-кодом, и я извлеку текст и озвучу его. "
                               "Если у тебя нет фотографии, можешь воспользоваться командой /camera, чтобы сделать фото и отправить его мне.")


# Функция для обработки команды /camera
def camera(update, context):
    update.message.reply_text(
        "Чтобы сделать фото, нажмите на иконку камеры в поле ввода сообщения и сфотографируйте QR-код. "
        "Затем отправьте полученное фото мне.")


# Функция для обработки входящих сообщений с изображением QR-кода
def qr_handler(update, context):
    # Получаем объект фотографии из сообщения пользователя
    photo = update.message.photo[-1].get_file()
    # Скачиваем фото в буфер
    photo_bytes = photo.download_as_bytearray()
    # Открываем изображение с помощью Pillow
    image = Image.open( BytesIO( photo_bytes ) )
    # Извлекаем текст с помощью pyzbar
    decoded_objects = decode( image )
    # Получаем текст из QR-кода
    qr_text = decoded_objects[0].data.decode( 'utf-8' )

    # Озвучиваем текст с помощью gTTS
    tts = gTTS( text=qr_text, lang='ru' )
    # Сохраняем озвученный текст в файл
    audio_file = BytesIO()
    tts.write_to_fp( audio_file )
    audio_file.seek( 0 )

    # Отправляем приветствие и озвученный текст пользователю
    update.message.reply_text( "Текст из QR-кода:" )
    update.message.reply_text( qr_text )
    update.message.reply_voice( voice=audio_file )


# Токен вашего бота
TOKEN = '7121354724:AAELCJhIA7ArQavEpGBUxoFJEsX1NzaBRvQ'

# Создаем экземпляр бота
bot = telegram.Bot( token=TOKEN )
# Получаем апдейтер для получения сообщений от пользователя
updater = Updater( token=TOKEN, use_context=True )
dispatcher = updater.dispatcher

# Обработчики команд
dispatcher.add_handler( CommandHandler( "start", start ) )
dispatcher.add_handler( CommandHandler( "camera", camera ) )
# Обработчик для сообщений с изображением
dispatcher.add_handler( MessageHandler( Filters.photo, qr_handler ) )

# Запускаем бота
updater.start_polling()
updater.idle()
