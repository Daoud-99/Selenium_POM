# Selenium_POM

Automated web application testing project using **Selenium** and the **Page Object Model (POM)** design pattern.

## 📌 Objective

This project automates the **login scenario** on the OrangeHRM demo site:  
🔗 [https://opensource-demo.orangehrmlive.com/](https://opensource-demo.orangehrmlive.com/)

---

## 🧰 Technologies Used

- 🐍 Python 3.x
- 🌐 Selenium WebDriver
- 🧪 unittest (Python's built-in test framework)
- 📄 HtmlTestRunner (for generating HTML test reports)
- 🧱 Page Object Model (POM) architecture

---

## 🗂️ Project Structure

Selenium_POM/
├── SampleProjects/
│ └── POMProjectDemo/
│ ├── Pages/
│ │ ├── loginPage.py
│ │ └── homePage.py
│ ├── Tests/
│ │ └── login.py
│ └── reports/
├── drivers/
│ └── chromedriver.exe
└── README.md


---

## ✅ Test Cases Covered

- Login with valid credentials ✅
- Login with invalid credentials ❌
- Error message verification on login failure

---

## 🚀 How to Run the Tests

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Selenium_POM.git
cd Selenium_POM

Test Reports
HTML test reports are generated in:

bash
Copier
Modifier
SampleProjects/POMProjectDemo/reports/
Open the .html files in your browser to view the test results.
