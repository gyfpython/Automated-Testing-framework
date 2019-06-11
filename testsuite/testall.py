#!coding=utf-8
import unittest,time
from HtmlTestRunner import HTMLTestRunner

test_dir = "..\\testcases\\"
#print(test_dir)
report_dir = "..\\report\\"
#log_dir = "..\\log\\"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
        now = time.strftime("%d-%m-%Y-%H-%M-%S")
        #logfile = log_dir + now + "-test.log"
        #fp = open(logfile, "w")
        Runner = HTMLTestRunner(output=report_dir,report_title="Test report",descriptions="Cases run results: ", verbosity=2)
        Runner.run(discover)