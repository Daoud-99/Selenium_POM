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

git clone https://github.com/your-username/Selenium_POM.git
cd Selenium_POM

### 2. Install Dependencies

Install selenium and HtmlTestRunner if not already installed:
pip install selenium
pip install html-testRunner

### 3. Run the Tests

From the project root directory:

python -m SampleProjects.POMProjectDemo.Tests.login

⚠️ Make sure the path to chromedriver.exe is correctly set in your code.

---
## 📊 Test Reports

HTML test reports are generated in: SampleProjects/POMProjectDemo/reports/
Open the .html files in your browser to view the test results.
![Capture d'écran 2025-06-04 153600](https://github.com/user-attachments/assets/36fe7bde-76a9-4573-aabd-cb1e03cab3e0)

---
## 🔧 Configuration
### WebDriver Path

The login.py file uses the following path (you can adjust as needed): 
cls.service = Service("C:/Users/GUEST/Desktop/Selenium_POM/drivers/chromedriver.exe")

Make sure this path is correct or place chromedriver.exe in a directory that is added to your system PATH.

---
## 🙌 Author
Project created by Daoud Boukhelouf
📧 Contact: boukheloufdaoud00@gmail.com

















