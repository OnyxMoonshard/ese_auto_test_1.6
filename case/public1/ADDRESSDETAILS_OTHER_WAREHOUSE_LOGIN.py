# coding=utf-8
import time
import unittest
from selenium.webdriver import ActionChains

class PublicCase2_4(unittest.TestCase):

    def addressdetails_other_warehouse_login(self, ese_shipper_contactname, ese_shipper_company, ese_shipper_addr1,
                                                ese_shipper_addr2, ese_shipper_city, ese_shipper_state,
                                                ese_shipper_zipcode, ese_shipper_email,
                                                ese_shipper_phone, ese_receiver_contactname, ese_receiver_company,
                                                ese_receiver_addr1, ese_receiver_addr2,
                                                ese_receiver_city, ese_receiver_district, ese_receiver_provnice,
                                                ese_receiver_zipcode, ese_receiver_email,
                                                ese_receiver_phone):
        '''到中国、登录、Warehouse'''
        browser = self.driver

        #悬停到MyAccount
        #登录
        # ese_my_account = browser.find_elements_by_xpath('//*[@class="txt"]')[1]
        ese_my_account = browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/div/div/div[3]/span')
        actions = ActionChains(browser)
        actions.move_to_element(ese_my_account).perform()
        time.sleep(5)

        # ese_sign_in = browser.find_elements_by_xpath('//*[@class="menu"]/li')[0]
        ese_sign_in = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[1]/div/div/div/div[4]/div')
        browser.execute_script("arguments[0].click();", ese_sign_in)
        time.sleep(50)

        ese_user_email = browser.find_element_by_xpath('//*[@placeholder="Enter your registered email"]')
        ese_user_email.send_keys('liuyi@ecmsglobal.com')
        time.sleep(5)
        ese_user_pwd = browser.find_element_by_xpath('//*[@placeholder="********"]')
        ese_user_pwd.send_keys('A123456789')
        time.sleep(5)

        # ese_rememberme = browser.find_elements_by_xpath('//*[@class="el-checkbox__inner"]')[1]
        # browser.execute_script("arguments[0].click();", ese_rememberme)
        ese_sign_in_btn = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/form/div[4]/button[1]/span')
        ese_sign_in_btn.click()

        time.sleep(50)











        ese_shipper_contactname1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[1]
        # ese_shipper_contactname1 = browser.find_element_by_xpath('//*[@placeholder="Full Name"]')
        ese_shipper_contactname1.send_keys(str(ese_shipper_contactname))

        ese_shipper_company1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[2]
        ese_shipper_company1.send_keys(str(ese_shipper_company))

        ese_shipper_zipcode1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[3]
        ese_shipper_zipcode1.clear()
        ese_shipper_zipcode1.send_keys(str(ese_shipper_zipcode))

        ese_shipper_addr11 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[4]
        ese_shipper_addr11.send_keys(str(ese_shipper_addr1))

        ese_shipper_addr22 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[5]
        ese_shipper_addr22.send_keys(str(ese_shipper_addr2))

        ese_shipper_city1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[6]
        ese_shipper_city1.send_keys(str(ese_shipper_city))

        ese_shipper_state1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[7]
        ese_shipper_state1.send_keys(str(ese_shipper_state))

        ese_shipper_email1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[8]
        ese_shipper_email1.send_keys(str(ese_shipper_email))

        ese_shipper_phone1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[9]
        ese_shipper_phone1.send_keys(int(ese_shipper_phone))

        ese_receiver_contactname1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[10]
        ese_receiver_contactname1.send_keys(str(ese_receiver_contactname))

        ese_receiver_company1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[11]
        ese_receiver_company1.send_keys(str(ese_receiver_company))

        ese_receiver_zipcode1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[12]
        ese_receiver_zipcode1.clear()
        ese_receiver_zipcode1.send_keys(str(ese_receiver_zipcode))

        ese_receiver_addr11 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[13]
        ese_receiver_addr11.send_keys(str(ese_receiver_addr1))

        ese_receiver_addr22 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[14]
        ese_receiver_addr22.send_keys(str(ese_receiver_addr2))

        ese_receiver_city1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[15]
        ese_receiver_city1.send_keys(str(ese_receiver_city))

        # ese_receiver_district1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[15]
        # ese_receiver_district1.send_keys(str(ese_receiver_district))

        ese_receiver_district1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[16]
        ese_receiver_district1.send_keys(str(ese_receiver_provnice))

        ese_receiver_email1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[17]
        ese_receiver_email1.send_keys(str(ese_receiver_email))

        ese_receiver_phone1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[18]
        ese_receiver_phone1.send_keys(int(ese_receiver_phone))

        ese_address_next_btn = browser.find_elements_by_xpath('//*[@class="el-button fr el-button--success"]')[0]
        ese_address_next_btn.click()
        time.sleep(5)
