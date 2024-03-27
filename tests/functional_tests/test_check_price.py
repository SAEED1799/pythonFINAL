import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from logic.brands_page import BrandsPage
# Assuming logic.category_page and logic.product_details_page are your custom modules
from logic.home_page import HomePage


class TerminalXProductTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path="C:\\Users\\hp\\PycharmProjects\\finalProject\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.terminalx.com/")

    def convert_price_to_float(self, price_str):
        cleaned_price = ''.join(c for c in price_str if c.isdigit() or c == '.')
        return float(cleaned_price)

    def test_sort_price_low_to_high(self):
        self.home_page = HomePage(self.driver)
        self.home_page.search_btn()
        self.home_page.search_text("nike")
        self.brand_page = BrandsPage(self.driver)
        self.brand_page.sort_by_brand()
        self.assertTrue(self.brand_page.sort_isDisplayed(),
                        f"First item price ""first_product"" is not lower than or equal to second item price second_price.")

    def tearDown(self):
        # Close the browser
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
