from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Ad_to_archive():
    url = 'https://test.manna-ads.cyberia.studio/'

    def __init__(self, driver):
        self.driver = driver

    # Locators

    url = 'https://test.manna-ads.cyberia.studio/'
    title_header = '//li[@class="navbar__item dropdown no-arrow"]'
    my_ad = '/html/body/div[2]/div[1]/div[1]/div/div/div[2]/ul/li[4]/ul/li[3]/a/span[1]'
    archive = '/html/body/div[2]/div[3]/div/div/div[2]/div/div[3]/div/div/div[1]/div[2]/div/a[4]'

    # Getters
    def get_title_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_header)))
    def get_my_ad(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.my_ad)))
    def get_archive(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.archive)))

    # Actions - описываем, что именно будем делать с локаторами
    def click_title_header(self):
        self.get_title_header().click()
        print('click select profile')
    def click_my_ad(self):
        self.get_my_ad().click()
        print('click select my ad')
    def click_archive(self):
        self.get_archive().click()
        print('ad to archive')

    # Methods - описываем, какие методы вызываем
    def profile(self):
        self.click_title_header()
        self.click_my_ad()
        self.click_archive()


