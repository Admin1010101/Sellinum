# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def send_otp(self):
        self.driver.find_element(By.ID, "sendOtp").click()

    def enter_otp(self, otp):
        self.driver.find_element(By.ID, "otp").send_keys(otp)

    def verify(self):
        self.driver.find_element(By.ID, "verifyOtp").click()


