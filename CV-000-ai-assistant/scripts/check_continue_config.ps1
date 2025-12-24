Write-Host "=== PROVERKA KONFIGURATsII CONTINUE ===" -ForegroundColor Cyan

# Put k konfigu Continue
$continueConfigPath = "$env:USERPROFILE\.continue\config.json"

if (Test-Path $continueConfigPath) {
    Write-Host "Konfiguratsionnii fail naiden:" -ForegroundColor Green
    Write-Host $continueConfigPath -ForegroundColor Gray
    
    try {
        $config = Get-Content $continueConfigPath -Raw | ConvertFrom-Json
        Write-Host "`nNastroiki modelei:" -ForegroundColor Yellow
        
        if ($config.models) {
            foreach ($model in $config.models) {
                Write-Host "  • Nazvanie: $($model.title)" -ForegroundColor White
                Write-Host "    Model: $($model.model)" -ForegroundColor Gray
                Write-Host "    Provaider: $($model.provider)" -ForegroundColor Gray
                Write-Host "    API: $($model.apiBase)" -ForegroundColor Gray
                Write-Host ""
            }
        } else {
            Write-Host "  ❌ Modeli ne nastroeni v konfige" -ForegroundColor Red
        }
    } catch {
        Write-Host "  ❌ Oshibka chteniya konfiguratsii" -ForegroundColor Red
    }
} else {
    Write-Host "Konfiguratsionnii fail NE naiden!" -ForegroundColor Red
    Write-Host "Sozdaite konfig cherez VS Code: F1 -> 'Continue: Open Config'" -ForegroundColor Yellow
}

Write-Host "`nOzhidaemaya konfiguratsiya:" -ForegroundColor Cyan
Write-Host '{
  "models": [
    {
      "title": "Local CV Expert",
      "model": "deepseek-coder:6.7b-instruct",
      "apiBase": "http://localhost:11434",
      "provider": "ollama"
    }
  ]
}' -ForegroundColor Gray

pause