# coding=utf-8
import time
import unittest


class PublicCase3_2(unittest.TestCase):

    def aDDRESSDETAILS_CN_WAREHOUSE_NONLOGIN(self,ese_shipper_contactname,ese_shipper_company,ese_shipper_addr1,
                        ese_shipper_addr2,ese_shipper_city,ese_shipper_state,ese_shipper_zipcode,ese_shipper_email,
                        ese_shipper_phone,ese_receiver_contactname,ese_receiver_company,ese_receiver_addr1,ese_receiver_addr2,
                        ese_receiver_city,ese_receiver_district,ese_receiver_provnice,ese_receiver_zipcode,ese_receiver_email,
                        ese_receiver_phone):
        '''到中国、未登录、Warehouse'''
        browser = self.driver
        # ese_shipper_contactname1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[1]
        ese_shipper_contactname1 = browser.find_element_by_xpath('//*[@placeholder="Full Name"]')
        ese_shipper_contactname1.send_keys(str(ese_shipper_contactname))
        time.sleep(2)
        ese_shipper_company1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[2]
        ese_shipper_company1.send_keys(str(ese_shipper_company))
        time.sleep(2)
        ese_shipper_addr11 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[3]
        ese_shipper_addr11.send_keys(str(ese_shipper_addr1))
        time.sleep(2)
        ese_shipper_addr22 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[4]
        ese_shipper_addr22.send_keys(str(ese_shipper_addr2))
        time.sleep(2)
        ese_shipper_city1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[5]
        ese_shipper_city1.send_keys(str(ese_shipper_city))
        time.sleep(2)
        ese_shipper_state1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[6]
        ese_shipper_state1.send_keys(str(ese_shipper_state))
        time.sleep(2)
        ese_shipper_state1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[7]
        ese_shipper_state1.send_keys(str(ese_shipper_zipcode))
        time.sleep(2)
        ese_shipper_email1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[8]
        ese_shipper_email1.send_keys(str(ese_shipper_email))
        time.sleep(2)
        ese_shipper_phone1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[9]
        ese_shipper_phone1.send_keys(int(ese_shipper_phone))
        time.sleep(2)
        ese_receiver_contactname1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[10]
        ese_receiver_contactname1.send_keys(str(ese_receiver_contactname))
        time.sleep(2)
        ese_receiver_company1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[11]
        ese_receiver_company1.send_keys(str(ese_receiver_company))
        time.sleep(2)
        ese_receiver_addr11 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[12]
        ese_receiver_addr11.send_keys(str(ese_receiver_addr1))
        time.sleep(2)
        ese_receiver_addr22 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[13]
        ese_receiver_addr22.send_keys(str(ese_receiver_addr2))
        time.sleep(2)
        ese_receiver_city1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[14]
        ese_receiver_city1.send_keys(str(ese_receiver_city))
        time.sleep(2)
        ese_receiver_district1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[15]
        ese_receiver_district1.send_keys(str(ese_receiver_district))
        time.sleep(2)
        ese_receiver_district1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[16]
        ese_receiver_district1.send_keys(str(ese_receiver_provnice))
        time.sleep(2)
        ese_receiver_district1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[17]
        ese_receiver_district1.send_keys(str(ese_receiver_zipcode))
        time.sleep(2)
        ese_receiver_email1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[18]
        ese_receiver_email1.send_keys(str(ese_receiver_email))
        time.sleep(2)
        ese_receiver_phone1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[19]
        ese_receiver_phone1.send_keys(int(ese_receiver_phone))
        time.sleep(2)
        ese_address_next_btn = browser.find_elements_by_xpath('//*[@class="el-button fr el-button--success"]')[0]
        ese_address_next_btn.click()
        time.sleep(5)
