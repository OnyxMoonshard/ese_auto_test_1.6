# coding=utf-8
import time
import unittest


class PublicCase5_1(unittest.TestCase):

    def reviewmyorder(self):
        '''确认订单、单订单'''
        browser = self.driver
        ese_order_checkbox = browser.find_element_by_xpath('//*[@class="el-checkbox__inner"]')
        ese_order_checkbox.click()

        ese_order_pay_btn = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        ese_order_pay_btn.click()
        time.sleep(20)
