import time
import unittest #导入单元测试包
from selenium.webdriver import ActionChains
from selenium import webdriver



# class ese_case2(unittest.TestCase):
class ese_case2():
    '''多商品多收货人匿名下单'''
    global browser
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0,
             "profile.default_content_setting_values.automatic_downloads": 1}

    options.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.get('http://106.39.97.90:17885/#/tools/uk/1')
    time.sleep(15)

    def index(self):
        '''首页'''
        ese_to = browser.find_elements_by_xpath('//*[@class="el-scrollbar__view el-select-dropdown__list"][1]/li/span')[2]
        browser.execute_script("arguments[0].click();", ese_to)
        ese_from_postcode = browser.find_element_by_id('areaStartPost')
        ese_from_postcode.send_keys('SL1 4PH')
        ese_to_postcode = browser.find_element_by_id('areaEndPost')
        ese_to_postcode.send_keys('123456')
        ese_weight = browser.find_element_by_id('grossWeight')
        ese_weight.send_keys('2')
        ese_length = browser.find_element_by_id('length')
        ese_length.send_keys('20')
        ese_weidth = browser.find_element_by_id('width')
        ese_weidth.send_keys(15)
        ese_height = browser.find_element_by_id('height')
        ese_height.send_keys('10')
        ese_quotenow = browser.find_element_by_id('submit')
        ese_quotenow.click()
        time.sleep(10)

    def parcel_content_multiplegoods_multiplereceiver(self):
        '''parcel_content'''
        ese_item_description = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[6]
        ese_item_description.send_keys('iphone 11 plus')

        ese_quantity = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[7]
        ese_quantity.send_keys('1')

        ese_weight = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[8]
        ese_weight.send_keys('1.2')

        ese_total_value = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[10]
        ese_total_value.send_keys('800')

        # ese_brand = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[11]
        # ese_brand.send_keys('iphone')

        # ese_model = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[12]
        # ese_model.send_keys('11x12x2')

        ese_country_of_origin = browser.find_element_by_xpath('//*[@class="el-select-dropdown__item"][10]/span')
        browser.execute_script("arguments[0].click();", ese_country_of_origin)

        ese_itemdetails = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[12]
        ese_itemdetails.send_keys('美版无锁4G')

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

        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=100000"
        browser.execute_script(js)

        ese_multiplereceiver_btn = browser.find_elements_by_xpath('//*[@class="el-button el-tooltip btn item el-button--success"]')[1]
        ese_multiplereceiver_btn.click()
        time.sleep(10)


    def address(self):
        '''address'''
        ese_shipper_contactname = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[2]
        ese_shipper_contactname.send_keys('宋士恩')

        ese_shipper_company = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[3]
        ese_shipper_company.send_keys('天津易客满国际物流有限公司英国分公司')

        ese_shipper_addr1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[4]
        ese_shipper_addr1.send_keys('145-66 228th Street, Unit 3  Springfield Gardens')

        ese_shipper_town = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[6]
        ese_shipper_town.send_keys('London')

        ese_shipper_state = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[7]
        ese_shipper_state.send_keys('London')

        ese_shipper_postcode = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[8]
        ese_shipper_postcode.send_keys('SL1 4PH')

        ese_shipper_email = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[9]
        ese_shipper_email.send_keys('songshien@ecmsglobal.com')

        ese_shipper_phone= browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[10]
        ese_shipper_phone.send_keys('13512490903')

        # 将滚动条移动到页面的中部
        js = "var q=document.documentElement.scrollTop=500"
        browser.execute_script(js)

        # 拖拽商品到包裹容器里
        # 起点
        item1_start = browser.find_elements_by_xpath('//*[@class="board-item"]')[0]
        print(item1_start.location)
        # 终点
        item1_end = browser.find_elements_by_xpath('//*[@class="board-item example"]')[0]
        print(item1_end.location)
        print(item1_end.location.get('x'))
        print(item1_end.location.get('y'))
        # 执行
        # 鼠标左键按下不放
        actions = ActionChains(browser)
        actions.drag_and_drop(item1_start,item1_end)
        actions.perform()

        time.sleep(10)

        ese_receiver_contactname = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[15]
        ese_receiver_contactname.send_keys('刘亿')

        ese_receiver_company = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[16]
        ese_receiver_company.send_keys('天津易客满国际物流有限公司北京分公司')

        ese_receiver_addr1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[17]
        ese_receiver_addr1.send_keys('北京市顺义区南法信镇 aclp大厦 南楼 w509')

        ese_receiver_town = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[19]
        ese_receiver_town.send_keys('北京市')

        ese_receiver_state = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[20]
        ese_receiver_state.send_keys('北京')

        ese_postcode = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[21]
        ese_postcode.send_keys('100000')

        ese_receiver_email = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[22]
        ese_receiver_email.send_keys('liuyi@ecmsglobal.com')

        ese_receiver_phone = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[23]
        ese_receiver_phone.send_keys('13512490903')

        ese_add_another_address_btn = browser.find_elements_by_xpath('//*[@class="el-icon-circle-plus-outline"]')[1]
        browser.execute_script("arguments[0].click();", ese_add_another_address_btn)

        ese_receiver_contactname2 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[28]
        ese_receiver_contactname2.send_keys('王于田')

        ese_receiver_company2 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[29]
        ese_receiver_company2.send_keys('天津易客满国际物流有限公司北京分公司')

        ese_receiver_addr12 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[30]
        ese_receiver_addr12.send_keys('北京市顺义区南法信镇 aclp大厦 南楼 w509')

        ese_receiver_town2 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[32]
        ese_receiver_town2.send_keys('北京市')

        ese_receiver_state2 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[33]
        ese_receiver_state2.send_keys('北京')

        ese_postcode2 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[34]
        ese_postcode2.send_keys('100000')

        ese_receiver_email2 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[35]
        ese_receiver_email2.send_keys('liuyi@ecmsglobal.com')

        ese_receiver_phone2 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[36]
        ese_receiver_phone2.send_keys('13512490903')

        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=10000"
        browser.execute_script(js)

        ese_address_next_btn = browser.find_elements_by_xpath('//*[@class="el-button next el-button--success"]')[0]
        ese_address_next_btn.click()
        time.sleep(5)

    def custom(self):
        '''custom'''
        ese_vat_status_btn = \
        browser.find_elements_by_xpath('//*[@class="el-select__caret el-input__icon el-icon-arrow-up"]')[0]
        browser.execute_script("arguments[0].click();", ese_vat_status_btn)

        ese_vat_status_value = \
        browser.find_elements_by_xpath('//*[@class="el-scrollbar__view el-select-dropdown__list"][1]/li/span')[0]
        browser.execute_script("arguments[0].click();", ese_vat_status_value)

        # ese_export_reason_btn = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[3]
        # ese_export_reason_btn.click()
        ese_export_reason_btn = \
        browser.find_elements_by_xpath('//*[@class="el-select__caret el-input__icon el-icon-arrow-up"]')[0]
        browser.execute_script("arguments[0].click();", ese_export_reason_btn)
        ese_export_reason_value = \
        browser.find_elements_by_xpath('//*[@class="el-scrollbar__view el-select-dropdown__list"][1]/li/span')[0]
        browser.execute_script("arguments[0].click();", ese_export_reason_value)

        ese_custom_next_btn = browser.find_elements_by_xpath('//*[@class="el-button next el-button--success"]')[0]
        ese_custom_next_btn.click()
        time.sleep(20)

    def order(self):
        '''order'''
        ese_order_checkbox = browser.find_elements_by_xpath('//*[@class="el-checkbox__original"]')
        for cb in ese_order_checkbox:
            browser.execute_script("arguments[0].click();", cb)

        ese_order_pay_btn = browser.find_element_by_xpath('//*[@class="btn-group el-row"]/div/button')
        ese_order_pay_btn.click()
        time.sleep(20)
    def pay(self):
        '''pay'''
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
        ese_print_downloaddoc = browser.find_element_by_xpath('//*[@class="el-row"][1]/button')
        ese_print_downloaddoc.click()

        ese_print_download = \
            browser.find_elements_by_xpath('//*[@class="el-button el-button--success el-button--small"]')[0]
        ese_print_download.click()

        time.sleep(10)

        # success_msg = browser.find_element_by_xpath('//*[@class="find_elements_by_xpath"]').text
        # self.assertEqual(success_msg, self.ese_successful)

    if __name__ == '__main__':
        index("index")
        parcel_content_multiplegoods_multiplereceiver("parcel_content_multiplegoods_multiplereceiver")
        address("address")
        # custom()
        # order()
        # pay()
        # printDetail()
