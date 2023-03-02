from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Ad_to_favorites(Base):
    url = 'https://test.manna-ads.cyberia.studio/'

    def __init__(self, driver):
        self.driver = driver

    # Locators

    url = 'https://test.manna-ads.cyberia.studio/'

    ad_favorites = '/html/body/div[2]/div[2]/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/a[2]/img'

    # Getters
    def get_ad_favorites(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ad_favorites)))

# Actions - описываем, что именно будем делать с локаторами
    def click_ad_favorites(self):
        self.get_ad_favorites().click()
        print('click ad favorites')

# Methods - описываем, какие методы вызываем
    def ad_to_favorites(self):
        self.click_ad_favorites()


