@echo off
setlocal

rem Configure ENV
set AC_DIRT=%~dp0
set VIRTUAL_ENV=venv

rem Activate python venv
call "%VIRTUAL_ENV%\Scripts\activate.bat"

rem Execute python script
python win.py

rem Deactivate python venv
deactivate

endlocal
taskkill /F /IM AutoConnect_win.bat