# Glavnii skript sinkhronizatsii - zapustite etot fail pervim!
Write-Host "=== SINKhRONIZATsIYa CV ASSISTANT ===" -ForegroundColor Cyan
Write-Host "Kopiruyu vse skripti v pravilnie mesta..." -ForegroundColor Yellow

# Opredelyaem puti
$projectPath = "D:\Apps\GitHub\KSP-Hub\My-CV-Engineering-Projects"
$scriptsPath = Join-Path $projectPath "scripts"

# Sozdaem papku scripts v proekte
if (-not (Test-Path $scriptsPath)) {
    New-Item -ItemType Directory -Path $scriptsPath -Force
}

# Kopiruem skripti
$scriptFiles = @(
    "check_assistant.ps1",
    "reset_assistant.ps1", 
    "start_cv_assistant.ps1"
)

foreach ($file in $scriptFiles) {
    $source = Join-Path $PSScriptRoot $file
    $dest = Join-Path $scriptsPath $file
    if (Test-Path $source) {
        Copy-Item -Path $source -Destination $dest -Force
        Write-Host "✓ $file skopirovan v $scriptsPath" -ForegroundColor Green
    } else {
        Write-Host "⚠ $file ne naiden v tekushchei papke" -ForegroundColor Yellow
    }
}

Write-Host "`n✅ Sinkhronizatsiya zavershena!" -ForegroundColor Green
Write-Host "Pereidite v papku proekta:" -ForegroundColor Gray
Write-Host "cd `"$projectPath`"" -ForegroundColor White
Write-Host "Zatem zapustite proverku:" -ForegroundColor Gray
Write-Host ".\scripts\check_assistant.ps1" -ForegroundColor White
Write-Host "`nEsli vozniknut oshibki prav dostupa, zapustite PowerShell ot imeni administratora"
pause