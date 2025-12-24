# sync_from_cloud.ps1 - Skript zagruzki konteksta iz oblaka
Write-Host "=== ZAGRUZKA KONTEKSTA IZ OBLAKA ===" -ForegroundColor Cyan

# Proverka nalichiya Yandex CLI
if (-not (Get-Command "yc" -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Yandex CLI ne naiden!" -ForegroundColor Red
    Write-Host "Ustanovite Yandex CLI iz ofitsialnogo istochnika" -ForegroundColor Yellow
    exit 1
}

# Proverka avtorizatsii v Yandex Cloud
try {
    $profile = yc config profile get default -q 2>$null
    if (-not $profile) {
        Write-Host "❌ Ne avtorizovany v Yandex Cloud!" -ForegroundColor Red
        Write-Host "Zapustite: yc init dlya avtorizatsii" -ForegroundColor Yellow
        exit 1
    }
} catch {
    Write-Host "❌ Oshibka proverki avtorizatsii v Yandex Cloud!" -ForegroundColor Red
    exit 1
}

# Opredelenie putey
$projectRoot = "D:\Apps\GitHub\KSP-Hub\My-CV-Engineering-Projects"
$docsPath = Join-Path $projectRoot "docs"
$contextPath = Join-Path $docsPath "ai-conversations"
$projectStatusFile = Join-Path $projectRoot "project-status.json"
$tempArchive = Join-Path $projectRoot "temp_context_download.zip"

Write-Host "Zagruzka arkhiva konteksta iz Yandex Object Storage..." -ForegroundColor Yellow

# Zdes dolzhna byt komanda zagruzki iz Object Storage
# Primer (trebuet nastroyki bucket-a i dostupa):
# yc storage bucket get --bucket <bucket-name> --key project_context.zip --file $tempArchive

Write-Host "ℹ️  Vremennaya komanda - ukazhite vash bucket:" -ForegroundColor Cyan
Write-Host 'yc storage bucket get --bucket <vash-bucket> --key project_context.zip --file "$tempArchive"' -ForegroundColor White
Write-Host ""

# Proverka nalichiya zagruzhennogo arkhiva
if (Test-Path $tempArchive) {
    Write-Host "✅ Arkhiv zagruzhen:" -ForegroundColor Green
    Write-Host $tempArchive -ForegroundColor White
    
    # Raskompakirovka arkhiva
    Write-Host "`nRaskompakirovka arkhiva..." -ForegroundColor Yellow
    
    # Sozdanie vremennoy papki dlya raskompakirovki
    $tempExtractPath = Join-Path $projectRoot "temp_extract"
    if (Test-Path $tempExtractPath) {
        Remove-Item $tempExtractPath -Recurse -Force
    }
    New-Item -ItemType Directory -Path $tempExtractPath | Out-Null
    
    # Raskompakirovka
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    [System.IO.Compression.ZipFile]::ExtractToDirectory($tempArchive, $tempExtractPath)
    
    Write-Host "✅ Raskompakirovka zavershena" -ForegroundColor Green
    
    # Kopirovanie faylov v proekt
    Write-Host "Kopirovanie faylov v proekt..." -ForegroundColor Yellow
    
    # Rekursovaya kopirovanie faylov
    Get-ChildItem -Path $tempExtractPath -Recurse | ForEach-Object {
        $relativePath = $_.FullName.Replace($tempExtractPath, "").TrimStart("\")
        $destinationPath = Join-Path $projectRoot $relativePath
        
        if ($_.PSIsContainer) {
            # Sozdanie papki
            if (-not (Test-Path $destinationPath)) {
                New-Item -ItemType Directory -Path $destinationPath -Force | Out-Null
            }
        } else {
            # Kopirovanie fayla
            Copy-Item -Path $_.FullName -Destination $destinationPath -Force
            Write-Host "  → $relativePath" -ForegroundColor Green
        }
    }
    
    # Udalenie vremennykh faylov
    Remove-Item $tempArchive -Force
    Remove-Item $tempExtractPath -Recurse -Force
    
    Write-Host "`n✅ Kontekst zagruzhen i primenen!" -ForegroundColor Green
    Write-Host "Proverьте obnovlennye fayly v papke docs/" -ForegroundColor Gray
} else {
    Write-Host "⚠️  Arkhiv ne zagruzhen" -ForegroundColor Yellow
    Write-Host "Vypolnite zagruzku vrukuy cherez Yandex Cloud Console" -ForegroundColor Gray
}

Write-Host "`n✅ Zagruzka iz oblaka zavershena!" -ForegroundColor Green
pause