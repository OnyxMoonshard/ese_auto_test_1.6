# coding=utf-8
import time
import unittest


class PublicCase3_1(unittest.TestCase):

        def parcel_details_single(self,ese_item_name,ese_item_weight,ese_item_quantity,ese_unit_value,
                                           ese_item_details):
                '''填写信息，复制sku,修改内件名称与内件详情'''
                browser = self.driver
                ese_item_name1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[1]
                ese_item_name1.send_keys(str(ese_item_name))

                ese_item_weight1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[2]
                ese_item_weight1.send_keys(str(ese_item_weight))

                ese_item_quantity1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[3]
                ese_item_quantity1.send_keys(int(ese_item_quantity))

                ese_unit_value1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[5]
                ese_unit_value1.send_keys(str(ese_unit_value))

                ese_item_details1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[6]
                ese_item_details1.send_keys(str(ese_item_details))

                ese_country_of_origin = browser.find_element_by_xpath('//*[@class="el-select-dropdown__item"][8]/span')
                browser.execute_script("arguments[0].click();", ese_country_of_origin)

                ese_promise  = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/div/div/div[1]/label/span[1]')
                ese_promise.click()

                ese_read_agree = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/div/div/div[2]/label/span[1]')
                ese_read_agree.click()

                ese_next = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/div/button[2]/span')
                ese_next.click()
                time.sleep(5)

