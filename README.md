# Selenium QA Automation Project

A beginner-friendly web automation testing project built using Python, Selenium WebDriver, Pytest, and Microsoft Edge.

## Project Overview

This project automates login functionality testing on a demo website to verify how the application handles valid and invalid login attempts.

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Microsoft Edge
- Visual Studio Code

## Test Scenarios

| Test ID | Scenario | Expected Result |
|---|---|---|
| TC01 | Valid login credentials | Login successful |
| TC02 | Invalid password | Error message displayed |
| TC03 | Empty username | Login rejected |
| TC04 | Empty password | Login rejected |

## Test Results

- Total test cases: 4
- Passed: 4
- Failed: 0

## Project Structure

```text
selenium-qa-automation/
├── login_test.py
├── negative_login_test.py
├── empty_username_test.py
├── empty_password_test.py
├── test_login.py
├── test_cases.md
├── bug_report.md
└── README.md
```

## How to Run

Install Selenium and Pytest:

```bash
python -m pip install selenium pytest
```

Run the automated test suite:

```bash
python -m pytest -v test_login.py
```

## Practice Website

https://the-internet.herokuapp.com/login

## Learning Objectives

- Understanding web application testing.
- Automating browser interactions using Selenium.
- Testing positive and negative login scenarios.
- Using Pytest to execute automated tests.
- Documenting test cases and bugs.

## Author

Muhammad Talha

Software Engineering Student | Aspiring QA Engineer
