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

:: ---- BUOC 1: Nhung du lieu JSON vao HTML ----
echo [1/3] Dang nap du lieu tu DU_LIEU_DUONG_HAM.json vao HTML...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0CAP_NHAT_DU_LIEU.ps1"
if errorlevel 1 (
  echo.
  echo Loi khi cap nhat du lieu. Kiem tra lai file DU_LIEU_DUONG_HAM.json.
  pause
  exit /b 1
)
echo.

:: ---- BUOC 2: Kiem tra git ----
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
  echo Dang kiem tra va day cac commit chua len GitHub...
  git push origin main
  if errorlevel 1 (
    echo Loi khi git push. Kiem tra dang nhap GitHub hoac ket noi mang.
    pause
    exit /b 1
  )
  echo Da dong bo len GitHub thanh cong.
  pause
  exit /b 0
)

echo Cac thay doi hien tai:
git status --short
echo.

:: ---- BUOC 3: Commit va push ----
echo [2/3] Dang commit...
git add DUONG_HAM_LOT_THEP_A_LUOI.html website/index.html CAP_NHAT_DU_LIEU.ps1 CAP_NHAT_GITHUB.cmd ../.gitignore
if errorlevel 1 (
  echo.
  echo ========================================================
  echo  LOI: Windows Defender dang chan thao tac git.
  echo  Cach sua: Click phai vao SUA_LOI_GIT_CHAY_1_LAN.bat
  echo            chon "Run as administrator", sau do chay lai.
  echo ========================================================
  pause
  exit /b 1
)

git commit -m "Cap nhat du an %date% %time%"
if errorlevel 1 (
  echo Loi khi git commit.
  pause
  exit /b 1
)

echo [3/3] Dang day len GitHub...
git push origin main
if errorlevel 1 (
  echo Loi khi git push. Kiem tra dang nhap GitHub hoac ket noi mang.
  pause
  exit /b 1
)

echo.
echo ==========================================
echo  HOAN THANH! Du an da duoc cap nhat.
echo  GitHub Pages tu cap nhat sau 1-2 phut.
echo  Xem tai: https://github.com/cuongchp/duong-ham-lot-thep-a-luoi
echo ==========================================
echo.
pause
