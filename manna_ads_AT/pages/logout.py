from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Logout():
    url = 'https://test.manna-ads.cyberia.studio/'

    def __init__(self, driver):
        self.driver = driver

# Locators

    url = 'https://test.manna-ads.cyberia.studio/'
    title_header = '//li[@class="navbar__item dropdown no-arrow"]'
    logout = '//a[@href="https://test.manna-ads.cyberia.studio/logout"]'

    # Getters
    def get_title_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_header)))

    def get_logout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.logout)))

# Actions - описываем, что именно будем делать с локаторами
    def click_title_header(self):
        self.get_title_header().click()
        print('click select profile')

    def click_logout(self):
        self.get_logout().click()
        print('logout')

 # Methods - описываем, какие методы вызываем
    def user_logout(self):
        self.click_title_header()
        self.click_logout()

