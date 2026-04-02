# 🚀 Hybrid Test Automation Framework (Selenium + PyTest + POM)

## 📌 Overview

This project is a **Hybrid Test Automation Framework** built using:

* Selenium WebDriver
* PyTest
* Page Object Model (POM)
* Data-Driven Testing (JSON)
* Parallel Execution (pytest-xdist)
* HTML Reporting
* Docker Support
* CI/CD Integration (GitHub Actions)

It automates the **OrangeHRM Login functionality** with both valid and invalid test scenarios.

---

## 🏗️ Framework Architecture

Hybrid framework combining:

* ✅ Page Object Model (for maintainability)
* ✅ PyTest (for execution & assertions)
* ✅ Data-driven approach (JSON)
* ✅ Utility-based reusable components

---

## 📁 Project Structure

```
HybridFramework/
│
├── tests/                 # Test cases
├── pages/                 # Page Object classes
├── locators/              # UI locators
├── utilities/             # Reusable utilities
├── config/                # Config files
├── testdata/              # Test data (JSON)
├── reports/               # HTML reports
├── logs/                  # Execution logs
│
├── conftest.py            # Fixtures
├── pytest.ini             # PyTest config
├── requirements.txt       # Dependencies
└── .github/workflows/     # CI/CD pipeline
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone <your-repo-url>
cd HybridFramework
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   (Windows)
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run Tests

### Run All Tests

```
pytest
```

### Run Specific Test

```
pytest tests/test_login.py
```

### Run in Parallel

```
pytest -n 4
```

---

## 📊 Reports

Generate HTML report:

```
pytest --html=reports/report.html
```

📌 Report will be available in:

```
/reports/report.html
```

---

## 🧪 Test Scenarios Covered

### ✅ Valid Login

* Login with correct credentials
* Verify successful navigation to dashboard

### ❌ Invalid Login

* Wrong username
* Wrong password
* Both incorrect
* Validate error message

---

## 📂 Test Data (JSON Example)

```
{
  "valid": {
    "username": "Admin",
    "password": "admin123"
  },
  "invalid": [
    {"username": "wrongUser", "password": "admin123"},
    {"username": "Admin", "password": "wrongPass"},
    {"username": "wrongUser", "password": "wrongPass"}
  ]
}
```

---

## 🧰 Key Features

* ✔️ Modular framework design
* ✔️ Reusable components
* ✔️ Explicit waits (stable execution)
* ✔️ Data-driven testing
* ✔️ Parallel execution support
* ✔️ Logging support
* ✔️ Docker execution
* ✔️ CI/CD pipeline integration

---

## 🐳 Run with Docker

### Build & Run

```
docker-compose up --build
```

---

## 🔁 CI/CD (GitHub Actions)

Pipeline triggers on:

* Push to main branch

Steps:

* Install dependencies
* Run tests
* Generate reports

---

## 🧠 Best Practices Used

* Separation of concerns (POM)
* No hardcoded test data
* Explicit waits over implicit waits
* Scalable folder structure
* Maintainable locator strategy

---

## 🚀 Future Enhancements

* Allure Reporting
* Screenshot on failure
* Retry mechanism for flaky tests
* Selenium Grid integration
* API + UI hybrid testing
* Jenkins pipeline

---

## 👨‍💻 Author

**Mahesh P**

---

## ⭐ Contribution

Feel free to fork this repo and enhance the framework!

---

## 📜 License

This project is for learning and demonstration purposes.
