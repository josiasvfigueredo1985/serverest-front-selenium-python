# Automation with Selenium and Python

- Test orchestrator: Pytest
- Dependency installer: pip

# Test Design Pattern

- Page Object Model

# Bases folder

- Responsible to define the main bahavior and attributes from test and page components

## Install dependencies

Prerequisites: Python 3.13 and Google Chrome.

Create a virtual environment and install the dependencies from
`requirements.txt` (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the tests

Run the test suite with:

```powershell
pytest
```

Pytest is configured in `pytest.ini` to write the HTML report to
`reports/pytest_report`, the log to `reports/logs/pytest-logs.txt`, and Allure
results to `reports/allure-results`.

GitHub Actions runs the tests on Windows with Python 3.13 on pushes and pull
requests. The generated reports are available as the `test-reports` artifact.
On pushes to `main`, the HTML report is also published to GitHub Pages, including
when tests fail. Enable **Settings > Pages > Build and deployment > Source >
GitHub Actions** in the repository first. The run summary links to the latest
published report; it may be publicly accessible depending on repository settings.
