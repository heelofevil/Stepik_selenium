import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://checkme.kavichki.com/"

class TestMainPage1():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    @pytest.mark.smoke
    def test_add_and_create_var(self):
        self.browser.get(link)
        # Open block 'Create new'
        self.browser.find_element(By.ID, 'open').click()

        # test values
        values1, values2, values3 = 'Большой зонт', '2', '499'

        # input values
        self.browser.find_element(By.XPATH, "//input[@id='name']").send_keys(values1)

        # input values
        self.browser.find_element(By.XPATH, "//input[@id='count']").send_keys(values2)

        # input values
        self.browser.find_element(By.XPATH, "//input[@id='price']").send_keys(values3)


        # Click button "add"
        self.browser.find_element(By.XPATH, "//input[@id='add']").click()


        check1 = self.browser.find_element(By.CSS_SELECTOR, 'tbody tr:last-child td:nth-child(1)')
        text_check1 = check1.text

        check2 = self.browser.find_element(By.CSS_SELECTOR, 'tbody tr:last-child td:nth-child(2)')
        text_check2 = check2.text

        check3 = self.browser.find_element(By.CSS_SELECTOR, 'tbody tr:last-child td:nth-child(3)')
        text_check3 = check3.text

        # expected results
        assert values1 == text_check1, 'Values "Name" not equal to input'
        assert values2 == text_check2, 'Values "Count" not equal to input!'
        assert values3 == text_check3, 'Values "Cost" not equal to input'


