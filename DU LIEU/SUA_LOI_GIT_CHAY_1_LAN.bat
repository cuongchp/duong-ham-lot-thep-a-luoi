@echo off
:: Chay file nay voi quyen Administrator (click phai -> Run as administrator)
:: Chi can chay 1 lan duy nhat

echo ==========================================
echo  SUA LOI GIT - THEM NGOAI LE DEFENDER
echo  (Chi can chay 1 lan)
echo ==========================================
echo.

:: Kiem tra quyen Admin
net session >nul 2>&1
if errorlevel 1 (
    echo LOI: Can chay voi quyen Administrator!
    echo.
    echo Huong dan: Click phai vao file nay, chon "Run as administrator"
    pause
    exit /b 1
)

echo Dang them ngoai le Windows Defender...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Add-MpPreference -ExclusionPath 'D:\1. WOKRS\1. THUY DIEN A LƯƠI\2- NHA MAY A LUOI\NAM 2026\3. P4\11. THEO DOI MANG XONG-OP DUONG HAM'"

if errorlevel 1 (
    echo.
    echo That bai. Thu cach thu cong:
    echo 1. Mo Windows Security
    echo 2. Virus and threat protection
    echo 3. Manage settings
    echo 4. Add or remove exclusions
    echo 5. Them thu muc: D:\1. WOKRS\...
    pause
    exit /b 1
)

echo.
echo THANH CONG! Windows Defender se khong can thiep vao thu muc du an nua.
echo Bay gio ban co the chay CAP_NHAT_GITHUB.cmd binh thuong.
echo.
pause
