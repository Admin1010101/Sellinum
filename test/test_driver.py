def test_browser_launch(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
