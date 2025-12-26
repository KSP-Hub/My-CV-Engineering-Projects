# API Reference

## face_detection_core.py

### Класс `FaceDetectionConfig`

Конфигурация для детекции лиц.

**Атрибуты:**
- `scale_factor` (float): Коэффициент масштабирования. Меньше значение = точнее, но медленнее. По умолчанию: 1.1
- `min_neighbors` (int): Минимальное количество соседей для принятия области как лица. Больше значение = меньше ложных срабатываний. По умолчанию: 5
- `min_size` (tuple): Минимальный размер лица в пикселях (ширина, высота). По умолчанию: (30, 30)
- `max_image_width` (int): Максимальная ширина изображения для веб-интерфейса. По умолчанию: 800

```python
class FaceDetectionConfig:
    def __init__(self):
        self.scale_factor = 1.1
        self.min_neighbors = 5
        self.min_size = (30, 30)
        self.max_image_width = 800
```

### Класс `FaceDetector`

Основной класс для детекции лиц с использованием Haar cascades.

#### Конструктор `__init__(self, config=None)`

Инициализирует детектор лиц.

**Аргументы:**
- `config` (FaceDetectionConfig): Конфигурация детектора. Если None, используется конфигурация по умолчанию.

**Исключения:**
- `FileNotFoundError`: Если файл каскада Хаара не найден
- `ValueError`: Если не удалось загрузить каскад Хаара

```python
class FaceDetector:
    def __init__(self, config=None):
        self.config = config or FaceDetectionConfig()
        # ... инициализация ...
```

#### Метод `detect_faces(self, image_path, output_path=None, resize_for_web=False)`

Детектирует лица на изображении.

**Аргументы:**
- `image_path` (str): Путь к входному изображению
- `output_path` (str, optional): Путь для сохранения результата
- `resize_for_web` (bool): Уменьшить изображение для веб-интерфейса

**Возвращает:**
Словарь с результатами детекции:
```python
{
    'count': int,  # Количество найденных лиц
    'faces': list,  # Список координат лиц [(x, y, w, h), ...]
    'output_path': str,  # Путь к сохраненному файлу (если указан output_path)
    'image': str  # Base64-кодированное изображение для веб-интерфейса
}
```

**Исключения:**
- `FileNotFoundError`: Если файл изображения не найден
- `ValueError`: Если не удалось загрузить изображение

```python
def detect_faces(self, image_path, output_path=None, resize_for_web=False):
    # ... реализация ...
```

#### Метод `display_result(self, image_path)`

Отображает результат детекции в окне OpenCV.

**Аргументы:**
- `image_path` (str): Путь к изображению с результатом

```python
def display_result(self, image_path):
    # ... реализация ...
```

## CV-010-app.py

### Функция `detect_faces_in_image(image_path)`

Функция-обертка для детекции лиц, используемая в веб-приложении.

**Аргументы:**
- `image_path` (str): Путь к изображению для анализа

**Возвращает:**
Результат работы `FaceDetector.detect_faces()`

**Исключения:**
Пробрасывает исключения от `FaceDetector.detect_faces()`

```python
def detect_faces_in_image(image_path):
    # ... реализация ...
```

### Flask API

#### Маршрут `/`

Главная страница веб-интерфейса. Возвращает HTML-страницу с формой загрузки изображения.

**Метод:** GET

#### Маршрут `/upload`

Обработка загрузки изображения.

**Метод:** POST

**Тело запроса:**
- `file` (file): Изображение для анализа

**Возвращает:**
JSON с результатами детекции или ошибкой:
```json
{
    "count": 3,
    "faces": [[100, 50, 80, 80], [300, 60, 75, 75], [500, 45, 85, 85]],
    "output_path": "static/output.jpg",
    "image": "base64-encoded-image-data"
}
```

В случае ошибки:
```json
{
    "error": "No file uploaded"
}
```
