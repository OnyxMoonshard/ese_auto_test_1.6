# coding=utf-8
import time
import unittest
import time

class PublicCase6_1(unittest.TestCase):

    def paymentoptions_usuk(self,ese_pay_cardno,ese_pay_youxiaoqi,ese_pay_cvc,ese_pay_postcode):
        '''US、UK、支付'''
        browser = self.driver
        # iframe = browser.find_elements_by_tag_name('iframe')[0]
        # browser.switch_to.frame(iframe)

        browser.switch_to.frame("myFrame")

        # WebDriverWait(browser, 50, 0.5).until(EC.presence_of_element_located((By.NAME, 'cardnumber')))
        '''
        ese_pay_cardno = browser.find_element_by_xpath( '//input[@class="InputElement is-empty Input Input--empty"and @name="cardnumber"]')
        ese_pay_cardno.send_keys(int(self.ese_pay_cardno))



        ese_pay_cardno = browser.find_element_by_xpath('//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input')
        ese_pay_cardno.send_keys(int(self.ese_pay_cardno))
        time.sleep(5)
        ese_pay_youxiaoqi = browser.find_element_by_xpath('//*[@id="root"]/form/div/div[2]/span[2]/span/span/input')
        ese_pay_youxiaoqi.send_keys(int(self.ese_pay_youxiaoqi))
        time.sleep(5)
        ese_pay_cvc = browser.find_element_by_xpath('//*[@id="root"]/form/div/div[2]/span[3]/span/span/input')
        ese_pay_cvc.send_keys(int(self.ese_pay_cvc))
        time.sleep(5)
        ese_pay_postcode = browser.find_element_by_xpath('//*[@id="root"]/form/div/div[2]/span[4]/span/span/input')
        ese_pay_postcode.send_keys(int(self.ese_pay_postcode))

        '''

        ese_pay_cardno1 = browser.find_element_by_name('cardnumber')
        ese_pay_cardno1.send_keys(int(ese_pay_cardno))
        time.sleep(5)
        ese_pay_youxiaoqi1 = browser.find_element_by_name('exp-date')
        ese_pay_youxiaoqi1.send_keys(int(ese_pay_youxiaoqi))

        ese_pay_cvc1 = browser.find_element_by_name('cvc')
        ese_pay_cvc1.send_keys(int(ese_pay_cvc))
        time.sleep(5)
        ese_pay_postcode1 = browser.find_element_by_name('postal')
        ese_pay_postcode1.send_keys(int(ese_pay_postcode))



        browser.switch_to.default_content()
        ese_pay_pay_btn = browser.find_elements_by_xpath('//*[@class="pay-with-stripe"]')[0]
        ese_pay_pay_btn.click()

        time.sleep(20)
