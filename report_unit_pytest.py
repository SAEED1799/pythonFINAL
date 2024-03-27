import unittest
import html
from datetime import datetime

# Import test modules
from tests.functional_tests import test_case_2_negative, test_check_price, test_Check_Sale_Page_Is_OK

def create_suite():
    suite = unittest.TestSuite()
    # Load tests from the test modules
    for test_module in [test_case_2_negative, test_check_price, test_Check_Sale_Page_Is_OK]:
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
    report_file = 'terminalX_report.html'
    with open(report_file, 'w') as f:
        f.write(f"<html><head><title>Test Report</title></head><body>")
        f.write(f"<h1>Test Report - {now}</h1>")
        f.write(f"<p>Total tests: {test_result.testsRun}</p>")
        f.write(f"<p>Failures: {len(test_result.failures)}</p>")
        f.write(f"<p>Errors: {len(test_result.errors)}</p><hr>")

        for test, result, traceback in test_result.results:
            color = "green" if result == "PASS" else "red"
            f.write(f"<div style='color:{color};'><h2>{test.id()}</h2>")
            f.write(f"<p><strong>Result:</strong> {result}</p>")
            if traceback:
                tb = html.escape("\n".join(unittest.TextTestResult._exc_info_to_string(test_result, test, traceback).splitlines()))
                f.write(f"<pre>{tb}</pre>")
            f.write("</div><hr>")

        f.write("</body></html>")

if __name__ == '__main__':
    test_suite = create_suite()
    runner = unittest.TextTestRunner(resultclass=HTMLTestResult, verbosity=2)
    result = runner.run(test_suite)
    generate_html_report(result)
