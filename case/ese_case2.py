import os
import time
import unittest  # 导入单元测试包

import resources
from selenium.webdriver.common.action_chains import ActionChains
import paramunittest
from selenium import webdriver

from until import getDir
from until.common import get_excel_value

import sys

from case.public1.ADDRESSDETAILS_OTHER_WAREHOUSE_NONLOGIN import PublicCase3
from case.public1.PARCEL_DETAILS_MULTIPLY import PublicCase4
from case.public1.CUSTOMSDDTAILS_US_NOCOMMERCIALINVOICE import PublicCase4_1
from case.public1.REVIEWMYORDER import PublicCase5_1
from case.public1.PAYMENTOPTIONS_USUK import PublicCase6_1
from case.public1.PRINTDOCS import PublicCase7_1

# proDir = getDir.proDir
now = time.strftime("%Y_%m_%d %H:%M:%S")
case2 = get_excel_value("test_data.xlsx", "case2")


@paramunittest.parametrized(*case2)
class EseCase2(unittest.TestCase):
    '''英国至非中国多商品单一收货人匿名下单'''

    def setParameters(self, case_name, ese_from_postcode, ese_to_postcode, ese_weight, ese_length,
                      ese_width, ese_height, ese_shipper_contactname, ese_shipper_company, ese_shipper_addr1,
                      ese_shipper_addr2, ese_shipper_city, ese_shipper_state, ese_shipper_zipcode, ese_shipper_email,
                      ese_shipper_phone, ese_receiver_contactname, ese_receiver_company, ese_receiver_addr1,
                      ese_receiver_addr2, ese_receiver_city, ese_receiver_district, ese_receiver_provnice,
                      ese_receiver_zipcode, ese_receiver_email, ese_receiver_phone, ese_tracking_waybill_no,
                      ese_item_name, ese_item_weight, ese_item_quantity, ese_unit_value, ese_item_details,
                      ese_pay_cardno, ese_pay_youxiaoqi, ese_pay_cvc, ese_pay_postcode, ese_successful):

        self.case_name = case_name
        self.ese_from_postcode = ese_from_postcode
        self.ese_to_postcode = ese_to_postcode
        self.ese_weight = ese_weight
        self.ese_length = ese_length
        self.ese_width = ese_width
        self.ese_height = ese_height

        self.ese_shipper_contactname = ese_shipper_contactname
        self.ese_shipper_company = ese_shipper_company
        self.ese_shipper_addr1 = ese_shipper_addr1
        self.ese_shipper_addr2 = ese_shipper_addr2
        self.ese_shipper_city = ese_shipper_city
        self.ese_shipper_state = ese_shipper_state
        self.ese_shipper_zipcode = ese_shipper_zipcode
        self.ese_shipper_email = ese_shipper_email
        self.ese_shipper_phone = ese_shipper_phone

        self.ese_receiver_contactname = ese_receiver_contactname
        self.ese_receiver_company = ese_receiver_company
        self.ese_receiver_addr1 = ese_receiver_addr1
        self.ese_receiver_addr2 = ese_receiver_addr2
        self.ese_receiver_city = ese_receiver_city
        self.ese_receiver_district = ese_receiver_district
        self.ese_receiver_provnice = ese_receiver_provnice
        self.ese_receiver_zipcode = ese_receiver_zipcode
        self.ese_receiver_email = ese_receiver_email
        self.ese_receiver_phone = ese_receiver_phone
        self.ese_tracking_waybill_no = ese_tracking_waybill_no

        self.ese_item_name = ese_item_name
        self.ese_item_weight = ese_item_weight
        self.ese_item_quantity = ese_item_quantity
        self.ese_unit_value = ese_unit_value
        self.ese_item_details = ese_item_details

        self.ese_pay_cardno = ese_pay_cardno
        self.ese_pay_youxiaoqi = ese_pay_youxiaoqi
        self.ese_pay_cvc = ese_pay_cvc
        self.ese_pay_postcode = ese_pay_postcode
        self.ese_successful = ese_successful

    def setUp(self):
        self._testMethodDoc = "</br>英国至非中国多商品单一收货人匿名下单:</br>" + self.case_name  # 设置用例名称
        self.options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 "profile.default_content_setting_values.automatic_downloads": 1}

        self.options.add_experimental_option('prefs', prefs)
        self.options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        # self.options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        self.driver = webdriver.Chrome(options=self.options, executable_path=resources.driverPath)
        self.baseUrl = resources.base_url
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        time.sleep(5)

    def index(self):
        '''首页'''
        browser = self.driver
        ese_to = browser.find_element_by_xpath('//*[@id="areaEnd"]')
        browser.execute_script("arguments[0].click();", ese_to)
        ese_to1 = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span')
        browser.execute_script("arguments[0].click();", ese_to1)

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




    # def get_screenshot(self):
    #     file_path = os.path.join(proDir, "report", "shots")
    #     if not os.path.exists(file_path):
    #         os.mkdir(file_path)
    #     shot_name = "screenshot_%s.png" % now
    #     shot_path = os.path.join(proDir, file_path, shot_name)
    #     self.driver.get_screenshot_as_file(shot_path)

    def tearDown(self):
        browser = self.driver
        # self.get_screenshot()
        browser.close()
        browser.quit()

    def test_main(self):
        self.index()
        PublicCase3.addressdetails_other_warehouse_nonlogin(self, self.ese_shipper_contactname, self.ese_shipper_company,
                                                            self.ese_shipper_addr1,
                                                            self.ese_shipper_addr2, self.ese_shipper_city,
                                                            self.ese_shipper_state, self.ese_shipper_zipcode,
                                                            self.ese_shipper_email,
                                                            self.ese_shipper_phone, self.ese_receiver_contactname,
                                                            self.ese_receiver_company, self.ese_receiver_addr1,
                                                            self.ese_receiver_addr2,
                                                            self.ese_receiver_city, self.ese_receiver_district,
                                                            self.ese_receiver_provnice, self.ese_receiver_zipcode,
                                                            self.ese_receiver_email,
                                                            self.ese_receiver_phone)
        PublicCase4.parcel_details_multiply(self,self.ese_item_name,self.ese_item_weight,self.ese_item_quantity,self.ese_unit_value,self.ese_item_details)
        PublicCase4_1.customsddtails_us_nocommercialinvoice(self)
        PublicCase5_1.reviewmyorder(self)
        PublicCase6_1.paymentoptions_usuk(self,self.ese_pay_cardno,self.ese_pay_youxiaoqi,self.ese_pay_cvc,self.ese_pay_postcode)
        PublicCase7_1.printdocs(self)



if __name__ == "__main__":
    unittest.main(verbosity=2)
