$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$docDir = Join-Path $root "DU LIEU\TAI LIEU"
$outFile = Join-Path $root "DU LIEU\tai-lieu.json"

if (-not (Test-Path -LiteralPath $docDir)) {
  New-Item -ItemType Directory -Path $docDir | Out-Null
}

function Format-DocSize([long]$bytes) {
  if ($bytes -lt 1024) { return "$bytes B" }
  if ($bytes -lt 1048576) { return ("{0:N1} KB" -f ($bytes / 1024)) }
  return ("{0:N1} MB" -f ($bytes / 1048576))
}

$docs = Get-ChildItem -LiteralPath $docDir -File |
  Where-Object { $_.Name -ne ".gitkeep" } |
  Sort-Object Name |
  ForEach-Object {
    [ordered]@{
      name = $_.Name
      url = "TAI LIEU/$($_.Name)"
      size = Format-DocSize $_.Length
    }
  }

$json = ConvertTo-Json -InputObject @($docs) -Depth 5
if ($null -eq $json) { $json = "[]" }

Set-Content -LiteralPath $outFile -Value $json -Encoding UTF8
Write-Host "Da tao danh muc tai lieu: $outFile"
