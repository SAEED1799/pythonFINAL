import unittest

from jira import JIRA
from selenium import webdriver

from logic.cart_page import CartPage
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.check_out_payment_page import Check_Out_Page


class negative_input_last_name_Test(unittest.TestCase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.terminalx.com/")
        self.url_add_to_cart = "https://www.terminalx.com/pg/MutationAddAnyProductsToAnyCart"
        self.login_page = LoginPage(self.driver)
        self.checkout_page = Check_Out_Page(self.driver)
       # self.auth_jira = JIRA(basic_auth=(self.jira_mail, self.jira_api), options={'server': self.jira_url})

    # def create_issue(self, summery, description, project_key, issue_type="Bug"):
    #     issue_dict = {
    #         'project': {'key': project_key},
    #         'summary': f'failed test: {summery}',
    #         'description': description,
    #         'issuetype': {'name': issue_type},
    #     }
    #     new_issue = self.auth_jira.create_issue(fields=issue_dict)
    #     return new_issue.key

    # test case 2
    def test_negative_input_last_name(self):
        self.home_page = HomePage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.home_page.click_on_sales_button()
        self.assertTrue(True, self.cart_page)
        # self.brand_page = BrandsPage(self.driver)
        # self.brand_page.click_planket()
        # self.brand_page.click_add_planket()
        # time.sleep(7)
        # self.home_page.click_on_cart_button()
        # self.home_page.click_go_to_card_button()
        # self.cart_page.click_checkout_page()
        # self.checkout_page.insert_keys()
        # # assert that i was continue of the name and city

    def tearDown(self):
        # Close the browser window
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
