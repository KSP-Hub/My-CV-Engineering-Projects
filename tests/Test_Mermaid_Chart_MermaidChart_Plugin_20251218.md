# 📈 Mermaid Chart Plugin Test

## Pie Chart
Code:
```mermaid
pie
    title Dataset Distribution
    "Training" : 70
    "Validation" : 15
    "Test" : 15
```

## Gantt Chart
Code:
```mermaid
gantt
    title CV Project Timeline
    dateFormat  YYYY-MM-DD
    section Data Preparation
    Data Collection       :a1, 2024-01-01, 14d
    Preprocessing         :a2, after a1, 7d
    
    section Model Development
    Architecture Design   :b1, 2024-01-15, 5d
    Training              :b2, after b1, 10d
    Evaluation            :b3, after b2, 5d
    
    section Deployment
    API Development       :c1, after b3, 7d
    Testing               :c2, after c1, 3d
```

## State Diagram
Code:
```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing: start()
    Processing --> Analyzing: data_ready
    Analyzing --> Idle: complete
    Analyzing --> Error: timeout
    Error --> Idle: reset()
    
    state Processing {
        [*] --> Preprocess
        Preprocess --> FeatureExtraction
        FeatureExtraction --> ModelInference
        ModelInference --> [*]
    }
```

## Mindmap

- Mindmap | Mermaid: https://mermaid.js.org/syntax/flowchart.html#mindmap

### An example of a mindmap.
Code:
```mermaid
mindmap
    root((mindmap))
        Origins
            Long history
            ::icon(fa fa-book)
            Popularisation
            British popular psychology author Tony Buzan
        Research
            On effectiveness<br/>and features
            On Automatic creation
                Uses
                    Creative techniques
                    Strategic planning
                    Argument mapping
        Tools
            Pen and paper
            Mermaid
```


### Markdown Strings
Функция "Markdown Strings" расширяет возможности интеллектуальных карт, предлагая более универсальный тип строк, который поддерживает такие параметры форматирования текста, как полужирный шрифт и курсив, и автоматически переносит текст в метки.

Code:
```mermaid
mindmap
id1["`**Root** with 
a second line 
Unicode works too: 🤓`"]
    id2["`The dog in **the** hog... a *very long text* that wraps to a new line`"]
        id2.1["`**Bold** and _italic_ text`"]
    id3[Regular labels still works]
        id3.1["`**Bold** and _italic_ text`"]
            id3.1.1["https://mermaid.js.org/"]
        id3.2["`**Bold** and _italic_ text`"]
        id3.3["`**Bold** and _italic_ text`"]
```


### Tidy-tree Layout (Аккуратный древовидный макет)
Структура tidy-tree упорядочивает узлы в иерархическом древовидном порядке. Она особенно полезна для диаграмм, где важны отношения «родитель-потомок», например, для интеллект-карт.

#### Features (Особенности)
Упорядочивает узлы в виде аккуратного, неперекрывающегося дерева
Идеально подходит для ментальных карт и иерархических данных
Автоматически регулирует интервалы для удобства чтения

#### Example Usage (Пример использования)

Code 1:
```mermaid
---
config:
    layout: tidy-tree
---
mindmap
root((mindmap is a long thing))
    A
    B
        B1   
    C
    D
```

Code 2:
```mermaid
---
config:
  layout: tidy-tree
---
mindmap
root((mindmap))
    Origins
    ::icon(fa-solid fa-book)
      Long history
      ::icon(fa fa-book)
      Popularisation
      ::icon(fa-solid fa-bookmark)
        British popular psychology author Tony Buzan
    Research
    ::icon("fas fa-book")
      On effectiveness <br/> and features
      On Automatic creation
      ::icon('fa-solid fa-bookmark')
        Uses <br/> <!-- @html private commit -->
            Creative techniques
            ::icon(fa fa-bookmark red-color)
            Strategic planning
            ::icon(fa fa-spin)
            Argument mapping
```

## Icons
Итсочник: https://fontawesome.ru/all-icons/

## Feedback
- Круто! Красиво. Всё работает исправно
- [Mermaid Live Editor](https://mermaid.live/edit#pako:eNpdkk9vnDAQxb_KyKddiW4DLLsBVZWS9NgoUZtcKi4ODGAVZujYjkpW-93r_UOShouZ33vzPLJmpyquURVqMFQPeiwJQJjdYnEGy-UBAdyJaQ3ZUwHwnamFzljHMs2sKEzFtGg0NPrTE_Pv5azc8-h7LcZqZ5hmCnAtxhnbwXjSYbRT1XHP7QTau44FHpgmuPYv-tz1Ay1qqbo5444AmwYrZ56R0NovT_L5q6YaGtTOC9p3xivveAgTVFAJfpjk0b5ZT9_N0fOM4LDqyPzxHw0_nWiHbYgbe01kqP1fv5LWD0gOwiuOr-oDc_8u6B4JDuOOekR5w7cogza1ilQr4SiceIzUcKaF2h2spXIdDliqIvzW2Gjfu1KVtA9to6ZfzMPcKezbThWN7m2o_FiHyb8Z3YoeXqkg1Sg37MmpIj5GqGKn_oYiTleb7WWex1mSbuNsk0VqCnidrpJ0vU2yNI0v8jTb7CP1crz1YrXJA8zjdRJvs8skXkcKaxO25fa0bset2_8DFgrEnQ)
- Официальная документация Mermaid ChartE
  - 1: https://plugins.jetbrains.com/vendor/mermaid-chart
  - 2: https://mermaid.js.org/
