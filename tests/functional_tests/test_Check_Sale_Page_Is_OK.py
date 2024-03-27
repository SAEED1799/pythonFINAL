import unittest
from selenium import webdriver
from logic.brands_page import BrandsPage
from logic.home_page import HomePage
from selenium.webdriver.chrome.service import Service


class TerminalXTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path="C:\\Users\\hp\\PycharmProjects\\finalProject\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()  # Maximize the browser window
        self.driver.get("https://www.terminalx.com/")

    def test_terminal_x_on_sale_page(self):
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_sales_button()
        self.brand_page = BrandsPage(self.driver)
        #self.assertTrue(self.brand_page.on_sale_is_displayed(), "on sale page ok")
        self.assertTrue(False, "on sale page ok")

    def tearDown(self):
        # Close the browser
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
