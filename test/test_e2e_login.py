from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "http://localhost:3000/#/login"
DASHBOARD_KEYWORD = "#/dashboard"

EMAIL = "remos.a@rndsoftech.com"
PASSWORD = ""


def test_e2e_login(driver):
    wait = WebDriverWait(driver, 20)

    driver.get(LOGIN_URL)

    email = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    password = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
    )

    email.clear()
    email.send_keys(EMAIL)

    password.clear()
    password.send_keys(PASSWORD)
    password.send_keys(Keys.ENTER)

    wait.until(EC.url_contains(DASHBOARD_KEYWORD))

    assert DASHBOARD_KEYWORD in driver.current_url
