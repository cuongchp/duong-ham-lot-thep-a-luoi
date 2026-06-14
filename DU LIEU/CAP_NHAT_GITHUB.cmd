@echo off
setlocal

cd /d "%~dp0"

echo ==========================================
echo  CAP NHAT DU AN LEN GITHUB
echo  Repo: duong-ham-lot-thep-a-luoi
echo ==========================================
echo.

:: Tu dong them ngoai le Defender neu co quyen Admin
net session >nul 2>&1
if not errorlevel 1 (
  powershell -NoProfile -ExecutionPolicy Bypass -Command "Add-MpPreference -ExclusionPath '%~dp0..' -ErrorAction SilentlyContinue" >nul 2>&1
)

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
  echo Loi: Thu muc nay chua phai Git repository.
  pause
  exit /b 1
)

set HAS_CHANGES=
for /f "delims=" %%i in ('git status --porcelain') do (
  set HAS_CHANGES=1
)

if not defined HAS_CHANGES (
  echo Khong co thay doi nao de cap nhat.
  echo.
  echo Dang kiem tra va day cac commit chua len GitHub...
  git push origin main
  if errorlevel 1 (
    echo.
    echo Loi khi git push. Kiem tra dang nhap GitHub hoac ket noi mang.
    pause
    exit /b 1
  )
  echo.
  echo Da dong bo len GitHub thanh cong.
  pause
  exit /b 0
)

echo Cac thay doi hien tai:
git status --short
echo.

git add DUONG_HAM_LOT_THEP_A_LUOI.html
if errorlevel 1 (
  echo.
  echo ========================================================
  echo  LOI: Windows Defender dang chan thao tac git.
  echo  Cach sua: Click phai vao file SUA_LOI_GIT_CHAY_1_LAN.bat
  echo            chon "Run as administrator", sau do chay lai file nay.
  echo ========================================================
  pause
  exit /b 1
)

git commit -m "Cap nhat du an %date% %time%"
if errorlevel 1 (
  echo.
  echo Loi khi git commit.
  pause
  exit /b 1
)

git push origin main
if errorlevel 1 (
  echo.
  echo Loi khi git push. Kiem tra dang nhap GitHub hoac ket noi mang.
  pause
  exit /b 1
)

echo.
echo Da cap nhat len GitHub thanh cong.
echo GitHub Pages se tu cap nhat sau vai chuc giay den vai phut.
echo Xem tai: https://github.com/cuongchp/duong-ham-lot-thep-a-luoi
echo.
pause
