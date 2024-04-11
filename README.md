# chatBotQR


QR VoiceOver - это Telegram бот, который позволяет пользователю отправлять изображения с QR-кодами, извлекать текст из них и получать озвученный текст в виде голосового сообщения.

## Установка

1. Установите необходимые библиотеки с помощью команды:

    ```
    pip install python-telegram-bot==13.7 pyzbar==0.1.8 Pillow==8.3.2 gtts==2.2.3
    ```

2. Получите токен вашего бота у [BotFather](https://t.me/BotFather) в Telegram.

3. Запустите файл `qr_voice_bot.py`, предоставив ему токен бота.

## Использование

1. Запустите бота.

2. Отправьте боту фотографию с QR-кодом.

3. Получите текст из QR-кода в виде текстового сообщения и озвученный текст в виде голосового сообщения.

## Команды

- `/start` - Начать взаимодействие с ботом и получить приветственное сообщение.
- `/camera` - Получить инструкции о том, как отправить фото с камеры.

## Зависимости

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) (v13.7)
- [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar) (v0.1.8)
- [Pillow](https://github.com/python-pillow/Pillow) (v8.3.2)
- [gtts](https://github.com/pndurette/gTTS) (v2.2.3)

## Авторы

- Локтионова ПС, Замарий ДЕ, Федотов ИВ, Смирнова ЕА - разработчик

## Лицензия

Этот проект лицензируется в соответствии с лицензией [MIT](https://opensource.org/licenses/MIT).
