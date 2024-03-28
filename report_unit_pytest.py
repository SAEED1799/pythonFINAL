import unittest
import html
from datetime import datetime
import traceback

# Import test modules
from tests.functional_tests import test_case_2_negative, test_check_price, test_Check_Sale_Page_Is_OK, \
    test_search_is_good
from tests.test_api_continue_ui import test_add_api_check_ui

#this for jira
def create_suite():
    suite = unittest.TestSuite()
    # Load tests from the test modules
    for test_module in [test_search_is_good, test_Check_Sale_Page_Is_OK, test_case_2_negative]:
        suite.addTests(unittest.TestLoader().loadTestsFromModule(test_module))
    return suite


class HTMLTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.results = []

    def addError(self, test, err):
        super().addError(test, err)
        self.results.append((test, "ERROR", err))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.results.append((test, "FAIL", err))

    def addSuccess(self, test):
        super().addSuccess(test)
        self.results.append((test, "PASS", None))


def generate_html_report(test_result):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_file = 'report.html'
    with open(report_file, 'w') as f:
        f.write(f"<html><head><title>Test Report</title></head><body>")
        f.write(f"<h1>Test Report - {now}</h1>")
        f.write(f"<p>Total tests: {test_result.testsRun}</p>")
        f.write(f"<p>Failures: {len(test_result.failures)}</p>")
        f.write(f"<p>Errors: {len(test_result.errors)}</p><hr>")

        for test, result, exc_info in test_result.results:
            color = "green" if result == "PASS" else "red"
            f.write(f"<div style='color:{color};'><h2>{test.id()}</h2>")
            f.write(f"<p><strong>Result:</strong> {result}</p>")
            if exc_info:
                # Format the exception information into a string
                exc_info_formatted = ''.join(traceback.format_exception(*exc_info))
                exc_info_escaped = html.escape(exc_info_formatted)
                f.write(f"<pre>{exc_info_escaped}</pre>")
            f.write("</div><hr>")

        f.write("</body></html>")

if __name__ == '__main__':
    test_suite = create_suite()
    runner = unittest.TextTestRunner(resultclass=HTMLTestResult, verbosity=2)
    result = runner.run(test_suite)
    generate_html_report(result)
