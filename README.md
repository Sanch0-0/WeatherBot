# WeatherBot

WeatherBot - это телеграм-бот для получения информации о погоде.

## Установка и запуск

1. Склонируйте репозиторий и перейдите в папку проекта:

    ```sh
    git clone git@github.com:Sanch0-0/WeatherBot.git
    cd WeatherBot
    ```

2. Создайте и активируйте виртуальное окружение:

    ```sh
    python -m venv venv
    venv\Scripts\activate  # Для Windows
    source venv/bin/activate  # Для Linux/Mac
    ```

3. Установите зависимости:

    ```sh
    pip install -r requirements.txt
    ```

4. Переименуйте файл `.env.example` в `.env` и добавьте ваши токены:

    ```sh
    mv .env.example .env
    ```

    Откройте файл `.env` и укажите свои токены:

    ```env
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    WEATHER_API_KEY=your_weather_api_key
    ```

5. Запустите бота:

    ```sh
    python main.py
    ```

Теперь ваш бот готов к использованию!

