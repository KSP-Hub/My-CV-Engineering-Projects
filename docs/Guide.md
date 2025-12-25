# Guide

## Заполнение задач
Пример: 
- [ ] Задача: Демонстрационная задача 1 | Приоритет: P1-P2-P3 | Статус: Backlog, Ongoing, Done | Ответственный: @ИИ @Пользователь | (@ИИ - игноризуй это поле)
- [ ] Задача "@ИИ": Демонстрационная задача 2 (@ИИ - игноризуй это поле)
- [ ] Задача "@Пользователя": Демонстрационная задача 3 (@ИИ - игноризуй это поле)

## Справочник для заполнения проектов
Источник информации: Сайт https://github.com/KSP-Hub/Stanislav-Karamin-Portfolio/blob/main/js/main.js

Code:
```js
    // ============================================
    // Projects Data
    // ============================================
    
    const projectsData = [
        {
            id: 18,
            title: 'Standalone Assistant 2025 for CV development in Python',
            description: 'Создан полностью автономный инструмент для помощи в написании кода на Python для задач компьютерного зрения.',
            fullDescription: 'Проект направлен на создание автономного инструмента для разработчиков и исследователей в сфере компьютерного зрения. Ассистент помогает автоматически создавать и оптимизировать код на Python, используя специализированные библиотеки и технологии глубокого обучения.
             Инструмент разработан с открытым исходным кодом и ориентирован на работу без санкционной зависимости, обеспечивая высокую производительность и интеграцию с основными инструментами разработчика, такими как VS Code.',
            tasks: 'Подготовка: Анализ существующих решений, аналогичных Cursor AI, выявление преимуществ и недостатков. → Настройка и доработка: Настройка ассистента под конкретную аппаратную конфигурацию, проверка производительности и необходимой оптимизации. → Минимально жизнеспособный продукт (MVP): Достижение ключевых показателей качества и документации результатов',
            technologies: ['Python', 'OpenCv', 'NumPy', 'SciPy', 'Tkinter'],
            category: 'ai',
            difficulty: 'advanced',
            date: '2025-11-09',
            image: 'https://raw.githubusercontent.com/KSP-Hub/My-CV-Engineering-Projects/main/Настроить%20Гибридного%20AI-агента%20для%20CV%20проектов/docs/Ai-Assist-image.webp',
            link: '',
            repo: 'https://github.com/KSP-Hub/My-CV-Engineering-Projects/tree/b17143114c9b2cee23461b25e6d119d4722b823a/%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C%20%D0%93%D0%B8%D0%B1%D1%80%D0%B8%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE%20AI-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D0%B0%20%D0%B4%D0%BB%D1%8F%20CV%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%B2/docs',
            hours: 45,
            status: 'done',
            features: ['Автономная работа без зависимости', 'Высокая производительность на GPU', 'Оптимизация под стандартные рабочие станции', 'Работа с большими объёмами данных', 'Свободный интерфейс с возможностью локализации'],
            results: [
                'Полностью автономный AI инструмент для помощи в написании кода для задач технического (компьютерного) зрения, лишённый зависимости от санкционных ограничений',
                'Эффективная поддержка разработчиков и исследователей',
                'Высокопроизводительная локальная инфраструктура для экспериментов',
                'Документированная методология настройки и эксплуатации'
            ]
        },
        {
            id: 17,
            title: 'Style Transfer между изображениями',
            description: 'Перенос художественного стиля между изображениями с использованием нейросетей',
            fullDescription: 'Реализация алгоритма Neural Style Transfer для переноса художественного стиля с одного изображения на другое. Изучение feature extraction из предобученных VGG сетей и оптимизации content и style loss.',
            tasks: 'Загрузить предобученную VGG сеть → Реализовать content и style loss → Настроить оптимизацию → Визуализировать процесс переноса → Эксперименты с различными стилями',
            technologies: ['Python', 'PyTorch', 'Style Transfer', 'VGG', 'Optimization', 'Artistic'],
            category: 'dl',
            difficulty: 'advanced',
            date: '2026-02-09',
            image: '',
            link: '',
            repo: '',
            hours: 35,
            status: 'backlog',
            features: ['Neural Style Transfer', 'Content/Style разделение', 'Визуализация процесса', 'Эксперименты с параметрами'],
            results: [
                'Рабочий алгоритм переноса стиля с настраиваемыми параметрами',
                'Библиотека предобученных стилей для быстрого применения',
                'Оптимизация для обработки изображений высокого разрешения'
            ]
        },
        {
            id: 16,
            title: 'Сегментация изображений U-Net',
            description: 'Семантическая сегментация медицинских изображений с архитектурой U-Net',
            fullDescription: 'Реализация U-Net архитектуры для задач семантической сегментации медицинских изображений. Применение к данным сегментации легких на рентгеновских снимках. Изучение метрик IoU, Dice coefficient и техник обработки медицинских данных.',
            tasks: 'Подготовить медицинский датасет → Реализовать U-Net архитектуру → Настроить loss функции (Dice, BCE) → Обучить модель → Валидация и метрики → Визуализация сегментации',
            technologies: ['Python', 'PyTorch', 'U-Net', 'Medical Imaging', 'Segmentation', 'MONAI'],
            category: 'dl',
            difficulty: 'advanced',
            date: '2026-01-26',
            image: '',
            link: '',
            repo: '',
            hours: 40,
            status: 'backlog',
            features: ['Semantic segmentation', 'Medical imaging', 'Custom loss functions', 'Metrics analysis', '3D визуализация'],
            results: [
                'Сегментация с IoU >0.85 на тестовых медицинских данных',
                'Адаптация архитектуры под специфику медицинских изображений',
                'Сравнение различных loss функций для segmentation задач'
            ]
        },
        {
            id: 15,
            title: 'Детекция объектов с YOLO',
            description: 'Реализация реального детектора объектов с использованием YOLO архитектуры',
            fullDescription: 'Практическая работа с современными архитектурами детекции объектов. Настройка YOLO для обнаружения и классификации объектов в реальном времени. Обучение на custom датасете, оптимизация для различных hardware.',
            tasks: 'Настроить YOLO окружение → Подготовить/разметить датасет → Конфигурирование модели → Обучение и валидация → Тестирование на видео → Оптимизация производительности',
            technologies: ['Python', 'PyTorch', 'YOLO', 'OpenCV', 'Object Detection', 'Ultralytics'],
            category: 'cv',
            difficulty: 'advanced',
            date: '2026-01-12',
            image: '',
            link: '',
            repo: '',
            hours: 45,
            status: 'backlog',
            features: ['Real-time детекция', 'Multi-class классификация', 'Обработка видео', 'Производительность >30 FPS', 'Custom датасет'],
            results: [
                'Детектор объектов с mAP >0.75 на custom датасете',
                'Real-time обработка видео потока с веб-камеры',
                'Сравнение YOLO версий по скорости/точности для различных use cases'
            ]
        },
        {
            id: 14,
            title: 'Transfer Learning для классификации изображений',
            description: 'Использование предобученных моделей для решения конкретной задачи классификации',
            fullDescription: 'Применение transfer learning с использованием предобученных моделей (ResNet, VGG) для классификации изображений из специализированного датасета. Fine-tuning последних слоев под конкретную задачу, изучение техник аугментации данных.',
            tasks: 'Выбрать датасет (CIFAR-10/Cats&Dogs) → Загрузить предобученную модель → Заморозить/разморозить слои → Настроить аугментацию данных → Обучить с fine-tuning → Оценить качество',
            technologies: ['Python', 'PyTorch', 'Transfer Learning', 'ResNet', 'Data Augmentation', 'Torchvision'],
            category: 'dl',
            difficulty: 'intermediate',
            date: '2025-12-29',
            image: '',
            link: '',
            repo: '',
            hours: 35,
            status: 'backlog',
            features: ['Fine-tuning предобученных моделей', 'Расширенная аугментация данных', 'Сравнение подходов', 'Визуализация предсказаний'],
            results: [
                'Модель с точностью >90% на custom датасете',
                'Сравнение эффективности различных предобученных архитектур',
                'Оптимизированный пайплайн fine-tuning для быстрого прототипирования'
            ]
        },
        {
            id: 13,
            title: 'Классификация рукописных цифр CNN',
            description: 'Создание сверточной нейросети для классификации MNIST датасета',
            fullDescription: 'Практическое введение в PyTorch: построение и обучение сверточной нейронной сети для распознавания рукописных цифр. Изучение основ архитектуры CNN, функций потерь, оптимизаторов и техник регуляризации.',
            tasks: 'Загрузить и подготовить MNIST датасет → Создать архитектуру CNN → Настроить training loop → Реализовать валидацию → Визуализировать метрики → Проанализировать ошибки',
            technologies: ['Python', 'PyTorch', 'CNN', 'MNIST', 'Matplotlib', 'Torchvision'],
            category: 'dl',
            difficulty: 'intermediate',
            date: '2025-12-15',
            image: '',
            link: '',
            repo: '',
            hours: 30,
            status: 'backlog',
            features: ['Custom CNN архитектура', 'Визуализация обучения', 'Анализ метрик', 'Регуляризация', 'Инференс на новых данных'],
            results: [
                'CNN модель с точностью >98% на тестовой выборке',
                'Визуализация feature maps и фильтров сети',
                'Сравнение различных архитектур и гиперпараметров'
            ]
        },

            category: 'visualization',
            difficulty: 'intermediate',
            date: '2025-10-05',
            image: 'https://raw.githubusercontent.com/KSP-Hub/Tasks-Solutions-Data-Analysis/refs/heads/main/20251005%20ДЗ_01.%20DataSet%20Coffe%20Sales%20DashBoard_DOC---.png',
            link: 'https://datalens.yandex/v1k9iwk4lxt8g',
            repo: 'https://github.com/KSP-Hub/Tasks-Solutions-Data-Analysis',
            hours: 20,
            status: 'done',
            results: [
                'Создан интерактивный дашборд с ключевыми метриками продаж',
                'Выявлены сезонные тренды и пиковые периоды продаж',
                'Подготовлены рекомендации для оптимизации ассортимента'
            ]
        },
        {
            id: 5,
            title: 'Анализ данных и визуализация в крупном интернет-магазине',
            description: 'Дашборд анализа продаж электронной коммерции за период 2007-2025',
            fullDescription: 'Анализ данных и визуализация продаж в крупном интернет-магазине за период 2007-2025. E-commerce. Подготовка дашборда для руководства с анализом продаж.',
            tasks: 'Проанализировать продажи в крупном интернет-магазине за 2007-2025 и подготовить дашборд для руководства.',
            technologies: ['BI', 'Yandex', 'DataLens', 'CSV', 'ClickHouse', 'Data Visualization', 'SQL'],
            category: 'visualization',
            difficulty: 'advanced',
            date: '2025-10-02',
            image: 'https://raw.githubusercontent.com/KSP-Hub/Tasks-Solutions-Data-Analysis/refs/heads/main/20250928%20ЛБ5%2C%20DataLens%20Dashboard%20—%20Карамин%20С.П.%20РЕШЕНИЕ%20online%20store%20sales%20for%202007-2025----.png',
            link: 'https://datalens.yandex/28ci2emzzssen',
            repo: 'https://github.com/KSP-Hub/Tasks-Solutions-Data-Analysis',
            hours: 30,
            status: 'done',
            results: [
                'Проанализировано 18 лет данных о продажах (2007-2025)',
                'Создан комплексный дашборд с динамическими фильтрами',
                'Выявлены долгосрочные тренды и сезонность продаж',
                'Оптимизированы SQL-запросы для работы с большими объемами данных'
            ]
        },
        {
            id: 4,
            title: 'SQL-запросы для анализа транзакций электронной коммерции',
            description: 'Анализ транзакций электронной коммерции с помощью SQL и генерация отчетов',
            fullDescription: 'Анализ транзакций электронной коммерции с использованием SQL-запросов. Включает анализ транзакций и доставку отчета в формате .docx.',
            tasks: 'Проанализировать транзакции электронной коммерции. Доставить отчет в формате .docx.',
            technologies: ['PostgreSQL', 'DBeaver', 'SQL', 'Common Table Expression', 'CTE'],
            category: 'data-analysis',
            difficulty: 'intermediate',
            date: '2025-09-28',
            image: 'https://raw.githubusercontent.com/KSP-Hub/Tasks-Solutions-Data-Analysis/refs/heads/main/20250928%20ЛБ4.%20E-commerce-transactions-dataset%20—%20РЕШЕНИЕ.%20С.%20П.%20Карамин_page_all---.gif',
            link: 'https://raw.githubusercontent.com/karamin-stanislav/Tasks-Solutions-Data-Analysis/main/20250928%20%D0%9B%D0%914%20E-commerce-transactions-dataset%20%E2%80%94%20%D0%A0%D0%95%D0%A8%D0%95%D0%9D%D0%98%D0%95.%20%D0%A1.%20%D0%9F.%20%D0%9A%D0%B0%D1%80%D0%B0%D0%BC%D0%B8%D0%BD.docx',
            repo: 'https://github.com/KSP-Hub/Tasks-Solutions-Data-Analysis',
            hours: 15,
            status: 'done'
        },
        {
            id: 3,
            title: 'Основы статистики в Excel',
            description: 'Комплексный статистический анализ продаж компании за 2021-2023 годы',
            fullDescription: 'Комплексный статистический анализ продаж компании за 2021-2023 годы, включая тренды и гипотезы. Использование теории вероятностей, регрессии, корреляции и визуализации данных.',
            tasks: 'Провести комплексный статистический анализ продаж компании за 2021-2023 годы, выявить тренды и проверить гипотезы.',
            technologies: ['Excel', 'Statistics', 'Probability Theory', 'Hypothesis', 'Regression', 'Correlation', 'Data Visualization', 'Microsoft'],
            category: 'data-analysis',
            difficulty: 'advanced',
            date: '2025-09-26',
            image: 'https://raw.githubusercontent.com/KSP-Hub/Tasks-Solutions-Data-Analysis/refs/heads/main/20250926%20ЛБ3.%20Excel.%20С.П.%20Карамин%20РЕШЕНИЕ---.gif',
            link: 'https://raw.githubusercontent.com/karamin-stanislav/Tasks-Solutions-Data-Analysis/main/20250926%20%D0%9B%D0%913.%20Excel.%20%D0%A1.%D0%9F.%20%D0%9A%D0%B0%D1%80%D0%B0%D0%BC%D0%B8%D0%BD%20%D0%A0%D0%95%D0%A8%D0%95%D0%9D%D0%98%D0%95.xlsx',
            repo: 'https://github.com/KSP-Hub/Tasks-Solutions-Data-Analysis',
            hours: 18,
            status: 'done'
        },
        {
            id: 2,
            title: 'Анализ данных в Jupyter Notebook на Python',
            description: 'Задачи анализа данных с использованием pandas, numpy и matplotlib',
            fullDescription: 'Анализ данных в Jupyter Notebook с использованием Python. Задача 1: создание Series, очистка DataFrame, анализ данных. Задача 2: исследование заемщиков с использованием pandas, numpy, matplotlib.',
            tasks: 'Задача 1: создать Series, очистить DataFrame, проанализировать данные. Задача 2: исследовать заемщиков с использованием pandas, numpy, matplotlib.',
            technologies: ['Anaconda', 'Python', 'Jupyter', 'Pandas', 'Numpy', 'Matplotlib'],
            category: 'data-analysis',
            difficulty: 'intermediate',
            date: '2025-09-15',
            image: 'https://raw.githubusercontent.com/KSP-Hub/Tasks-Solutions-Data-Analysis/refs/heads/main/20250915%20ЛБ2.%20Основы%20анализа%20данных%20в%20Python.%20РЕШЕНИЕ.%20С.%20П.%20Карамин.%2007.10.2025_page-0001_1_5sek---.gif',
            link: 'https://raw.githubusercontent.com/karamin-stanislav/Tasks-Solutions-Data-Analysis/main/20250915%20%D0%9B%D0%912.%20%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D0%B2%20Python.%20%D0%A0%D0%95%D0%A8%D0%95%D0%9D%D0%98%D0%95.%20%D0%A1.%20%D0%9F.%20%D0%9A%D0%B0%D1%80%D0%B0%D0%BC%D0%B8%D0%BD.%2007.10.2025.ipynb',
            repo: 'https://github.com/KSP-Hub/Tasks-Solutions-Data-Analysis',
            hours: 12,
            status: 'done'
        },
        {
            id: 1,
            title: 'Сбор, обработка и структурирование данных в Jupyter Notebook на Python',
            description: 'Работа с модулями openpyxl и docx для обработки данных',
            fullDescription: 'Сбор, обработка и структурирование данных в Jupyter Notebook с использованием Python. Работа с модулями "openpyxl, docx" для обработки документов.',
            tasks: 'Работа с модулями "openpyxl, docx" в Jupyter notebook для сбора, обработки и структурирования данных.',
            technologies: ['Anaconda', 'Python', 'Jupyter', 'Openpyxl', 'Docx'],
            category: 'data-analysis',
            difficulty: 'beginner',
            date: '2025-09-09',
            image: 'https://raw.githubusercontent.com/KSP-Hub/Tasks-Solutions-Data-Analysis/refs/heads/main/20250909%20ЛБ1.%20Сбор%2C%20обработка%20и%20структурирование%20данных%20С.%20П.%20Карамин%202025%20РЕШЕНИЕ_page_all_1_5sek---.gif',
            link: 'https://raw.githubusercontent.com/karamin-stanislav/Tasks-Solutions-Data-Analysis/main/20250909%20%D0%9B%D0%90%D0%911.%20%D0%A1%D0%B1%D0%BE%D1%80%2C%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0%20%D0%B8%20%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D0%A1.%20%D0%9F.%20%D0%9A%D0%B0%D1%80%D0%B0%D0%BC%D0%B8%D0%BD%202025%20%D0%A0%D0%95%D0%A8%D0%95%D0%9D%D0%98%D0%95.ipynb',
            repo: 'https://github.com/KSP-Hub/Tasks-Solutions-Data-Analysis',
            hours: 8,
            status: 'done'
        }
    ];
    

            // Category mapping
            const categoryMap = {
                'data-analysis': 'Анализ данных',
                'visualization': 'Визуализация',
                'web': 'Веб-разработка',
                'cv': 'Компьютерное зрение',
                'dl': 'Глубокое обучение',
                'ai': 'Искусственный интеллект'
            };
            
            // Difficulty mapping
            const difficultyMap = {
                'beginner': 'Начальный',
                'intermediate': 'Средний',
                'advanced': 'Высокий',
                'высокая': 'Высокая',
                'средняя': 'Средняя',
                'низкая': 'Низкая',
                'начальный': 'Начальный',
                'средний': 'Средний',
                'высокий': 'Высокий'
            };
```
