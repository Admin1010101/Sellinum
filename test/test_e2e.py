def test_login_dashboard_order(driver):
    driver.get("https://test-portal.company.com")

    assert "Login" in driver.title
