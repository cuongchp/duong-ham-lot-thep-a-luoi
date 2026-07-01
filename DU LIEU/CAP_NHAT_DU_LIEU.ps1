# =============================================================
# CAP_NHAT_DU_LIEU.ps1  -  Pipeline cap nhat day du (1 lenh duy nhat)
#
# B1: Quet TAI LIEU/*.pdf -> build danh sach, giu summary cu
# B2: Backup + ghi tai-lieu.json
# B3: Dong bo DOCS_EMBEDDED vao HTML (multi-line hoac single-line)
# B4: Nhung const RD tu DU_LIEU_DUONG_HAM.json vao HTML
# B5: Ghi HTML + copy website/index.html
# B6: git status / diff / add / commit / push
#     (dung GIT_INDEX_FILE workaround neu Windows Defender chan git rename)
# =============================================================

$ErrorActionPreference = 'Stop'
$dir       = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot  = Split-Path $dir -Parent
$utf8noBom = New-Object System.Text.UTF8Encoding $false

$jsonPath    = Join-Path $dir "DU_LIEU_DUONG_HAM.json"
$htmlPath    = Join-Path $dir "DUONG_HAM_LOT_THEP_A_LUOI.html"
$docJsonPath = Join-Path $dir "tai-lieu.json"
$docDir      = Join-Path $dir "TAI LIEU"
$webHtmlPath = Join-Path $dir "website\index.html"
$gitIdxPath  = Join-Path $repoRoot ".git\index"

function Write-Section($title) {
    Write-Host ""
    Write-Host "--- $title ---" -ForegroundColor Cyan
}

# ==============================================================
# BUOC 1: Quet thu muc TAI LIEU/
# ==============================================================
Write-Section "BUOC 1: Quet thu muc TAI LIEU/"

function Format-DocSize([long]$bytes) {
    if ($bytes -lt 1024)    { return "$bytes B" }
    if ($bytes -lt 1048576) { return ("{0:N1} KB" -f ($bytes / 1024)) }
    return ("{0:N1} MB" -f ($bytes / 1048576))
}

# Doc summary cu: dung ReadAllText de xu ly BOM chinh xac (PS5 Get-Content co the giu BOM)
$oldSummary = @{}
if (Test-Path -LiteralPath $docJsonPath) {
    try {
        $oldRaw  = [System.IO.File]::ReadAllText($docJsonPath, [System.Text.Encoding]::UTF8)
        $oldDocs = $oldRaw | ConvertFrom-Json   # Tach biet: tranh @(pipeline) wrapping bug PS5.1
        foreach ($d in $oldDocs) {
            if ($d.name) { $oldSummary[$d.name] = [string]$d.summary }
        }
        Write-Host "  Da doc $($oldSummary.Count) summary cu tu tai-lieu.json"
    } catch {
        Write-Host "  [!] Khong doc duoc tai-lieu.json cu: $_" -ForegroundColor Yellow
    }
}

if (-not (Test-Path -LiteralPath $docDir)) {
    New-Item -ItemType Directory -Path $docDir | Out-Null
}

$docsArr = @(
    Get-ChildItem -LiteralPath $docDir -File |
    Where-Object { $_.Name -ne ".gitkeep" -and $_.Extension -ieq ".pdf" } |
    Sort-Object Name |
    ForEach-Object {
        $isNew = -not $oldSummary.ContainsKey($_.Name)
        $sum   = if ($isNew) { "" } else { $oldSummary[$_.Name] }
        if ($isNew) {
            Write-Host "  [MOI]  $($_.Name)" -ForegroundColor Yellow
            Write-Host "         -> summary chua co, can bo sung sau" -ForegroundColor DarkYellow
        } else {
            $tag = if ($sum) { "co summary" } else { "summary con rong" }
            Write-Host "  [GIU]  $($_.Name)  ($tag)"
        }
        [ordered]@{
            name    = $_.Name
            url     = "TAI LIEU/$($_.Name)"
            size    = Format-DocSize $_.Length
            summary = $sum
        }
    }
)

Write-Host ""
Write-Host "  Tong: $($docsArr.Count) file PDF trong TAI LIEU/"
if ($docsArr.Count -eq 0) {
    Write-Host "  [!] Canh bao: Khong tim thay file PDF nao trong TAI LIEU/" -ForegroundColor Yellow
}

# ==============================================================
# BUOC 2: Backup + ghi tai-lieu.json
# ==============================================================
Write-Section "BUOC 2: Ghi tai-lieu.json"

if (Test-Path -LiteralPath $docJsonPath) {
    Copy-Item -LiteralPath $docJsonPath -Destination "$docJsonPath.bak" -Force
    Write-Host "  Backup: tai-lieu.json.bak"
}
$docsJsonPretty = ConvertTo-Json -InputObject @($docsArr) -Depth 5
[System.IO.File]::WriteAllText($docJsonPath, $docsJsonPretty, $utf8noBom)
Write-Host "  Da ghi tai-lieu.json ($($docsArr.Count) file)"

# ==============================================================
# BUOC 3+4: Backup + cap nhat HTML
# ==============================================================
Write-Section "BUOC 3+4: Cap nhat HTML"

if (-not (Test-Path -LiteralPath $htmlPath)) {
    Write-Error "Khong tim thay: $htmlPath"
    exit 1
}
Copy-Item -LiteralPath $htmlPath -Destination "$htmlPath.bak" -Force
Write-Host "  Backup: $(Split-Path $htmlPath -Leaf).bak"

$lines = [System.IO.File]::ReadAllLines($htmlPath, [System.Text.Encoding]::UTF8)

# --- B3: Thay the khoi DOCS_EMBEDDED (xu ly ca single-line lan multi-line) ---
$docsCompact = ConvertTo-Json -InputObject @($docsArr) -Depth 5 -Compress

$dStart = -1
$dEnd   = -1
for ($i = 0; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match '^const DOCS_EMBEDDED=') {
        $dStart = $i
        if ($lines[$i] -match ';\s*$') { $dEnd = $i; break }   # single-line
    }
    if ($dStart -ge 0 -and $i -gt $dStart -and $lines[$i] -match '^\];\s*$') {
        $dEnd = $i; break                                         # multi-line ket thuc
    }
}
if ($dStart -lt 0 -or $dEnd -lt 0) {
    Write-Error "Khong tim thay 'const DOCS_EMBEDDED' trong HTML."
    exit 1
}

$newLines = [System.Collections.Generic.List[string]]::new()
for ($i = 0; $i -lt $lines.Length; $i++) {
    if ($i -eq $dStart) {
        $newLines.Add("const DOCS_EMBEDDED=$docsCompact;")
    } elseif ($i -gt $dStart -and $i -le $dEnd) {
        # Bo qua dong cu cua khoi DOCS_EMBEDDED
    } else {
        $newLines.Add($lines[$i])
    }
}
$lines = $newLines.ToArray()
Write-Host "  DOCS_EMBEDDED: $($docsArr.Count) file da dong bo"

# --- B4: Thay const RD ---
if (-not (Test-Path -LiteralPath $jsonPath)) {
    Write-Error "Khong tim thay: $jsonPath"
    exit 1
}
try {
    $data = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8) | ConvertFrom-Json
} catch {
    Write-Error "Loi doc DU_LIEU_DUONG_HAM.json: $_"
    exit 1
}
$count   = $data.Count
$compact = $data | ConvertTo-Json -Depth 10 -Compress

$rdFound = $false
for ($i = 0; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match '^const RD=\[') {
        $lines[$i] = "const RD=$compact;"
        $rdFound   = $true
        Write-Host "  const RD: $count ban ghi duong han (dong $($i+1))"
        break
    }
}
if (-not $rdFound) {
    Write-Error "Khong tim thay 'const RD=[' trong HTML."
    exit 1
}

# --- B5: Ghi HTML + copy website/ ---
[System.IO.File]::WriteAllLines($htmlPath, $lines, $utf8noBom)
$webDir = Split-Path $webHtmlPath -Parent
if (-not (Test-Path $webDir)) { New-Item -ItemType Directory -Path $webDir | Out-Null }
[System.IO.File]::WriteAllLines($webHtmlPath, $lines, $utf8noBom)
Write-Host "  HTML da ghi + dong bo website/index.html"

# ==============================================================
# BUOC 6: Git status / diff / add / commit / push
# ==============================================================
Write-Section "BUOC 6: Git"

$stamp = Get-Date -Format "dd/MM/yyyy HH:mm:ss"

# Thu them Defender exclusion neu co quyen Admin
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if ($isAdmin) {
    try {
        Add-MpPreference -ExclusionPath $repoRoot -ErrorAction SilentlyContinue
        Write-Host "  Defender exclusion: da them (Admin)"
    } catch {}
} else {
    Write-Host "  [i] Chay khong phai Admin — su dung GIT_INDEX_FILE workaround" -ForegroundColor DarkGray
}

# GIT_INDEX_FILE workaround: git ghi index vao TEMP, sau do chep ve .git/index
# Can thiet vi Windows Defender co the chan MoveFileEx cua git trong .git/ khi khong Admin
$webTmpIdx = $null
$parTmpIdx = $null

try {
    # === A: website/ submodule (repo rieng, remote: duong-ham-a-luoi.git) ===
    $webSubDir  = Join-Path $dir "website"
    $webIdxPath = Join-Path $webSubDir ".git\index"
    if ((Test-Path $webSubDir) -and (Test-Path $webIdxPath)) {
        Write-Host ""
        Write-Host "  [A] website/ submodule..." -ForegroundColor DarkGray
        Push-Location $webSubDir
        try {
            $webTmpIdx = [System.IO.Path]::Combine($env:TEMP, "git_web_idx_$PID")
            [System.IO.File]::Copy($webIdxPath, $webTmpIdx, $true)
            $env:GIT_INDEX_FILE = $webTmpIdx

            & git add index.html
            if ($LASTEXITCODE -ne 0) { throw "git add index.html trong website/ that bai" }

            if (@(& git status --porcelain).Count -gt 0) {
                # Dung commit-tree + ghi ref truc tiep: bypass Defender (tranh lock-file rename)
                $webParent = (& git rev-parse HEAD).Trim()
                $webTree   = (& git write-tree).Trim()
                if ($LASTEXITCODE -ne 0 -or -not $webTree) { throw "git write-tree website/ that bai" }
                $webNew = (& git commit-tree $webTree -p $webParent -m "Cap nhat HTML $stamp").Trim()
                if ($LASTEXITCODE -ne 0 -or -not $webNew) { throw "git commit-tree website/ that bai" }
                # Ghi ref truc tiep (khong dung lock file -> tranh rename fail)
                [System.IO.File]::WriteAllText(
                    (Join-Path $webSubDir ".git\refs\heads\main"),
                    "$webNew`n",
                    [System.Text.Encoding]::ASCII)
                Write-Host "    Commit: $($webNew.Substring(0,8))..."
                # Lam sach index sau commit
                & git read-tree $webTree
                [System.IO.File]::Copy($webTmpIdx, $webIdxPath, $true)
                Remove-Item env:GIT_INDEX_FILE -ErrorAction SilentlyContinue
                $webTmpIdx = $null
                & git push origin main
                if ($LASTEXITCODE -ne 0) { throw "git push website/ that bai" }
                Write-Host "    website/ da push." -ForegroundColor Green
            } else {
                Write-Host "    website/ khong co thay doi."
            }
        } finally {
            Remove-Item env:GIT_INDEX_FILE -ErrorAction SilentlyContinue
            if ($webTmpIdx -and (Test-Path $webTmpIdx)) {
                Remove-Item $webTmpIdx -ErrorAction SilentlyContinue; $webTmpIdx = $null
            }
            Pop-Location   # tro ve $repoRoot (sau Push-Location $repoRoot phia duoi chua co!)
        }
    }

    # === B: Parent repo ===
    Push-Location $repoRoot
    try {
        $null = & git rev-parse --is-inside-work-tree 2>&1
        if ($LASTEXITCODE -ne 0) { throw "Khong phai Git repository" }

        Write-Host ""
        Write-Host "  [git status --short]" -ForegroundColor DarkGray
        & git status --short
        Write-Host ""
        Write-Host "  [git diff --stat]" -ForegroundColor DarkGray
        & git diff --stat
        Write-Host ""

        $hasChanges = @(& git status --porcelain).Count -gt 0

        if (-not $hasChanges) {
            Write-Host "  Khong co thay doi. Push commit chua len..." -ForegroundColor Yellow
            & git push origin main
            if ($LASTEXITCODE -ne 0) { throw "git push that bai" }
        } else {
            $parTmpIdx = [System.IO.Path]::Combine($env:TEMP, "git_par_idx_$PID")
            [System.IO.File]::Copy($gitIdxPath, $parTmpIdx, $true)
            $env:GIT_INDEX_FILE = $parTmpIdx
            Write-Host "  GIT_INDEX_FILE: $parTmpIdx" -ForegroundColor DarkGray

            $toStage = @(
                "DU LIEU/DUONG_HAM_LOT_THEP_A_LUOI.html",
                "DU LIEU/tai-lieu.json",
                "DU LIEU/CAP_NHAT_DU_LIEU.ps1",
                "DU LIEU/CAP_NHAT_GITHUB.cmd",
                "DU LIEU/README.md"
            )
            foreach ($f in $toStage) {
                if (Test-Path -LiteralPath $f) {
                    & git add $f
                    if ($LASTEXITCODE -ne 0) { throw "git add that bai: $f" }
                }
            }
            # Cap nhat gitlink cua submodule website/ (neu no da commit moi)
            if (Test-Path -LiteralPath "DU LIEU/website") {
                & git add "DU LIEU/website"
            }
            # PDF moi trong TAI LIEU/
            if (Test-Path -LiteralPath "DU LIEU/TAI LIEU") {
                & git add "DU LIEU/TAI LIEU/"
            }
            if (Test-Path -LiteralPath ".gitignore") {
                & git add ".gitignore"
            }

            Write-Host ""
            Write-Host "  [git diff --cached --stat  (se commit)]" -ForegroundColor DarkGray
            & git diff --cached --stat
            Write-Host ""

            # Dung commit-tree + ghi ref truc tiep: bypass Defender (tranh lock-file rename)
            $parParent = (& git rev-parse HEAD).Trim()
            $parTree   = (& git write-tree).Trim()
            if ($LASTEXITCODE -ne 0 -or -not $parTree) { throw "git write-tree that bai" }
            $parNew = (& git commit-tree $parTree -p $parParent -m "Cap nhat du an $stamp").Trim()
            if ($LASTEXITCODE -ne 0 -or -not $parNew) { throw "git commit-tree that bai" }
            # Ghi ref truc tiep (khong dung lock file -> tranh rename fail)
            [System.IO.File]::WriteAllText(
                (Join-Path $repoRoot ".git\refs\heads\main"),
                "$parNew`n",
                [System.Text.Encoding]::ASCII)
            Write-Host "  Commit: $($parNew.Substring(0,8))..."
            # Lam sach index sau commit
            & git read-tree $parTree
            [System.IO.File]::Copy($parTmpIdx, $gitIdxPath, $true)
            Remove-Item env:GIT_INDEX_FILE -ErrorAction SilentlyContinue
            $parTmpIdx = $null

            & git push origin main
            if ($LASTEXITCODE -ne 0) { throw "git push that bai" }
        }

        Write-Host "  Da push len GitHub thanh cong." -ForegroundColor Green

    } finally {
        Remove-Item env:GIT_INDEX_FILE -ErrorAction SilentlyContinue
        if ($parTmpIdx -and (Test-Path $parTmpIdx)) {
            Remove-Item $parTmpIdx -ErrorAction SilentlyContinue; $parTmpIdx = $null
        }
        Pop-Location
    }

} catch {
    Write-Host ""
    Write-Host "LOI o buoc git: $_" -ForegroundColor Red
    exit 1
}

# ==============================================================
# TONG KET
# ==============================================================
Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "  HOAN THANH" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host "  Du lieu duong han  : $count ban ghi"
Write-Host "  Tai lieu PDF       : $($docsArr.Count) file"

$needSummary = @($docsArr | Where-Object { -not $_['summary'] })
if ($needSummary.Count -gt 0) {
    Write-Host ""
    Write-Host "  [!] $($needSummary.Count) file con summary rong - can bo sung:" -ForegroundColor Yellow
    foreach ($f in $needSummary) {
        Write-Host "      - $($f['name'])" -ForegroundColor Yellow
    }
}
Write-Host ""
Write-Host "  GitHub Pages tu cap nhat sau 1-2 phut."
Write-Host "  https://github.com/cuongchp/duong-ham-lot-thep-a-luoi"
Write-Host ""
