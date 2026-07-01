@echo off
setlocal

cd /d "%~dp0"

echo ==========================================
echo  CAP NHAT DU AN LEN GITHUB
echo  (xu ly toan bo qua CAP_NHAT_DU_LIEU.ps1)
echo ==========================================
echo.

:: Tu dong them ngoai le Defender neu co quyen Admin
net session >nul 2>&1
if not errorlevel 1 (
  powershell -NoProfile -ExecutionPolicy Bypass -Command "Add-MpPreference -ExclusionPath '%~dp0..' -ErrorAction SilentlyContinue" >nul 2>&1
)

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0CAP_NHAT_DU_LIEU.ps1"
if errorlevel 1 (
  echo.
  echo LOI: Qua trinh cap nhat that bai. Xem log o tren.
  echo Neu bi chan boi Windows Defender, chay SUA_LOI_GIT_CHAY_1_LAN.bat
  echo voi quyen Administrator, sau do thu lai.
  echo.
  pause
  exit /b 1
)

echo.
pause
