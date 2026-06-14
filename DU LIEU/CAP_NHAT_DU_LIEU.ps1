# =============================================================
# CAP_NHAT_DU_LIEU.ps1
# Nhung du lieu tu DU_LIEU_DUONG_HAM.json vao DUONG_HAM_LOT_THEP_A_LUOI.html
# Nguon du lieu duy nhat: DU_LIEU_DUONG_HAM.json
# =============================================================

$ErrorActionPreference = 'Stop'
$dir = Split-Path -Parent $MyInvocation.MyCommand.Path

$jsonPath = Join-Path $dir "DU_LIEU_DUONG_HAM.json"
$htmlPath = Join-Path $dir "DUONG_HAM_LOT_THEP_A_LUOI.html"

# --- Kiem tra file ---
if (-not (Test-Path $jsonPath)) {
    Write-Error "Khong tim thay file: $jsonPath"
    exit 1
}
if (-not (Test-Path $htmlPath)) {
    Write-Error "Khong tim thay file: $htmlPath"
    exit 1
}

# --- Doc JSON va kiem tra hop le ---
try {
    $jsonRaw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
    $data    = $jsonRaw | ConvertFrom-Json
} catch {
    Write-Error "Loi doc file JSON: $_"
    exit 1
}

$count   = $data.Count
$compact = $data | ConvertTo-Json -Depth 10 -Compress

# --- Tim va thay the dong 'const RD=[...]' trong HTML ---
$lines = [System.IO.File]::ReadAllLines($htmlPath, [System.Text.Encoding]::UTF8)
$found = $false

for ($i = 0; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match '^const RD=\[') {
        $lines[$i] = "const RD=$compact;"
        $found = $true
        Write-Host "  Dong $($i+1): const RD da duoc thay the ($count ban ghi)."
        break
    }
}

if (-not $found) {
    Write-Error "Khong tim thay 'const RD=[' trong HTML. Kiem tra lai file HTML."
    exit 1
}

# --- Luu HTML (UTF-8 khong BOM) ---
$utf8noBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllLines($htmlPath, $lines, $utf8noBom)

# --- Dong bo website/index.html = copy toan bo file chinh (1 nguon duy nhat) ---
$webHtmlPath = Join-Path $dir "website\index.html"
$webDir = Split-Path $webHtmlPath -Parent
if (-not (Test-Path $webDir)) { New-Item -ItemType Directory -Path $webDir | Out-Null }
[System.IO.File]::WriteAllLines($webHtmlPath, $lines, $utf8noBom)
Write-Host "  website/index.html: da dong bo tu file chinh."

Write-Host ""
Write-Host "HOAN THANH: Da nhung $count ban ghi va dong bo website/index.html." -ForegroundColor Green
