import os
import time
import unittest  # 导入单元测试包

import paramunittest
from selenium import webdriver
from selenium.webdriver import ActionChains

import resources
from until import getDir
from until.common import get_excel_value

# proDir = getDir.proDir
now = time.strftime("%Y_%m_%d %H:%M:%S")
case6 = get_excel_value("test_data.xlsx", "case6")


@paramunittest.parametrized(*case6)
class EseCase6(unittest.TestCase):
    '''英国至非中国忘记密码+重置密码'''
    def setParameters(self, case_name, ese_from_postcode, ese_to_postcode, ese_weight, ese_length, ese_width,
                      ese_height,email,password,confirmpassword,reset_org_password,reset_new_password,reset_confirm_password, ese_successful ):
        """
        从 excel 中获取用例
        :param case_name: 用例名称
        :param ese_from_postcode: 发货人邮编
        :param ese_to_postcode: 收货人邮编
        :param ese_weight: 总重量
        :param ese_length: 总长度
        :param ese_width: 总宽度
        :param ese_height: 总高度
        :param email: 邮箱
        :param password: 密码
        :param confirmpassword: 确认密码
        :param reset_org_password: 重置密码中的原始密码
        :param reset_new_password: 重置密码中的新密码
        :param reset_confirm_password: 重置密码中的确认密码
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
        self.email = email
        self.password = password
        self.confirmpassword = confirmpassword
        self.reset_org_password = reset_org_password
        self.reset_new_password = reset_new_password
        self.reset_confirm_password = reset_confirm_password
        self.ese_successful = ese_successful

    def setUp(self):
        self._testMethodDoc = "</br>英国至非中国忘记密码+重置密码:</br>" + self.case_name  # 设置用例名称
        self.options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 "profile.default_content_setting_values.automatic_downloads": 1}

        self.options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(options=self.options)
        # self.driver.delete_all_cookies()
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

    def find_password(self):
        '''find password'''
        browser = self.driver
        # 悬停到MyAccount
        # 登录
        ese_my_account = browser.find_elements_by_xpath('//*[@class="txt"]')[1]
        if(str(ese_my_account.text).__eq__('MY PARCELS')):
            ese_my_account = browser.find_elements_by_xpath('//*[@class="txt"]')[2]
        actions = ActionChains(browser)
        actions.move_to_element(ese_my_account).perform()
        time.sleep(10)
        ese_loginout = browser.find_elements_by_xpath('//*[@class="menu"]/li')[0]
        if(str(ese_loginout.text).__eq__('Login Out')):
            browser.execute_script("arguments[0].click();", ese_loginout)
            actions.move_to_element(ese_my_account).perform()
            time.sleep(5)
            ese_signin = browser.find_elements_by_xpath('//*[@class="menu"]/li')[0]
            browser.execute_script("arguments[0].click();", ese_signin)
        else:
            browser.execute_script("arguments[0].click();", ese_loginout)
        time.sleep(5)
        ese_forgetpassword = browser.find_element_by_xpath('//*[@class="forget-password"]')
        browser.execute_script("arguments[0].click();", ese_forgetpassword)
        # if(str(self.gender).__eq__('Ms.')):
        #     gender = browser.find_elements_by_xpath('//*[@class="el-scrollbar__view el-select-dropdown__list"][1]/li')[1]
        #     browser.execute_script("arguments[0].click();", gender)
        email = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[15]
        email.send_keys(str(self.email))

        password = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[17]
        password.send_keys(str(self.password))
        confirmpassword = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[18]
        confirmpassword.send_keys(str(self.confirmpassword))
        ese_getcaptcha_btn = browser.find_elements_by_xpath('//*[@class="el-button el-button--primary"]')[1]
        ese_getcaptcha_btn.click()
        time.sleep(60)
        ese_confirm_btn = browser.find_elements_by_xpath('//*[@class="el-button el-button--primary"]')[2]
        ese_confirm_btn.click()
        time.sleep(10)
        #关闭登录框
        ese_signinclose_btn = browser.find_elements_by_xpath('//*[@class="el-dialog__close el-icon el-icon-close"]')[4]
        browser.execute_script("arguments[0].click();", ese_signinclose_btn)
        time.sleep(5)
        ese_my_account = browser.find_elements_by_xpath('//*[@class="txt"]')[1]
        if (str(ese_my_account.text).__eq__('MY PARCELS')):
            ese_my_account = browser.find_elements_by_xpath('//*[@class="txt"]')[2]
        actions = ActionChains(browser)
        actions.move_to_element(ese_my_account).perform()
        time.sleep(5)
        ese_signin = browser.find_elements_by_xpath('//*[@class="menu"]/li')[0]
        browser.execute_script("arguments[0].click();", ese_signin)
        # 登录
        denglu_email = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[13]
        denglu_email.send_keys(self.email)
        denglu_password = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[14]
        denglu_password.send_keys(self.password)
        denglu_singin_btn = browser.find_elements_by_xpath('//*[@class="el-button el-button--success"]')[1]
        denglu_singin_btn.click()
        time.sleep(5)

    def reset_password(self):
        browser = self.driver
        # 悬停到MyAccount
        # 登录
        ese_my_account = browser.find_elements_by_xpath('//*[@class="txt"]')[1]
        if (str(ese_my_account.text).__eq__('MY PARCELS')):
            ese_my_account = browser.find_elements_by_xpath('//*[@class="txt"]')[2]
        actions = ActionChains(browser)
        actions.move_to_element(ese_my_account).perform()
        time.sleep(10)

        ese_reset = browser.find_elements_by_xpath('//*[@class="menu"]/li')[1]
        browser.execute_script("arguments[0].click();", ese_reset)
        time.sleep(5)

        org_password = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[15]
        org_password.send_keys(str(self.reset_org_password))
        reset_new_password = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[16]
        reset_new_password.send_keys(str(self.reset_new_password))
        reset_confirm_password = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[17]
        reset_confirm_password.send_keys(str(self.reset_confirm_password))
        reset_reset_btn = browser.find_elements_by_xpath('//*[@class="el-button sign-up el-button--success"]')[1]
        reset_reset_btn.click()

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
        self.get_screenshot()
        browser.close()
        browser.quit()

    def test_main(self):
        self.index()
        self.find_password()
        self.reset_password()

if __name__ == "__main__":
    unittest.main(verbosity=2)



