import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException
)

START_URL = "http://localhost:3000/#/login"


def test_full_ui_flow(driver):
    driver.get(START_URL)
    time.sleep(3)

    visited = set()
    issues = []

    def check_page():
        url = driver.current_url

        if url in visited:
            return

        print(f"\n🔍 Checking page: {url}")
        visited.add(url)

        # 🔒 Skip button testing on login page
        skip_buttons = "#/login" in url

        # -------- LINKS --------
        for link in driver.find_elements(By.TAG_NAME, "a"):
            try:
                href = link.get_attribute("href")
                if href and "localhost:3000" in href and href not in visited:
                    driver.execute_script("window.open(arguments[0]);", href)
                    driver.switch_to.window(driver.window_handles[-1])
                    time.sleep(1)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
            except Exception as e:
                issues.append(("LINK_ERROR", url, str(e)))

        # -------- BUTTONS --------
        if not skip_buttons:
            for idx, button in enumerate(driver.find_elements(By.TAG_NAME, "button")):
                try:
                    if button.get_attribute("disabled"):
                        continue

                    driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});", button
                    )
                    time.sleep(0.3)
                    button.click()
                    time.sleep(1)
                    driver.back()

                except (ElementClickInterceptedException, StaleElementReferenceException):
                    issues.append(("BUTTON_NOT_CLICKABLE", url, idx))
                except Exception as e:
                    issues.append(("BUTTON_ERROR", url, str(e)))

    check_page()

    if issues:
        print("\n❌ UI ISSUES FOUND:")
        for issue in issues:
            print(issue)

    assert not issues
