# check_context.ps1
Write-Host "Проверка контекста проекта..." -ForegroundColor Cyan

# Проверяем наличие файлов контекста
if (Test-Path "docs/ai-conversations/") {
    $contextFiles = Get-ChildItem -Path "docs/ai-conversations/" -Filter "*.md" -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 3
    
    Write-Host "Найдено файлов контекста: $($contextFiles.Count)" -ForegroundColor Green
    
    foreach ($file in $contextFiles) {
        Write-Host "  - $($file.Name) (обновлен: $($file.LastWriteTime))" -ForegroundColor Gray
    }
} else {
    Write-Host "Директория контекста не найдена" -ForegroundColor Yellow
}

# Проверяем статус проекта
if (Test-Path "project-status.json") {
    $status = Get-Content "project-status.json" | ConvertFrom-Json
    Write-Host "Статус проекта: $($status.status)" -ForegroundColor Green
    Write-Host "Текущая фаза: $($status.current_phase)" -ForegroundColor Yellow
    
    if ($status.completed_tasks) {
        Write-Host "Завершенные задачи:" -ForegroundColor Green
        $status.completed_tasks | ForEach-Object { Write-Host "  - $_" -ForegroundColor Gray }
    }
    
    if ($status.next_tasks) {
        Write-Host "Следующие задачи:" -ForegroundColor Cyan
        $status.next_tasks | ForEach-Object { Write-Host "  - $_" -ForegroundColor Gray }
    }
} else {
    Write-Host "Файл статуса проекта не найден" -ForegroundColor Red
}

# Проверяем наличие скриптов AI-ассистента
Write-Host "`nПроверка скриптов AI-ассистента:" -ForegroundColor Cyan
$assistantScripts = @("start_cv_assistant.ps1", "check_assistant.ps1", "reset_assistant.ps1")
foreach ($script in $assistantScripts) {
    if (Test-Path "scripts/$script") {
        Write-Host "  ✅ $script" -ForegroundColor Green
    } else {
        Write-Host "  ❌ $script" -ForegroundColor Red
    }
}