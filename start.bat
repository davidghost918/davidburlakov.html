@echo off
:: Переключение консоли на кодировку UTF-8
chcp 65001 >nul

:: Создание виртуального окружения, если отсутствует
if not exist ".venv" (
    echo Создание виртуального окружения .venv...
    call python -m venv .venv
)

:: Активация виртуального окружения
call .venv\Scripts\activate.bat

:: Установка зависимостей из requirements.txt
if exist "requirements.txt" (
    echo Установка зависимостей из requirements.txt...
    pip install --upgrade pip
    pip install -r requirements.txt
) else (
    echo Файл requirements.txt не найден. Проверьте наличие файла.
    exit /b 1
)

:: Запуск uvicorn
python manage.py runserver

:: Деактивация виртуального окружения после завершения работы
deactivate
