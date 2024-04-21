@echo off

REM Get the current directory of the batch file
set "script_dir=%~dp0"

REM Check if two command-line arguments are provided
if "%~2"=="" (
    echo Usage: %0 ^<name^> ^<input_file^>
    exit /b 1
)

REM Run CreateInputFile.py with name and inputfile
python "%script_dir%CreateInputFile.py" %1 %2

REM Change directory to the newly created folder
cd %1

REM Run multiscrape on input.txt
python "%script_dir%multiscrape.py" input.txt

REM Move back to the original directory
cd ..

REM Pause the script to keep the terminal window open
pause
