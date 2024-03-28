README - Automation Project: pythonFINAL
Overview
The pythonFINAL project is a comprehensive automation testing suite designed for extensive testing of web applications. It covers various types of tests, including API tests, functional tests, non-functional tests, and the ability to generate test reports. This suite is structured to facilitate easy navigation, execution, and maintenance of tests.

Project Structure
.venv: Virtual environment directory for Python packages. Keeps project dependencies isolated.
infra: Contains infrastructure-as-code or configurations for setting up the testing environment.
logic: Holds the business logic for test setup, tear down, and utility functions.
tests:
api_tests: Tests focused on the application's API layer, ensuring endpoints behave as expected.
functional_tests: Includes tests verifying the application's functionality from a user's perspective.
test_case_2_negative.py: A specific negative case test.
test_check_price.py: Verifies correctness of price listings.
test_Check_Sale_Page_Is_OK.py: Ensures the sales page loads and displays correctly.
test_log_in.py: Tests login functionality.
test_remove_item.py: Validates item removal functionality.
test_search_is_good.py: Checks search feature accuracy and responsiveness.
title_test.py: Assesses page title accuracy across the application.
non_functional_tests: Houses tests for non-functional aspects like performance and security.
test_reports: Destination for generated reports post-test execution.
test_api_continue_ui: Scripts for tests that span both API and UI aspects.
run_test.py: Central script to run the entire test suite or specific tests.
utils:
api_config.json: Configuration for API tests.
api_get_data.py: Utility for fetching data required for API tests.
config_terminalX.json: General configuration for the test suite.
chromedriver.exe: ChromeDriver executable for Selenium-based tests.
Jenkinsfile: Defines the pipeline for running tests in a CI/CD environment like Jenkins.
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/SAEED1799/pythonFINAL
cd pythonFINAL
Setup Virtual Environment (Windows):

Copy code
python -m venv .venv
.\.venv\Scripts\activate
For Linux/Mac:

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
Install Dependencies:

Copy code
pip install -r requirements.txt
Running Tests
Run all tests:

css
Copy code
python run_test.py --all
Run specific test category:

For API tests:

css
Copy code
python run_test.py --api
For Functional tests:

css
Copy code
python run_test.py --functional
Generate Test Report:

After tests execution, reports will be saved in test_reports.

Contribution
Contributions to enhance or extend the test suite are welcome. Please submit a pull request with your proposed changes or additions.

Support
For issues or questions regarding the test suite, please file an issue on the project's GitHub repository.
