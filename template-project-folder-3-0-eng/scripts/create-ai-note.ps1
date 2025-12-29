# create-ai-note.ps1
# 
# 🎯 Назначение: автоматически создаёт .md файл для фиксации разговора с AI
# - Имя файла: дата_время.md (например, 2025-12-18_11-30-45.md)
# - Папка назначения: ai-conversations/
# - Содержит метаданные: дату, время, тему (опционально)
#
# 💡 Как использовать:
#   .\scripts\create-ai-note.ps1 -Topic "Настройка .gitignore и хуки"
#   или просто:
#   .\scripts\create-ai-note.ps1

param (
    [string]$Topic = "Без темы"
)

# Пути
$notesDir = "D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects/ai-conversations"
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$filename = "$timestamp.md"
$filepath = Join-Path $notesDir $filename

# Содержимое заметки
$content = @"
# Запись разговора с AI-ассистентом

- **Дата:** $(Get-Date -Format "yyyy-MM-dd")
- **Время:** $(Get-Date -Format "HH:mm:ss")
- **Тема:** $Topic

## Обсуждение

<!-- Вставьте здесь основной диалог или вывод -->

## Решения

- 

## Действия

1. 

## Ссылки

- 
"@ 

# Создание файла
if (-not (Test-Path $notesDir)) {
    New-Item -ItemType Directory -Path $notesDir -Force | Out-Null
    Write-Host "✅ Создана папка: $notesDir"
}

Set-Content -Path $filepath -Value $content -Encoding UTF8
Write-Host "✅ Создана запись: $filepath"