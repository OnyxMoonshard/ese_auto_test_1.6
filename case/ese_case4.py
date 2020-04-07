import os
import time
import unittest  # 导入单元测试包

import paramunittest
from selenium import webdriver
from selenium.webdriver import ActionChains

from until import getDir
from until.common import get_excel_value

proDir = getDir.proDir
now = time.strftime("%Y_%m_%d %H:%M:%S")
case4 = get_excel_value("test_data.xlsx", "case4")


@paramunittest.parametrized(*case4)
class EseCase4(unittest.TestCase):
    '''英国至非中国MY PARCELS OVERVIEW'''

    def setParameters(self, case_name, ese_from_postcode, ese_to_postcode, ese_weight, ese_length, ese_width,
                      ese_height,username,password, ese_successful ):
        """
        从 excel 中获取用例
        :param case_name: 用例名称
        :param username: 用户名
        :param password: 密码
        :param ese_from_postcode: 发货人邮编
        :param ese_to_postcode: 收货人邮编
        :param ese_weight: 总重量
        :param ese_length: 总长度
        :param ese_width: 总宽度
        :param ese_height: 总高度
        :param ese_successful: 系统返回成功的结果
        :return:
        """
        self.case_name = case_name
        self.username = username
        self.password = password
        self.ese_from_postcode = ese_from_postcode
        self.ese_to_postcode = ese_to_postcode
        self.ese_weight = ese_weight
        self.ese_length = ese_length
        self.ese_width = ese_width
        self.ese_height = ese_height
        self.ese_successful = ese_successful

    def setUp(self):
        self._testMethodDoc = "</br>英国至非中国MY PARCELS OVERVIEW:</br>" + self.case_name  # 设置用例名称
        self.options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 "profile.default_content_setting_values.automatic_downloads": 1}

        self.options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(options=self.options)
        self.baseUrl = 'http://106.39.97.90:17885/#/tools/uk/1'
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        time.sleep(20)

    def index(self):
        '''首页'''
        browser = self.driver
        ese_to = browser.find_elements_by_xpath('//*[@class="el-select-dropdown__item area-end-option"]/span')[2]
        browser.execute_script("arguments[0].click();", ese_to)
        ese_from_postcode = browser.find_element_by_id('areaStartPost')
        ese_from_postcode.send_keys(str(self.ese_from_postcode))
        ese_to_postcode = browser.find_element_by_id('areaEndPost')
        ese_to_postcode.send_keys(int(self.ese_to_postcode))
        ese_weight = browser.find_element_by_id('grossWeight')
        ese_weight.send_keys(str(self.ese_weight))
        ese_length = browser.find_element_by_id('length')
        ese_length.send_keys(str(self.ese_length))
        ese_width = browser.find_element_by_id('width')
        ese_width.send_keys(str(self.ese_width))
        ese_height = browser.find_element_by_id('height')
        ese_height.send_keys(str(self.ese_height))
        ese_quotenow = browser.find_element_by_id('submit')
        ese_quotenow.click()
        time.sleep(10)

    def my_parcels(self):
        '''my_parcels'''
        browser = self.driver
        # 悬停到MyAccount
        # 登录
        ese_my_account = browser.find_elements_by_xpath('//*[@class="txt"]')[1]
        actions = ActionChains(browser)
        actions.move_to_element(ese_my_account).perform()
        time.sleep(10)
        ese_sign_in = browser.find_elements_by_xpath('//*[@class="menu"]/li')[0]
        browser.execute_script("arguments[0].click();", ese_sign_in)
        time.sleep(10)
        ese_user_email = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[13]
        ese_user_email.send_keys(self.username)
        ese_user_pwd = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[14]
        ese_user_pwd.send_keys(self.password)
        # ese_rememberme = browser.find_elements_by_xpath('//*[@class="el-checkbox__inner"]')[1]
        # browser.execute_script("arguments[0].click();", ese_rememberme)
        ese_sign_in_btn = browser.find_elements_by_xpath('//*[@class="el-button el-button--success"]')[1]
        ese_sign_in_btn.click()

        time.sleep(10)
        actions.reset_actions()

        ese_myparcles_btn = browser.find_elements_by_xpath('//*[@class="txt"]')[1]
        ese_myparcles_btn.click()
        time.sleep(5)

    def shipments_in_progress(self):
        '''shipments_in_progress'''
        browser = self.driver
        ese_page1_row1_details_btn = browser.find_elements_by_xpath('//*[@class="el-button el-button--text el-button--small"]')[0]
        ese_page1_row1_details_btn.click()
        time.sleep(10)
        ese_page1_row1_details_close_btn = browser.find_elements_by_xpath('//*[@class="el-dialog__close el-icon el-icon-close"]')[3]
        browser.execute_script("arguments[0].click();", ese_page1_row1_details_close_btn)
        ese_fanye = browser.find_element_by_xpath('//*[@class="el-icon el-icon-arrow-right"]')
        browser.execute_script("arguments[0].click();", ese_fanye)
        time.sleep(10)

        ese_page2_row1_details_btn = browser.find_elements_by_xpath('//*[@class="el-button el-button--text el-button--small"]')[0]
        ese_page2_row1_details_btn.click()
        time.sleep(10)
        ese_page2_row1_details_close_btn = browser.find_elements_by_xpath('//*[@class="el-dialog__close el-icon el-icon-close"]')[3]
        browser.execute_script("arguments[0].click();", ese_page2_row1_details_close_btn)
        browser.execute_script("arguments[0].click();", ese_fanye)
        browser.execute_script("arguments[0].click();", ese_fanye)
        browser.execute_script("arguments[0].click();", ese_fanye)
        time.sleep(10)

        ese_page5_row1_details_btn = browser.find_elements_by_xpath('//*[@class="el-button el-button--text el-button--small"]')[0]
        ese_page5_row1_details_btn.click()
        time.sleep(10)
        ese_page5_row1_details_close_btn = browser.find_elements_by_xpath('//*[@class="el-dialog__close el-icon el-icon-close"]')[3]
        browser.execute_script("arguments[0].click();", ese_page5_row1_details_close_btn)

        ese_pengding_with_exceptions_btn = browser.find_elements_by_xpath('//*[@class="el-link--inner"]')[2]
        browser.execute_script("arguments[0].click();", ese_pengding_with_exceptions_btn)
        time.sleep(10)

    def pending_with_exceptions(self):
        '''pending_with_exceptions'''
        browser = self.driver
        ese_page1_row1_details_btn = browser.find_elements_by_xpath('//*[@class="el-button el-button--text el-button--small"]')[0]
        ese_page1_row1_details_btn.click()
        time.sleep(10)
        ese_page1_row1_details_close_btn = browser.find_elements_by_xpath('//*[@class="el-dialog__close el-icon el-icon-close"]')[3]
        browser.execute_script("arguments[0].click();", ese_page1_row1_details_close_btn)

        ese_completed_deliveries_btn = browser.find_elements_by_xpath('//*[@class="el-link--inner"]')[4]
        browser.execute_script("arguments[0].click();", ese_completed_deliveries_btn)
        time.sleep(5)

    def completed_deliveries(self):
        '''completed_deliveries'''
        browser = self.driver
        time.sleep(10)

        ese_pending_in_the_cart_btn = browser.find_elements_by_xpath('//*[@class="el-link--inner"]')[3]
        browser.execute_script("arguments[0].click();", ese_pending_in_the_cart_btn)
        time.sleep(5)

    def pending_in_the_cart(self):
        '''pending_in_the_cart'''
        browser = self.driver
        ese_order_checkbox = browser.find_elements_by_xpath('//*[@class="el-checkbox__original"]')[0]
        browser.execute_script("arguments[0].click();", ese_order_checkbox)

        ese_del_btn = browser.find_element_by_xpath('//*[@class="el-button el-button--danger"]')
        ese_del_btn.click()
        time.sleep(5)

        ese_order_checkbox = browser.find_elements_by_xpath('//*[@class="el-checkbox__original"]')[1]
        browser.execute_script("arguments[0].click();", ese_order_checkbox)
        ese_order_continue = browser.find_element_by_xpath('//*[@class="el-button el-button--primary"]')
        browser.execute_script("arguments[0].click();", ese_order_continue)

        time.sleep(15)



    def printDetail(self):
        '''printDetail'''
        browser = self.driver
        ese_print_downloaddoc = browser.find_element_by_xpath('//*[@class="el-row"][1]/button')
        ese_print_downloaddoc.click()

        ese_print_download = browser.find_elements_by_xpath('//*[@class="el-button el-button--success el-button--small"]')[0]
        ese_print_download.click()

        time.sleep(10)

    def get_screenshot(self):
        file_path = os.path.join(proDir, "testFile", "shots")
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        shot_name = "screenshot_%s.png" % now
        shot_path = os.path.join(proDir, file_path, shot_name)
        self.driver.get_screenshot_as_file(shot_path)

    def tearDown(self):
        browser = self.driver
        self.get_screenshot()
        # browser.close()
        # browser.quit()

    def test_main(self):
        self.index()
        self.my_parcels()
        self.shipments_in_progress()
        self.pending_with_exceptions()
        self.completed_deliveries()
        # self.pending_in_the_cart()
        # self.printDetail()

if __name__ == "__main__":
    unittest.main(verbosity=2)



