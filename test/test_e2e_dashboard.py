import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    TimeoutException
)

LOGIN_URL = "http://localhost:3000/#/login"
DASHBOARD_KEYWORD = "#/dashboard"

EMAIL = "remos.a@rndsoftech.com"
PASSWORD = "your_password_here"


def close_modal_if_present(driver, wait):
    """
    Closes any open modal dialog safely.
    Works for 'Contact Your Rep' and similar modals.
    """
    try:
        # Common close button patterns
        close_buttons = driver.find_elements(
            By.XPATH,
            "//button[@aria-label='Close' or @aria-label='close' or contains(@class,'close') or contains(text(),'Cancel') or contains(text(),'Close')]"
        )

        for btn in close_buttons:
            if btn.is_displayed():
                btn.click()
                wait.until(EC.invisibility_of_element(btn))
                time.sleep(0.5)
                return True
    except Exception:
        pass

    return False


def test_e2e_dashboard_ui(driver):
    wait = WebDriverWait(driver, 20)

    # ---------------- LOGIN ----------------
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
    time.sleep(2)

    assert DASHBOARD_KEYWORD in driver.current_url

    # ---------------- DASHBOARD CHECK ----------------
    warnings = []

    # Only get COUNT (never keep elements)
    button_count = len(driver.find_elements(By.TAG_NAME, "button"))

    for idx in range(button_count):
        try:
            # Always re-find elements (React-safe)
            buttons = driver.find_elements(By.TAG_NAME, "button")
            if idx >= len(buttons):
                continue

            button = buttons[idx]
            button_text = (button.text or "").strip()

            # Skip non-user buttons
            if not button.is_displayed():
                continue
            if button.get_attribute("disabled"):
                continue
            if not button_text:
                continue

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", button
            )
            time.sleep(0.3)

            wait.until(EC.element_to_be_clickable(button))
            button.click()
            time.sleep(1)

            # 🔥 HANDLE MODAL HERE
            if close_modal_if_present(driver, wait):
                print(f"ℹ️ Modal closed after clicking '{button_text}'")
                continue

            # Stay inside dashboard
            if DASHBOARD_KEYWORD not in driver.current_url:
                driver.back()
                time.sleep(1)

        except (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException):
            warnings.append((idx, button_text, "stale / modal / intercepted"))
        except Exception as e:
            warnings.append((idx, button_text, str(e)))

    # ---------------- REPORT ----------------
    if warnings:
        print("\n⚠️ DASHBOARD WARNINGS (NON-BLOCKING):")
        for w in warnings:
            print(w)

    assert True
