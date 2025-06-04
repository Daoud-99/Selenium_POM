from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import time
from SampleProjects.POMProjectDemo.Pages.loginPage import LoginPage
from SampleProjects.POMProjectDemo.Pages.homePage import HomePage
import HtmlTestRunner




#Scénario de login  
class LoginTest (unittest.TestCase) :

#ouverture de la navigateur    
    @classmethod
    def setUpClass(cls) :
        cls.service = Service("C:/Users/GUEST/Desktop/Selenium_POM/drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

#ouverture la page de login 
    def perform_login(self, username, password):
        """Méthode utilitaire pour exécuter une tentative de login."""
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()

#cas de test 1 (valid)
    def test_login_valid(self) :

        self.perform_login("Admin", "admin123" )      
        
        homePage = HomePage(self.driver)

        homePage.click_account()
        homePage.click_logout()
        print("cas de test 1 succeeded")

#Cas de test 2 (invalid)
    def test_login_invalid(self) :
        
        self.perform_login("AdminNN", "admiN342")
        #Vérification que la login avec UN et MP invalides est échoué 

        error_message_element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.oxd-alert-content-text") #récuperer l'élement après la login

        error_message = error_message_element.text #attention avec assert .text permet d'extraire le text qui contient dans l'élément 

        self.assertEqual(error_message, "Invalid credentials")



#fermeture de la navigateur  
    @classmethod
    def tearDownClass(cls):
        
        cls.driver.close()
        cls.driver.quit()
        print("test completed")    

# main pour unittest
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/GUEST/Desktop/Selenium_POM/reports"))









