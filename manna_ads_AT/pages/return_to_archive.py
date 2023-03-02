from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Return_from_archive():
    url = 'https://test.manna-ads.cyberia.studio/'

    def __init__(self, driver):
        self.driver = driver

        # Locators

    url = 'https://test.manna-ads.cyberia.studio/'
    title_header = '//li[@class="navbar__item dropdown no-arrow"]'
    archive = '/html/body/div[2]/div[1]/div[1]/div/div/div[2]/ul/li[4]/ul/li[6]/a'
    return_from_archive = '//a[@title="Востановить"]'

    # Getters
    def get_title_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_header)))

    def get_archive(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.archive)))

    def get_return_from_archive(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.return_from_archive)))

# Actions - описываем, что именно будем делать с локаторами
    def click_title_header(self):
        self.get_title_header().click()
        print('click select profile')

    def click_archive(self):
        self.get_archive().click()
        print('click archive')

    def click_return_from_archive(self):
        self.get_return_from_archive().click()
        print('return from archive')

        # Methods - описываем, какие методы вызываем

    def return_ad(self):
        self.click_title_header()
        self.click_archive()
        self.click_return_from_archive()


