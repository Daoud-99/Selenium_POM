from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):

        self.driver = driver

        self.account_class = ".oxd-icon.bi-caret-down-fill.oxd-userdropdown-icon"

        self.logout_classname = "oxd-userdropdown-link"


    def click_account(self):

        self.driver.find_element(By.CSS_SELECTOR, self.account_class).click()
    

    def click_logout(self):

        self.driver.find_element(By.CLASS_NAME, self.logout_classname).click()
        



