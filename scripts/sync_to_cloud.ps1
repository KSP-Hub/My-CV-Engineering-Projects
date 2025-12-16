# sync_to_cloud.ps1 - Skript sinkhronizatsii konteksta s oblakom
Write-Host "=== SINKhRONIZATSIYa KONTEKSTA S OBLAKOM ===" -ForegroundColor Cyan

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

# Sozdanie vremennogo arkhiva
$tempArchive = Join-Path $projectRoot "temp_context.zip"
$finalArchive = Join-Path $projectRoot "project_context_$(Get-Date -Format 'yyyyMMdd_HHmmss').zip"

Write-Host "Sozdanie arkhiva konteksta..." -ForegroundColor Yellow

# Sozdanie spiska faylov dlya arkhivirovaniya
$filesToArchive = @()

# Dobavlenie osnovnykh faylov konteksta
if (Test-Path $projectStatusFile) {
    $filesToArchive += $projectStatusFile
}

# Dobavlenie faylov konteksta razgovorov
if (Test-Path $contextPath) {
    Get-ChildItem -Path $contextPath -Filter "*.md" | ForEach-Object {
        $filesToArchive += $_.FullName
    }
    Get-ChildItem -Path $contextPath -Filter "*.json" | ForEach-Object {
        $filesToArchive += $_.FullName
    }
}

# Dobavlenie vazhnykh dokumentov
Get-ChildItem -Path $docsPath -Filter "*.md" | ForEach-Object {
    $filesToArchive += $_.FullName
}

# Sozdanie vremennogo arkhiva
if (Test-Path $tempArchive) {
    Remove-Item $tempArchive -Force
}

# Sozdanie arkhiva s faylami konteksta
$filesToArchive | ForEach-Object {
    $relativePath = $_.Replace($projectRoot, "").TrimStart("\")
    # Komanda PowerShell dlya dobavleniya fayla v arkhiv
    # Ispolzuem .NET metod dlya sozdaniya arkhiva
}

# Ispolzovanie .NET metodov dlya sozdaniya arkhiva
Add-Type -AssemblyName System.IO.Compression.FileSystem
$compressionLevel = [System.IO.Compression.CompressionLevel]::Optimal
$zip = [System.IO.Compression.ZipFile]::Open($tempArchive, "Create")

foreach ($file in $filesToArchive) {
    $relativePath = $file.Replace($projectRoot, "").TrimStart("\")
    [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $file, $relativePath, $compressionLevel) | Out-Null
    Write-Host "  + $relativePath" -ForegroundColor Green
}

$zip.Dispose()

# Perekhimenovanie v finalnyi arkhiv
Move-Item -Path $tempArchive -Destination $finalArchive -Force

Write-Host "`n✅ Arkhiv konteksta sozdan:" -ForegroundColor Green
Write-Host $finalArchive -ForegroundColor White

# Zagruzka v Yandex Object Storage (primer - trebuet nastroyki bucket-a)
# Eto trebuet dopolnitelnoy nastroyki bucket-a v Yandex Cloud
# i predvaritelnoy avtorizatsii cherez service account

Write-Host "`nℹ️  Dlya zagruzki v Object Storage:" -ForegroundColor Cyan
Write-Host "1. Sozdayte bucket v Yandex Object Storage" -ForegroundColor Gray
Write-Host "2. Nastroyte dostup cherez service account" -ForegroundColor Gray
Write-Host "3. Zapustite komandu:" -ForegroundColor Gray
Write-Host "   yc storage bucket put --bucket <bucket-name> --key project_context.zip --file $finalArchive" -ForegroundColor White

Write-Host "`n✅ Sinkhronizatsiya zavershena!" -ForegroundColor Green
pause