# save_project_context.ps1
Write-Host "Сохранение контекста проекта..." -ForegroundColor Cyan

# Получаем текущую дату и время
$timestamp = Get-Date -Format "yyyy-MM-dd-HH-mm"
$projectContextFile = "docs/project-context-$timestamp.md"

# Создаем директорию для контекста, если она не существует
if (!(Test-Path "docs")) {
    New-Item -ItemType Directory -Name "docs" | Out-Null
}

# Создаем файл контекста проекта
@"
# Контекст проекта My-CV-Engineering-Projects
Дата сохранения: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

## Текущее состояние проекта

$(if (Test-Path "README.md") { Get-Content "README.md" -Head 20 } else { "README.md не найден" })

## Последние изменения

$(git log -n 5 --pretty=format:"%h - %an, %ar : %s" 2>$null)

## Активные задачи

$(if (Test-Path "TODO.md") { Get-Content "TODO.md" } else { "Нет активных задач" })

## Зависимости

$(if (Test-Path "requirements.txt") { Get-Content "requirements.txt" } else { "Файл зависимостей не найден" })

## Последние файлы контекста

$(Get-ChildItem -Path "docs/ai-conversations/" -Filter "*.md" -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 3 | ForEach-Object { "- $($_.Name) (обновлен: $($_.LastWriteTime))" })

" | Out-File -FilePath $projectContextFile -Encoding UTF8

Write-Host "Контекст проекта сохранен в $projectContextFile" -ForegroundColor Green