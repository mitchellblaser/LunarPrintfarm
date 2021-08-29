%~dp0 & "\.lenv"

if exist %~dp0 & "\.lenv\" (
    .lenv\Scripts\activate.bat
) else (
    echo "Setting up Lunar Virtual Environment for the first time."
    python3 -m venv .lenv
    .lenv\Scripts\activate.bat
    pip install -r requirements.txt
)

echo "Starting Lunar."
set FLASK_APP=lunar.py
flask run