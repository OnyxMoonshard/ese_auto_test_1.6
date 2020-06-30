# coding=utf-8
import time
import unittest


class PublicCase4(unittest.TestCase):

        def parcel_details_multiply(self,ese_item_name,ese_item_weight,ese_item_quantity,ese_unit_value,
                                           ese_item_details):
                '''填写信息，复制sku,修改内件名称与内件详情'''
                browser = self.driver
                ese_item_name1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[1]
                ese_item_name1.send_keys(str(ese_item_name))

                ese_item_weight1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[2]
                ese_item_weight1.send_keys(str(ese_item_weight))

                ese_item_quantity1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[3]
                ese_item_quantity1.send_keys(int(ese_item_quantity))
                time.sleep(3)

                ese_unit_value1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[5]
                ese_unit_value1.send_keys(str(ese_unit_value))
                time.sleep(3)

                ese_item_details1 = browser.find_elements_by_xpath('//*[@class="el-input__inner"]')[6]
                ese_item_details1.send_keys(str(ese_item_details))
                time.sleep(3)

                ese_country_of_origin = browser.find_element_by_xpath('//*[@class="el-select-dropdown__item"][8]/span')
                browser.execute_script("arguments[0].click();", ese_country_of_origin)
                time.sleep(3)

                ese_copy_btn = browser.find_element_by_xpath('//*[@class="el-tooltip el-icon-document item"]')
                browser.execute_script("arguments[0].click();", ese_copy_btn)
                time.sleep(3)

                ese_item_name2 = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/form/div[2]/div[1]/div[1]/div/div[1]/input')
                ese_item_name2.clear()
                ese_item_name2.send_keys('DEVIL MAY CAY5')

                ese_item_details2 = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/form/div[2]/div[2]/div[1]/div/div/input')
                ese_item_details2.clear()
                ese_item_details2.send_keys('HD Collection ')
                time.sleep(3)

                ese_promise  = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/div/div/div[1]/label/span[1]')
                ese_promise.click()
                time.sleep(3)

                ese_read_agree = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/div/div/div[2]/label/span[1]')
                ese_read_agree.click()
                time.sleep(3)

                ese_next = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/div/button[2]/span')
                ese_next.click()
                time.sleep(5)

