import os
import time
import unittest  # 导入单元测试包
import resources

import paramunittest
from selenium import webdriver

from until import getDir
from until.common import get_excel_value

# proDir = getDir.proDir
now = time.strftime("%Y_%m_%d %H:%M:%S")
case1 = get_excel_value("test_data.xlsx", "case1")


@paramunittest.parametrized(*case1)
class EseCase1(unittest.TestCase):
    '''英国至非中国多商品单一收货人匿名下单'''

    def setParameters(self, case_name, ese_from_postcode, ese_to_postcode, ese_weight, ese_length, ese_width,
                      ese_height, ese_item_description, ese_quantity, ese_item_weight, ese_total_value,
                      ese_item_details, ese_shipper_contactname, ese_shipper_company, ese_shipper_addr1,
                      ese_shipper_town, ese_shipper_state, ese_shipper_email, ese_shipper_phone,
                      ese_receiver_contactname, ese_receiver_company, ese_receiver_addr1, ese_receiver_town,
                      ese_receiver_state, ese_receiver_email, ese_receiver_phone,
                      ese_pay_cardno, ese_pay_youxiaoqi, ese_pay_cvc, ese_pay_postcode, ese_successful ):
        """
        从 excel 中获取用例
        :param case_name: 用例名称
        :param ese_from_postcode: 发货人邮编
        :param ese_to_postcode: 收货人邮编
        :param ese_weight: 总重量
        :param ese_length: 总长度
        :param ese_width: 总宽度
        :param ese_height: 总高度
        :param ese_item_description: 第一个商品描述
        :param ese_quantity: 第一个商品数量
        :param ese_item_weight: 第一个商品重量
        :param ese_total_value: 第一个商品总价格
        :param ese_item_details: 第一个商品详情
        :param ese_shipper_contactname: 发货人联系名称
        :param ese_shipper_company: 发货人公司
        :param ese_shipper_addr1: 发货地址1
        :param ese_shipper_town: 发货城市/城镇
        :param ese_shipper_state: 发货州/省
        :param ese_shipper_email: 发货人email
        :param ese_shipper_phone: 发货人电话
        :param ese_receiver_contactname: 收货人联系名称
        :param ese_receiver_company: 收货人公司
        :param ese_receiver_addr1: 收货人地址1
        :param ese_receiver_town: 收货人城市
        :param ese_receiver_state: 收货人州/省
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
        self.ese_item_description = ese_item_description
        self.ese_quantity = ese_quantity
        self.ese_item_weight = ese_item_weight
        self.ese_total_value = ese_total_value
        self.ese_item_details = ese_item_details
        self.ese_shipper_contactname = ese_shipper_contactname
        self.ese_shipper_company = ese_shipper_company
        self.ese_shipper_addr1 = ese_shipper_addr1
        self.ese_shipper_town = ese_shipper_town
        self.ese_shipper_state = ese_shipper_state
        self.ese_shipper_email = ese_shipper_email
        self.ese_shipper_phone = ese_shipper_phone
        self.ese_receiver_contactname = ese_receiver_contactname
        self.ese_receiver_company = ese_receiver_company
        self.ese_receiver_addr1 = ese_receiver_addr1
        self.ese_receiver_town = ese_receiver_town
        self.ese_receiver_state = ese_receiver_state
        self.ese_receiver_email = ese_receiver_email
        self.ese_receiver_phone = ese_receiver_phone
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
        self.driver = webdriver.Chrome(options=self.options,executable_path=resources.driverPath)
        self.baseUrl = resources.base_url
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

    def parcel_content_multiplegoods_singlereceiver(self):
        '''parcel_content'''
        browser = self.driver
        ese_item_description = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[6]
        ese_item_description.send_keys(str(self.ese_item_description))

        ese_quantity = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[7]
        ese_quantity.send_keys(int(self.ese_quantity))

        ese_item_weight = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[8]
        ese_item_weight.send_keys(self.ese_item_weight)

        ese_total_value = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[10]
        ese_total_value.send_keys(self.ese_total_value)

        # ese_brand = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[11]
        # ese_brand.send_keys(str(self.data[10]))

        # ese_model = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[12]
        # ese_model.send_keys(str(self.data[11]))

        ese_country_of_origin = browser.find_element_by_xpath('//*[@class="el-select-dropdown__item"][8]/span')
        browser.execute_script("arguments[0].click();", ese_country_of_origin)

        ese_item_details = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[12]
        ese_item_details.send_keys(str(self.ese_item_details))

        ese_copy_btn = browser.find_element_by_xpath('//*[@class="el-tooltip el-icon-document item"]')
        browser.execute_script("arguments[0].click();", ese_copy_btn)

        ese_item_description1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[13]
        ese_item_description1.clear()
        ese_item_description1.send_keys('iphone 12 plus')

        ese_total_value1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[17]
        ese_total_value1.clear()
        ese_total_value1.send_keys('1000')

        # ese_model1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[21]
        # ese_model1.clear()
        # ese_model1.send_keys('11x13x2')

        ese_singlereceiver_btn = browser.find_elements_by_xpath('//*[@class="el-button el-tooltip btn item el-button--success"]')[0]
        ese_singlereceiver_btn.click()
        time.sleep(5)

    def address(self):
        '''address'''
        browser = self.driver
        ese_shipper_contactname = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[2]
        ese_shipper_contactname.send_keys(str(self.ese_shipper_contactname))

        ese_shipper_company = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[3]
        ese_shipper_company.send_keys(str(self.ese_shipper_company))

        ese_shipper_addr1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[4]
        ese_shipper_addr1.send_keys(str(self.ese_shipper_addr1))

        ese_shipper_town = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[6]
        ese_shipper_town.send_keys(str(self.ese_shipper_town))

        ese_shipper_state = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[7]
        ese_shipper_state.send_keys(str(self.ese_shipper_state))

        ese_shipper_email = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[9]
        ese_shipper_email.send_keys(str(self.ese_shipper_email))

        ese_shipper_phone = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[10]
        ese_shipper_phone.send_keys(int(self.ese_shipper_phone))

        ese_receiver_contactname = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[11]
        ese_receiver_contactname.send_keys(str(self.ese_receiver_contactname))

        ese_receiver_company = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[12]
        ese_receiver_company.send_keys(str(self.ese_receiver_company))

        ese_receiver_addr1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[13]
        ese_receiver_addr1.send_keys(str(self.ese_receiver_addr1))

        ese_receiver_town = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[15]
        ese_receiver_town.send_keys(str(self.ese_receiver_town))

        ese_receiver_state = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[16]
        ese_receiver_state.send_keys(str(self.ese_receiver_state))

        ese_receiver_email = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[18]
        ese_receiver_email.send_keys(str(self.ese_receiver_email))

        ese_receiver_phone = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[19]
        ese_receiver_phone.send_keys(int(self.ese_receiver_phone))

        ese_address_next_btn = browser.find_elements_by_xpath('//*[@class="el-button next el-button--success"]')[0]
        ese_address_next_btn.click()
        time.sleep(5)

    def custom(self):
        '''custom'''
        browser = self.driver
        # ese_vat_status_btn = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[2]
        # ese_vat_status_btn.click()
        ese_vat_status_btn = browser.find_elements_by_xpath('//*[@class="el-select__caret el-input__icon el-icon-arrow-up"]')[0]
        browser.execute_script("arguments[0].click();", ese_vat_status_btn)

        ese_vat_status_value = browser.find_elements_by_xpath('//*[@class="el-scrollbar__view el-select-dropdown__list"][1]/li/span')[0]
        browser.execute_script("arguments[0].click();", ese_vat_status_value)

        # ese_export_reason_btn = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[3]
        # ese_export_reason_btn.click()
        ese_export_reason_btn = browser.find_elements_by_xpath('//*[@class="el-select__caret el-input__icon el-icon-arrow-up"]')[0]
        browser.execute_script("arguments[0].click();", ese_export_reason_btn)
        ese_export_reason_value = browser.find_elements_by_xpath('//*[@class="el-scrollbar__view el-select-dropdown__list"][1]/li/span')[0]
        browser.execute_script("arguments[0].click();", ese_export_reason_value)

        ese_custom_next_btn = browser.find_elements_by_xpath('//*[@class="el-button next el-button--success"]')[0]
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
        self.parcel_content_multiplegoods_singlereceiver()
        self.address()
        self.custom()
        self.order()
        self.pay()
        self.printDetail()
if __name__ == "__main__":
    unittest.main(verbosity=2)
