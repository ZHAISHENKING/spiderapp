# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# print(driver.page_source)

import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

# driver = webdriver.Chrome()
# driver.get('http://www.jd.com')
#
# js = 'window.scrollTo(0,document.body.scrollHeight)'
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(2)
# driver.execute_script('window.stop()')
#
# print(driver.page_source)


if __name__ == "__main__":
    unittest.main()
