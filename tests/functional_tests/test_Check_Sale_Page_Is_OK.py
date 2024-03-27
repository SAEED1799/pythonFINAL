import unittest
from selenium import webdriver
from logic.brands_page import BrandsPage
from logic.home_page import HomePage


class TerminalXTest(unittest.TestCase):

    def setUp(self):
        # Initialize WebDriver (in this case, Chrome)
        self.driver = webdriver.Chrome("C:\\Users\\hp\\PycharmProjects\\pythonFINAL\\chromedriver.exe")
        self.driver.maximize_window()  # Maximize the browser window
        self.driver.get("https://www.terminalx.com/")

    def test_terminal_x_on_sale_page(self):
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_sales_button()
        self.brand_page = BrandsPage(self.driver)
        self.assertTrue(self.brand_page.on_sale_is_displayed(), "on sale page ok")

    def tearDown(self):
        # Close the browser
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
