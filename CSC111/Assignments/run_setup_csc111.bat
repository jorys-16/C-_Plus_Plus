@echo off
setlocal

cd /d "%~dp0"
python setup_csc111.py --apply

if errorlevel 1 (
    echo.
    echo The CSC111 setup did not complete successfully.
    pause
    exit /b 1
)

echo.
echo CSC111 setup completed successfully.
pause
