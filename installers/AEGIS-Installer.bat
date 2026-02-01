@echo off
setlocal

set "ROOT=%~dp0.."
set "VENV=%ROOT%\.venv"

if not exist "%VENV%" (
  py -m venv "%VENV%"
)

call "%VENV%\Scripts\activate.bat"
python -m pip install --upgrade pip
python -m pip install "%ROOT%"

echo.
echo Запуск AEGIS...
python -m aegis.cli --message "Привет, AEGIS!"
pause
