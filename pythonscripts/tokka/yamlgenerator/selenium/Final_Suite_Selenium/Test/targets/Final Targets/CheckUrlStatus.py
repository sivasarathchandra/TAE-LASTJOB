import unittest
import sys
from loginPage import login
from selenium.common.exceptions import NoSuchElementException

class CheckUrlStatus(unittest.TestCase):

    def setUp(self):
        if domain == 'staging':
            self.browser = login.login_staging()
            self.url = 'https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category'
        elif domain == '15stp':
            self.browser = login.login_15stp()
            self.url = 'https://15stpdep.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category'
        else:
            self.browser = login.login_dev()
            self.url = 'https://adventisthealthsystem.analytics.devcernerpophealth.com/explore/revenue_cycle/config/config/age_category'

    def test_check_url_status(self):
        pageStatus = 0
        self.browser.get(self.url)
        try:
            self.browser.find_element_by_xpath('//*[@id="global-wrapper"]/header/h1/a')
            pageStatus = 1
        except NoSuchElementException:
            pageStatus = 0

        self.assertEqual(pageStatus, 1)
        self.browser.close()

if __name__ == '__main__':
    domain = sys.argv[1]
    del sys.argv[1:]
    unittest.main()