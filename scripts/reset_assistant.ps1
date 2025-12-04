Write-Host "=== AVARIINII SBROS CV ASSISTANT ===" -ForegroundColor Red

Write-Host "1. Ostanavlivaem VSE protsessi Ollama..." -ForegroundColor Yellow
Get-Process -Name "ollama" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2

Write-Host "2. Proveryaem i osvobozhdaem port 11434..." -ForegroundColor Yellow
$portProcess = Get-NetTCPConnection -LocalPort 11434 -ErrorAction SilentlyContinue | Select-Object -First 1
if ($portProcess) {
    Write-Host "   Obnaruzhen protsess (PID: $($portProcess.OwningProcess)). Ostanavlivayu..." -ForegroundColor Red
    Stop-Process -Id $portProcess.OwningProcess -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 2
}

Write-Host "3. Zapuskaem sistemu zanovo..." -ForegroundColor Yellow
$env:OLLAMA_GPU_DEVICES="0"
$env:OLLAMA_FLASH_ATTENTION="1"
Start-Process -NoNewWindow -FilePath "ollama" -ArgumentList "serve"
Start-Sleep -Seconds 5

Write-Host "4. Predzagruzka modeli..." -ForegroundColor Yellow
Start-Process -NoNewWindow -FilePath "ollama" -ArgumentList "run", "deepseek-coder:6.7b-instruct"
Start-Sleep -Seconds 5

Write-Host "`n[USPEKh] Sistema polnostyu perezapushchena!" -ForegroundColor Green
Write-Host "Proverte rabotu v VS Code." -ForegroundColor Green
Write-Host "Dlya proverki zapustite check_assistant.ps1" -ForegroundColor Gray
pause