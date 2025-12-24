Write-Host "=== PROVERKA SISTEMI CV ASSISTANT ===" -ForegroundColor Cyan
$MY_MODEL = "deepseek-coder:6.7b-instruct"
Write-Host "Tselevaya model: $MY_MODEL" -ForegroundColor Gray
Write-Host ""

$allOk = $true

# 1. Proverka protsessov
Write-Host "[1] Protsessi Ollama: " -NoNewline
$processes = Get-Process -Name "ollama" -ErrorAction SilentlyContinue
if ($processes) {
    Write-Host "ZAPUShchENI ($($processes.Count) sht.)" -ForegroundColor Green
} else {
    Write-Host "NE NAIDENI!" -ForegroundColor Red
    $allOk = $false
}

# 2. Proverka porta
Write-Host "[2] Port 11434: " -NoNewline
try {
    $portCheck = Test-NetConnection -ComputerName localhost -Port 11434 -WarningAction SilentlyContinue -InformationLevel Quiet
    if ($portCheck -eq $true) {
        Write-Host "OTKRIT" -ForegroundColor Green
    } else {
        Write-Host "ZAKRIT" -ForegroundColor Red
        $allOk = $false
    }
} catch {
    Write-Host "OShIBKA PROVERKI" -ForegroundColor Red
    $allOk = $false
}

# 3. Proverka modeli
Write-Host "[3] Dostupnost modeli: " -NoNewline
try {
    $response = Invoke-RestMethod -Uri "http://localhost:11434/api/tags" -Method Get -TimeoutSec 10
    $modelList = $response.models.name -join ", "
    
    if ($response.models.name -contains $MY_MODEL) {
        Write-Host "`"$MY_MODEL`" NAIDENA" -ForegroundColor Green
        Write-Host "   Vse modeli: $modelList" -ForegroundColor Gray
    } else {
        Write-Host "`"$MY_MODEL`" OTSUTSTVUET!" -ForegroundColor Red
        Write-Host "   Dostupno: $modelList" -ForegroundColor Yellow
        $allOk = $false
    }
} catch {
    Write-Host "OShIBKA SVYaZI S SERVEROM" -ForegroundColor Red
    $allOk = $false
}

# Itog
Write-Host ""
Write-Host "=" * 50
if ($allOk) {
    Write-Host "✅ SISTEMA GOTOVA K RABOTE" -ForegroundColor Green
    Write-Host "  Mozhete otkrivat VS Code." -ForegroundColor Gray
} else {
    Write-Host "❌ OBNARUZhENI PROBLEMI" -ForegroundColor Red
    Write-Host "  Zapustite reset_assistant.ps1 dlya perezapuska." -ForegroundColor Yellow
}
Write-Host "=" * 50
pause