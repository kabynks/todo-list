import time
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
    '''функциональный тест'''

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return 
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')
