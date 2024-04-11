# chatBotQR


QR VoiceOver - это Telegram бот, который позволяет пользователю отправлять изображения с QR-кодами, извлекать текст из них и получать озвученный текст в виде голосового сообщения.

## Установка
Для установки необходим [Python](https://www.python.org/downloads/release/python-3100/) (v3.10)

1. Установите необходимые библиотеки с помощью команды:

    ```shell
    pip install -r requirements.txt
    ```
   или
   ```shell
   pip install python-telegram-bot==13.7 pyzbar==0.1.8 Pillow==8.3.2 gtts==2.2.3
   ```

2. Получите токен вашего бота у [BotFather](https://t.me/BotFather) в Telegram.

3. Запустите файл `main.py`, предварительно предоставив ему токен бота.

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

- Замарий ДЕ, Локтионова ПС, Смирнова ЕА, Федотов ИВ  - разработчики

## Лицензия

Этот проект лицензируется в соответствии с лицензией [MIT](https://opensource.org/licenses/MIT).
