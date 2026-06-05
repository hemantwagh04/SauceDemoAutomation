# SauceDemo Automation Framework

## Overview
This project automates the SauceDemo website using Selenium WebDriver, PyTest, and the Page Object Model (POM) design pattern.

## Technologies Used
- Python
- Selenium WebDriver
- PyTest
- PyTest HTML Reports
- Page Object Model (POM)

## Project Structure

SauceDemoAutomation/
├── pages/
├── tests/
├── reports/
├── README.md
└── requirements.txt

## Test Cases
- Valid Login
- Invalid Login
- Add To Cart
- Checkout
- Logout

## Execute Tests

```bash
python -m pytest tests -v
```

## Generate HTML Report

```bash
python -m pytest tests -v --html=reports/report.html --self-contained-html
```

## Result
All 5 automated test cases are passing successfully.
