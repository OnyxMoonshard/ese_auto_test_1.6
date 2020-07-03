# coding=utf-8
import time
import unittest


class PublicCase7_1(unittest.TestCase):

    def printdocs(self):
        '''打印收据、发票、面单'''
        browser = self.driver
        '''
        ese_print_downloaddoc = browser.find_element_by_xpath('//*[@class="el-row"][1]/button')
        ese_print_downloaddoc.click()

        ese_print_download = \
            browser.find_elements_by_xpath('//*[@class="el-button el-button--success el-button--small"]')[0]
        ese_print_download.click()
        '''
        ese_download_receipt = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[3]/button[3]/span')
        ese_download_receipt.click()
        time.sleep(3)
        ese_download_commercial = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[3]/button[2]/span')
        ese_download_commercial.click()
        time.sleep(3)
        ese_download_ec_label = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[3]/button[1]/span')
        ese_download_ec_label.click()
        time.sleep(10)
