@echo off
setlocal

cd /d "%~dp0"

echo ==========================================
echo  CAP NHAT DU AN LEN GITHUB
echo ==========================================
echo.

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
  pause
  exit /b 0
)

echo Cac thay doi hien tai:
git status --short
echo.

git add .
if errorlevel 1 (
  echo.
  echo Loi khi git add.
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

git push
if errorlevel 1 (
  echo.
  echo Loi khi git push. Kiem tra dang nhap GitHub hoac ket noi mang.
  pause
  exit /b 1
)

echo.
echo Da cap nhat len GitHub thanh cong.
echo GitHub Pages se tu cap nhat sau vai chuc giay den vai phut.
echo.
pause
