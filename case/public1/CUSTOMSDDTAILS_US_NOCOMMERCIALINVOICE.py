# coding=utf-8
import time
import unittest


class PublicCase4_1(unittest.TestCase):

    def customsddtails_us_nocommercialinvoice(self):
        '''美国始发、无商业发票'''
        browser = self.driver

        # ese_export_reasonbtn = browser.find_element_by_xpath('//*[@class="el-input__inner"]')[2]
        # browser.execute_script("arguments[0].click();", ese_export_reasonbtn)
        # ese_export_reason1 = \
        #     browser.find_element_by_xpath('//*[@class="el-scrollbar__view el-select-dropdown__list"][1]/li/span')[0]
        # browser.execute_script("arguments[0].click();", ese_export_reason1)

        ese_export_reason = browser.find_element_by_xpath('//*[@placeholder="Please select your reason"]')
        browser.execute_script("arguments[0].click();", ese_export_reason)

        ese_export_reason1 = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[3]/span')
        browser.execute_script("arguments[0].click();", ese_export_reason1)

        time.sleep(5)

        ese_commercial_invoice = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[2]/div[2]/div/div[2]/label')
        ese_commercial_invoice.click()

        ese_custom_next_btn = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[3]/button[2]/span')
        ese_custom_next_btn.click()
        time.sleep(5)