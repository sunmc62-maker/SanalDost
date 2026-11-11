@echo off
chcp 65001 >nul
rem Sanal Dost'u tek bir .exe dosyasina cevirir (sanal_dost.py, dost klasoru ve sanal_dost.ico ayni klasorde olmali)
pip install pyinstaller pystray Pillow psutil
pyinstaller --noconsole --onefile --icon sanal_dost.ico --add-data "sanal_dost.ico;." --paths . --name SanalDost sanal_dost.py
echo.
echo Bitti! Dosya: dist\SanalDost.exe
pause
