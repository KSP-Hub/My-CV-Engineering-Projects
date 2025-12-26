# Getting Started

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/KSP-Hub/My-CV-Engineering-Projects.git
```

2. Перейдите в директорию проекта:
```bash
cd My-CV-Engineering-Projects/CV-010_face_detection
```

3. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
venv\Scripts\activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Быстрый запуск

### Запуск консольного приложения

1. Поместите изображение для анализа в корневую директорию и назовите его `input.jpg`
2. Запустите скрипт:
```bash
python src/face_detection.py
```

### Запуск веб-приложения

1. Запустите сервер:
```bash
python src/CV-010-app.py
```
2. Откройте в браузере: http://localhost:5000
3. Загрузите изображение для анализа

## Проверка установки

Запустите тесты для проверки корректности установки:
```bash
pytest tests/
```

## Возможные проблемы

### Проблема с OpenCV
Если возникают проблемы с установкой OpenCV, попробуйте:
```bash
conda install -c conda-forge opencv
```

### Порт 5000 уже используется
Если порт 5000 занят, завершите процесс:
```bash
netstat -aon | findstr ":5000"
taskkill /PID <PID> /F
```

Или измените порт в `src/CV-010-app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=8080, use_reloader=False)
```
