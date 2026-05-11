from calculator_page import CalculatorPage
from selenium import webdriver


def test_calculator():
    driver = webdriver.Chrome()

    try:
        page = CalculatorPage(driver)
        page.open()
        page.set_delay("45")

        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

        rezultat = page.get_result()

        assert rezultat == "15", f"должно быть 15 а вышло {rezultat}"

    finally:
        driver.quit()