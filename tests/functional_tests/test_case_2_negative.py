import time
import unittest

from jira import JIRA
from selenium import webdriver

from logic.brands_page import BrandsPage
from logic.cart_page import CartPage
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.check_out_payment_page import Check_Out_Page
from selenium.webdriver.chrome.service import Service


class negative_input_last_name_Test(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path="C:\\Users\\hp\\PycharmProjects\\finalProject\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("https://www.terminalx.com/")
        self.url_add_to_cart = "https://www.terminalx.com/pg/MutationAddAnyProductsToAnyCart"
        self.login_page = LoginPage(self.driver)
        self.checkout_page = Check_Out_Page(self.driver)

    def connect(self):
        TOKEN = "ATATT3xFfGF0iiJ-G0jPEKIaLaPq0u-iLuW72YVbEtUSDNjLa1jH-B28VrIEsbJvcKM2KQJAXbj0o7Ekp2GKhTmN_bYXZKwhf7apCR2dbL8h51RKggCllAb-WDashFIgTwA0Mxg0-zNQQjBdtYytzOzNM4KRZsV9I2ihjKUHXB2yJnWBdrZP1kw=4D64587B"
        auth_jira = JIRA(basic_auth=('saeed.esawi99@gmail.com', TOKEN),
                         options={'server': "https://saeed0bd.atlassian.net"})
        return auth_jira

    def create_issue(self, summery, description, project_key, issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': f'failed test: {summery}',
            'description': description,
            'issuetype': {'name': issue_type},
        }
        jira_auth_new = self.connect()
        new_issue = jira_auth_new.create_issue(fields=issue_dict)
        return new_issue.key

    # test case 2
    def test_negative_input_last_name(self):
        self.home_page = HomePage(self.driver)
        self.home_page.search_btn()
        self.home_page.search_text("מגבת")
        self.assertFalse(True, "this is failed")

    def tearDown(self):
        self.create_issue(self.connect, "this is first test", "SBYON", "Bug")
        print("Issue Created")
        # Close the browser window
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
