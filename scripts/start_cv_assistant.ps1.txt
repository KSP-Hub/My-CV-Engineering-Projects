Write-Host "=== ZAPUSK CV ASSISTANT (GPU OPTIMIZED) ===" -ForegroundColor Cyan

# Proverka nalichiya ollama.exe
if (-not (Get-Command "ollama" -ErrorAction SilentlyContinue)) {
    Write-Host "Oshibka: ollama ne naiden v sistemnom puti!" -ForegroundColor Red
    Write-Host "Ubedites, chto Ollama ustanovlen." -ForegroundColor Yellow
    pause
    exit 1
}

# Nastroiki dlya Quadro RTX 4000
Write-Host "Nastroika dlya Quadro RTX 4000 (8GB)..." -ForegroundColor Yellow
$env:OLLAMA_GPU_DEVICES = "0"
$env:OLLAMA_FLASH_ATTENTION = "1"
$env:OLLAMA_NUM_GPU = "35"  # ~5.5GB iz 8GB
$env:OLLAMA_NUM_THREAD = "16"  # 16 iz 20 potokov

# Ostanavlivaem starie protsessi
Write-Host "Ostanovka starikh protsessov Ollama..." -ForegroundColor Yellow
Get-Process -Name "ollama" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 3

# Osvobozhdaem port
Write-Host "Osvobozhdenie porta 11434..." -ForegroundColor Yellow
$portProcess = Get-NetTCPConnection -LocalPort 11434 -ErrorAction SilentlyContinue | Select-Object -First 1
if ($portProcess) {
    Stop-Process -Id $portProcess.OwningProcess -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 2
}

# Zapuskaem server s optimizirovannimi nastroikami
Write-Host "Zapusk servera Ollama s GPU uskoreniem..." -ForegroundColor Yellow
Start-Process -NoNewWindow -FilePath "ollama" -ArgumentList "serve"
Start-Sleep -Seconds 5

# Proveryaem ili sozdayom optimizirovannuyu model
Write-Host "Proverka optimizirovannoi modeli..." -ForegroundColor Yellow
$models = ollama list | Out-String
if ($models -notmatch "cv-rtx4000") {
    Write-Host "Sozdayu optimizirovannuyu model dlya Quadro RTX 4000..." -ForegroundColor Yellow
    # Zdes mozhno dobavit sozdanie modeli iz Modelfile
    # No proshche vruchnuyu sozdat odin raz
    Write-Host "Zapustite komandu vruchnuyu:" -ForegroundColor Red
    Write-Host 'ollama create cv-rtx4000 -f "Modelfile-rtx4000"' -ForegroundColor White
    pause
}

# Predzagruzka modeli
Write-Host "Predzagruzka modeli cv-rtx4000..." -ForegroundColor Yellow
Start-Process -NoNewWindow -FilePath "ollama" -ArgumentList "run", "cv-rtx4000"
Start-Sleep -Seconds 8

Write-Host "`n✅ SISTEMA ZAPUShchENA S GPU USKORENIEM" -ForegroundColor Green
Write-Host "Model: cv-rtx4000 (optimizirovana dlya Quadro RTX 4000)" -ForegroundColor Green
Write-Host "Port: 11434" -ForegroundColor Green
Write-Host "Pamyat GPU: ~5.5GB/8GB" -ForegroundColor Green
Write-Host "Potoki CPU: 16/20" -ForegroundColor Green
Write-Host "`nTeper mozhno otkrivat VS Code." -ForegroundColor Gray