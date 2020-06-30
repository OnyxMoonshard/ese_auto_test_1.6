# coding=utf-8
import time
import unittest


class PublicCase7_1(unittest.TestCase):

    def printdocs(self):
        '''打印订单'''
        browser = self.driver
        ese_print_downloaddoc = browser.find_element_by_xpath('//*[@class="el-row"][1]/button')
        ese_print_downloaddoc.click()

        ese_print_download = \
            browser.find_elements_by_xpath('//*[@class="el-button el-button--success el-button--small"]')[0]
        ese_print_download.click()

        time.sleep(10)
