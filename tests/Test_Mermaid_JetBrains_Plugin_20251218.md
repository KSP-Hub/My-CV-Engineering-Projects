# 📊 Mermaid JetBrains Plugin Test

## Flowchart (Graph)
```mermaid
graph TD
    A[Start] --> B{Data Type}
    B -->|Images| C[Preprocessing]
    B -->|Video| D[Frame Extraction]
    C --> E[Feature Extraction]
    D --> E
    E --> F[Model Inference]
    F --> G[Post-processing]
    G --> H[Results]
    
    classDef process fill:#bbdefb,stroke:#0d47a1
    classDef decision fill:#ffecb3,stroke:#ff8f00
    classDef result fill:#c8e6c9,stroke:#1b5e20
    
    class B decision
    class C,E,F,G process
    class H result
```

## Sequence Diagram
```mermaid
sequenceDiagram
    participant User
    participant API
    participant Model
    participant Database
    
    User->>API: POST /detect
    API->>Model: Preprocess image
    Model-->>API: Features
    API->>Model: Run inference
    Model-->>API: Bounding boxes
    API->>Database: Log results
    Database-->>API: Confirmation
    API-->>User: JSON response
```

## Class Diagram
```mermaid
classDiagram
    class ImageProcessor {
        +load_image(): ndarray
        +resize(): ndarray
        +normalize(): ndarray
        -apply_augmentation(): ndarray
    }
    
    class BaseModel {
        +__init__()
        +train(): None
        +predict(): Results
        #load_weights(): None
    }
    
    class YOLOv8 {
        +detect_objects(): list[BoundingBox]
        +calculate_metrics(): dict
    }
    
    BaseModel <|-- YOLOv8
    ImageProcessor --> BaseModel : provides data
```

## Feedback
- Официальная документация plugin Mermaid JetBrains: https://plugins.jetbrains.com/plugin/20146-mermaid