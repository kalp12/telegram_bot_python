# Telegram Weather Bot 🌦️

A Python-based Telegram bot that provides weather forecasts and demonstrates various Telegram Bot API features.

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)

## Features ✨
- **Interactive Commands**: 
  - `/start` - Welcome message
  - `/option` - Inline keyboard buttons
  - `/location` - Request location sharing
- **Weather Forecast**: Get weather predictions using OpenWeatherMap API
- **Location Handling**: Capture and process user location data
- **Message Echo**: Convert text messages to uppercase
- **Callback Queries**: Handle inline button interactions

## Prerequisites 📋
- Python 3.7+
- Telegram Bot Token ([Get from @BotFather](https://core.telegram.org/bots#6-botfather))
- OpenWeatherMap API Key ([Sign up here](https://openweathermap.org/api))
- Basic understanding of Telegram bots

## Installation 🚀

### 1. Clone Repository
```bash
git clone https://github.com/kalp12/telegram_bot_python.git
cd telegram_bot_python
```
### 2. Install Dependencies
```bash
pip install python-telegram-bot pyowm
```
### 3. Configure API Keys
```bash
<!--Replace in main.py:-->
updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN') 
<!--Replace in weather_forecast.py:-->
owm = OWM('YOUR_OPENWEATHERMAP_API_KEY')
```
### Usage 💻
Start the Bot

python main.py
Available Commands
Command	Description
/start	Get welcome message
/option	Show interactive inline keyboard
/location	Request location sharing
### Interactive Features
Inline Buttons: Try /option to see callback button handling

Location Sharing: Use /location to test geolocation features

Weather Forecast: (See weather_forecast.py for standalone usage)

Project Structure 📂

    telegram_bot_python
        ├── main.py                 # Main bot logic
        ├── weather_forecast.py     # Weather API integration
        └── README.md               # Documentation
