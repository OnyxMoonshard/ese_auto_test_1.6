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
from case.public1.ADDRESSDETAILS_CN_WAREHOUSE_NONLOGIN import PublicCase1
from case.public1.PARCEL_DETAILS_MULTIPLY import PublicCase4

# proDir = getDir.proDir
now = time.strftime("%Y_%m_%d %H:%M:%S")
case1 = get_excel_value("test_data.xlsx", "case1")


@paramunittest.parametrized(*case1)
class EseCase1(unittest.TestCase):
    '''英国至非中国多商品单一收货人匿名下单'''

    def setParameters(self, case_name, ese_from_postcode, ese_to_postcode, ese_weight, ese_length,
                      ese_width, ese_height, ese_shipper_contactname, ese_shipper_company, ese_shipper_addr1,
                      ese_shipper_addr2, ese_shipper_city, ese_shipper_state, ese_shipper_zipcode, ese_shipper_email,
                      ese_shipper_phone, ese_receiver_contactname, ese_receiver_company, ese_receiver_addr1,
                      ese_receiver_addr2, ese_receiver_city, ese_receiver_district, ese_receiver_provnice,
                      ese_receiver_zipcode, ese_receiver_email, ese_receiver_phone, ese_tracking_waybill_no,
                      ese_item_name, ese_item_weight, ese_item_quantity, ese_unit_value, ese_item_details,
                      ese_pay_cardno, ese_pay_youxiaoqi, ese_pay_cvc, ese_pay_postcode, ese_successful):
        """
        从 excel 中获取用例
        :param case_name: 用例名称
        :param ese_from_postcode: 发货人邮编
        :param ese_to_postcode: 收货人邮编
        :param ese_weight: 总重量
        :param ese_length: 总长度
        :param ese_width: 总宽度
        :param ese_height: 总高度
        :param ese_item_name: 第一个商品描述
        :param ese_quantity: 第一个商品数量
        :param ese_weight: 第一个商品重量
        :param ese_unit_value: 第一个商品总价格
        :param ese_item_details: 第一个商品详情
        :param ese_shipper_contactname: 发货人联系名称
        :param ese_shipper_company: 发货人公司
        :param ese_shipper_addr1: 发货地址1
        :param ese_shipper_city: 发货城市/城镇
        :param ese_shipper_state: 发货州/省
        :param ese_shipper_email: 发货人email
        :param ese_shipper_phone: 发货人电话
        :param ese_receiver_contactname: 收货人联系名称
        :param ese_receiver_company: 收货人公司
        :param ese_receiver_addr1: 收货人地址1
        :param ese_receiver_city: 收货人城市
        :param ese_receiver_district: 收货人州/省
        :param ese_receiver_email: 收货人邮箱
        :param ese_receiver_phone: 收货人电话
        :param ese_pay_cardno: 支付卡号
        :param ese_pay_youxiaoqi: 银行卡有效期
        :param ese_pay_cvc: 银行卡CVC
        :param ese_pay_postcode: 支付邮编
        :param ese_successful: 系统返回成功的结果
        :return:
        """
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
        '''
        # ese_from = browser.find_elements_by_xpath('//*[@class="el-select-dropdown__item area-start-option"]/span')[3]
        # browser.execute_script("arguments[0].click();", ese_from)
        # ese_to = browser.find_elements_by_xpath('//*[@class="el-select-dropdown__item area-end-option"]/span')[1]
        # browser.execute_script("arguments[0].click();", ese_to)        '''
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

    def custom(self):
        '''custom'''
        browser = self.driver

        ese_export_reasonbtn = browser.find_element_by_xpath('//*[@class="el-input__inner"]')[2]
        browser.execute_script("arguments[0].click();", ese_export_reasonbtn)
        ese_export_reason1 = \
            browser.find_element_by_xpath('//*[@class="el-scrollbar__view el-select-dropdown__list"][1]/li/span')[0]
        browser.execute_script("arguments[0].click();", ese_export_reason1)
        time.sleep(5)

        ese_COMMERCIAL_INVOICE = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[2]/div[2]/div/div[2]/label')
        ese_COMMERCIAL_INVOICE.click()

        ese_custom_next_btn = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[3]/button[2]/span')
        ese_custom_next_btn.click()
        time.sleep(20)

    def order(self):
        '''order'''
        browser = self.driver
        ese_order_checkbox = browser.find_elements_by_xpath('//*[@class="el-checkbox__original"]')
        for cb in ese_order_checkbox:
            browser.execute_script("arguments[0].click();", cb)

        ese_order_pay_btn = browser.find_element_by_xpath('//*[@class="btn-group el-row"]/div/button')
        ese_order_pay_btn.click()
        time.sleep(20)

    def pay(self):
        '''pay'''
        browser = self.driver
        iframe = browser.find_elements_by_tag_name('iframe')[0]
        browser.switch_to.frame(iframe);
        # WebDriverWait(browser, 50, 0.5).until(EC.presence_of_element_located((By.NAME, 'cardnumber')))
        ese_pay_cardno = browser.find_element_by_name('cardnumber')
        ese_pay_cardno.send_keys(int(self.ese_pay_cardno))
        time.sleep(5)
        ese_pay_youxiaoqi = browser.find_element_by_name('exp-date')
        ese_pay_youxiaoqi.send_keys(int(self.ese_pay_youxiaoqi))

        ese_pay_cvc = browser.find_element_by_name('cvc')
        ese_pay_cvc.send_keys(int(self.ese_pay_cvc))
        time.sleep(5)
        ese_pay_postcode = browser.find_element_by_name('postal')
        ese_pay_postcode.send_keys(int(self.ese_pay_postcode))
        browser.switch_to.default_content()
        ese_pay_pay_btn = browser.find_elements_by_xpath('//*[@class="pay-with-stripe"]')[0]
        ese_pay_pay_btn.click()

        time.sleep(20)

    def printDetail(self):
        '''printDetail'''
        browser = self.driver
        ese_print_downloaddoc = browser.find_element_by_xpath('//*[@class="el-row"][1]/button')
        ese_print_downloaddoc.click()

        ese_print_download = \
            browser.find_elements_by_xpath('//*[@class="el-button el-button--success el-button--small"]')[0]
        ese_print_download.click()

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
        PublicCase3_2.aDDRESSDETAILS_CN_WAREHOUSE_NONLOGIN(self, self.ese_shipper_contactname, self.ese_shipper_company,
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
        '''
        self.address()
        self.parcel_content_multiplegoods_singlereceiver()
        self.custom()
        self.order()
        self.pay()
        self.printDetail()
        '''


if __name__ == "__main__":
    unittest.main(verbosity=2)
