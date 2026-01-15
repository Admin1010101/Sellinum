from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_login():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://promedhealthplus.com/#/login")

    wait = WebDriverWait(driver, 30)

    # Email field (React-safe)
    email = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
    )
    email.send_keys("remos.a@rndsoftech.com")

    # Password field
    password = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )
    password.send_keys("Ilovegod@23")

    # Sign In button (by visible text)
    sign_in = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[normalize-space()='Sign In']"
        ))
    )
    sign_in.click()

    # Wait for page to change after login attempt
    wait.until(EC.url_changes("https://promedhealthplus.com/#/login"))

    # Simple validation
    assert "login" not in driver.current_url.lower()

    driver.quit()
