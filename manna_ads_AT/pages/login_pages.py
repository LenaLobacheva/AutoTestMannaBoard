from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from base.base_class import Base

def supper():
    pass

class Login_page(Base):

    url = 'https://test.manna-ads.cyberia.studio/'

    def __init__(self, driver):
        self.driver = driver

    # Locators
    url = 'https://test.manna-ads.cyberia.studio/'

    enter_button = '/html/body/div[2]/div[1]/div[1]/div/div/div[2]/ul/li[3]/a'
    email = "//input[@id='mLogin']"
    password = '//input[@id="mPassword"]'
    login_button = '//button[@class="col btn btn--success btn--height"]'
    main_word = '//span[@title="Король Артур"]'
    cookies_button = '/html/body/div[8]/div[2]'

    # Getters
    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_cookies_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cookies_button)))


# Actions - описываем, что именно будем делать с локаторами
    def click_enter_button(self):
        self.get_enter_button().click()
        print('click enter_button')
    def input_email(self, email):
        self.get_email().send_keys(email)
        print('input email')
    def input_password(self, password):
        self.get_password().send_keys(password)
        print('input password')
    def click_login_button(self):
        self.get_login_button().click()
        print('click login_button')
    def click_cookies_button(self):
        self.get_cookies_button().click()
        print('click accept cookies')

        # Methods - описываем, какие методы вызываем
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_button()
        self.input_email("riyanak623@fandua.com")
        self.input_password("riyanak623")
        self.click_login_button()
        self.assert_word(self.get_main_word(), 'Король Артур')
        self.click_cookies_button()









