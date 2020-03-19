import unittest
import openpyxl
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/imad/PycharmProjects/test/chromedriver")
        # load the test data excel file
        wb = openpyxl.load_workbook("Amazon.xlsx")
        # activate the current worksheet
        self.sheet = wb.active


    def test_AmazonSearch(self):
        sheet=self.sheet
        driver=self.driver
        driver.get("https://www.amazon.com")
        driver.maximize_window()
        for row in sheet.iter_rows(min_row=2, max_col=1, max_row=5):
            for cell in row:
                search_box= driver.find_element_by_id("twotabsearchtextbox")
                search_box.click()
                search_box.clear()
                search_box.send_keys(cell.value)
                time.sleep(1)
                search_button_icon = driver.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input")
                search_button_icon.click()
                time.sleep(7)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()