# cloud_context_manager.ps1 - Meneger konteksta dlya raboty s oblakom
param(
    [Parameter(Mandatory=$false)]
    [ValidateSet("sync", "download", "status")]
    [string]$Action = "status",
    
    [Parameter(Mandatory=$false)]
    [string]$BucketName = ""
)

Write-Host "=== MENEDZHER KONTEKSTA OBLAKA ===" -ForegroundColor Cyan

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

function Show-Status {
    Write-Host "`n[STATUS] Tekushii status konteksta:" -ForegroundColor Cyan
    
    # Proverka lokalnykh faylov konteksta
    if (Test-Path $contextPath) {
        $localFiles = Get-ChildItem -Path $contextPath -Filter "*.md" | Measure-Object | Select-Object -ExpandProperty Count
        Write-Host "  Lokalnye fayly konteksta (MD): $localFiles" -ForegroundColor Green
    } else {
        Write-Host "  Lokalnye fayly konteksta: 0" -ForegroundColor Yellow
    }
    
    # Proverka fayla statusa proekta
    if (Test-Path $projectStatusFile) {
        Write-Host "  Fayl statusa proekta: est" -ForegroundColor Green
    } else {
        Write-Host "  Fayl statusa proekta: otsutstvuet" -ForegroundColor Red
    }
    
    # Proverka dostupa k Yandex Cloud
    try {
        $buckets = yc storage bucket list --format json 2>$null | ConvertFrom-Json
        Write-Host "  Dostup k Yandex Object Storage: est" -ForegroundColor Green
        Write-Host "  Dostupnye buckets: $($buckets.Count)" -ForegroundColor Gray
    } catch {
        Write-Host "  Dostup k Yandex Object Storage: oshibka" -ForegroundColor Red
    }
}

function Sync-ToCloud {
    Write-Host "`n[SYNC] Sinkhronizatsiya konteksta s oblakom..." -ForegroundColor Cyan
    
    # Zapusk skripta sinkhronizatsii
    $syncScript = Join-Path $projectRoot "scripts" "sync_to_cloud.ps1"
    if (Test-Path $syncScript) {
        & $syncScript
    } else {
        Write-Host "❌ Skript sinkhronizatsii ne naiden!" -ForegroundColor Red
        Write-Host "Sozdayte skript: $syncScript" -ForegroundColor Yellow
    }
}

function Download-FromCloud {
    Write-Host "`n[DOWNLOAD] Zagruzka konteksta iz oblaka..." -ForegroundColor Cyan
    
    # Zapusk skripta zagruzki
    $downloadScript = Join-Path $projectRoot "scripts" "sync_from_cloud.ps1"
    if (Test-Path $downloadScript) {
        & $downloadScript
    } else {
        Write-Host "❌ Skript zagruzki ne naiden!" -ForegroundColor Red
        Write-Host "Sozdayte skript: $downloadScript" -ForegroundColor Yellow
    }
}

# Vypolnenie deystviya
switch ($Action) {
    "status" {
        Show-Status
    }
    "sync" {
        Sync-ToCloud
    }
    "download" {
        Download-FromCloud
    }
}

Write-Host "`n✅ Rabota zavershena!" -ForegroundColor Green