AI Mood Tracker
================

A small Flask app that detects mood from free text and suggests supportive actions or games. This repo includes simple user authentication and persistence (SQLite).

Prerequisites
-------------
- Python 3.10+ (3.11 recommended)
- Git (optional)

Quick setup (Windows PowerShell)
-------------------------------
Open PowerShell in the project folder and run:

```powershell
# 1) Create virtual environment (if you don't have one)
python -m venv .venv

# 2) Activate it
.\.venv\Scripts\Activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Start the app
python main.py
```

The app will start at http://127.0.0.1:5000/ (debug mode).

Notes
-----
- The app creates an `app.db` SQLite database in the project folder automatically on first run.
- To secure sessions in production, set an environment variable `FLASK_SECRET_KEY` before starting the app:

```powershell
$env:FLASK_SECRET_KEY = "a-strong-random-secret"
python main.py
```

Testing endpoints
-----------------
You can test the mood API from the terminal (with the server running):

```powershell
curl -i -X POST http://127.0.0.1:5000/api/mood -H "Content-Type: application/json" -d '{"mood":"bored"}'
```

Or in-browser:
- Open http://127.0.0.1:5000/
- Register a new user or sign in
- Enter a mood (e.g., "bored", "happy", "anxious") and click "Get Support"
- Use the History link to view saved mood entries

Troubleshooting
---------------
- If `flask` import errors appear in the editor, ensure VS Code or your editor is using the virtual environment: select the interpreter at `.venv\Scripts\python.exe`.
- If popups are blocked by the browser, the UI will navigate to the game route in the same tab automatically.
- Check the terminal running `python main.py` for tracebacks.

Next improvements
-----------------
- Add migrations (Flask-Migrate) and switch to SQLAlchemy for richer DB usage.
- Add client-side validation and nicer UI animations.
- Add unit tests and CI pipeline.

License
-------
MIT (your choice)