# !/usr/bin/python3

"""
FileName    : common.py
Author      : ken
Date        : 2018-04-21
Describe    : common method for test
"""

import os
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import resources

import xlrd
from selenium import webdriver

from until import getDir


proDir = resources.proDir


class PyExcel:
    """Use the given excel_name and sheet_name, sheet_value, write excel and read excel.
        1. write_excel
        2. read_excel
    """
    TestFile = os.path.join(proDir, "testFile")
    suffix = ".xlsx"

    def __init__(self, excel_name, sheet_name=None, sheet_value=None):
        """
        initialization parameter
        :param excel_name: The file suffix must be "xls"
        :param sheet_name: set the workbook's sheetName
        :param sheet_value: The type of object must be "list" or "tuple"
        """
        self.excel_name = excel_name
        self.sheet_name = sheet_name
        self.sheet_value = sheet_value



        if not str(self.excel_name).endswith(self.suffix):
            raise Exception('%s suffix is not "%s"' %
                            (self.excel_name, self.suffix))
        self.EXCEL_PATH = os.path.join(self.TestFile, self.excel_name)

        if self.sheet_value is not None:
            try:
                if isinstance(self.sheet_value, list) or isinstance(self.sheet_value, tuple):
                    for i in range(len(self.sheet_value)):
                        assert isinstance(self.sheet_value[i], list)
            except TypeError as e:
                self.logger.error(e, exc_info=True)
                print(e)

    # def write_excel(self):
    #     if self.sheet_name is not None:
    #         wb = xlwt.Workbook()
    #         sheet = wb.add_sheet(self.sheet_name)
    #
    #         for i in range(len(self.sheet_value)):
    #             for j in range(len(self.sheet_value[i])):
    #                 sheet.write(i, j, self.sheet_value[i][j])
    #
    #         wb.save(self.EXCEL_PATH)
    #         print("write date success!")
    #     else:
    #         return False

    def read_excel(self):
        workbook = xlrd.open_workbook(self.EXCEL_PATH)
        if self.sheet_name:
            work_sheet = workbook.sheet_by_name(self.sheet_name)
        else:
            work_sheet = workbook.sheet_by_index(0)

        for i in range(work_sheet.nrows):
            for j in range(work_sheet.ncols):
                print(work_sheet.cell_value(i, j), "\t", end="")
            print()


def get_excel_value(excel_name, sheet_name):
    """
    get excel value by given excel_name and sheet_name
    :param excel_name:
    :param sheet_name:
    :return: cls
    """
    cls = []
    excel_path = os.path.join(proDir, "testFile", excel_name)
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name(sheet_name)
    nrows = sheet.nrows

    for i in range(nrows):
        if sheet.row_values(i)[0] != "case_name":
            cls.append(sheet.row_values(i))
    return cls


def get_NewReport(testreport):
    #获取testreport 目录下的文件返回一个list
    dirs = os.listdir(testreport)
    #对文件list 进行排序 进行增序排列
    dirs.sort()
    #获取序列最后一个元素，即最大的一个元素。
    newreportname = dirs[-1]
    print('The new report name: {0}'.format(newreportname))
    file_new = os.path.join(testreport, newreportname)
    print(file_new)
    return file_new

def get_Result(filename):
    driver = webdriver.Chrome()
    driver.maximize_window()
    ##得到测试报告路径
    result_url = "file://%s" % filename
    driver.get(result_url)
    time.sleep(5)

    result = driver.find_element_by_xpath("html/body/div[1]/p[3]").text

    result = result.split(':')
    print  (result)
    driver.quit()
    return  result[-1]

def send_Mail(path,file_new,result):
    f = open(path+"/"+file_new, 'rb')
    # 读取测试报告正文
    mail_body = f.read()
    f.close()
    try:
        smtp = smtplib.SMTP(resources.Smtp_Server, 25)
        sender = resources.Smtp_Sender
        password = resources.Smtp_Sender_Password
        receiver = resources.Smtp_Receiver
        smtp.login(sender, password)
        msg = MIMEMultipart()
        # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
        # 发送正文
        text = MIMEText(mail_body, 'html', 'utf-8')
        # 定义邮件正文标题
        text['Subject'] = Header('ESETestReport', 'utf-8')
        msg.attach(text)
        # 发送附件
        # Header()用于定义邮件主题，主题加上时间，是为了防止主题重复，主题重复，发送太过频繁，邮件会发送不出去。
        msg['Subject'] = Header('[执行结果：' + str(result) + ']:'+ file_new, 'utf-8')
        msg_file = MIMEText(mail_body, 'html', 'utf-8')
        msg_file['Content-Type'] = 'application/octet-stream'
        msg_file["Content-Disposition"] = 'attachment; filename='+file_new
        msg.attach(msg_file)
        # 定义发件人，如果不写，发件人为空
        msg['From'] = sender
        # 定义收件人，如果不写，收件人为空
        msg['To'] = ",".join(receiver)
        tmp = smtp.sendmail(sender, receiver, msg.as_string())
        print (tmp)
        smtp.quit()
        return True
    except smtplib.SMTPException as e:
        print(str(e))
        return False


# if __name__ == "__main__":
    # value = (
    #     ["case_name", "username", "password", "excepted"],
#     #     ["用户名正确，密码错误", "qiutiandeyanjin@163.com", "efg", "用户名或密码不正确"],
#     #     ["有用户名没有密码", "qiutiandeyanjin@163.com", "", "请输入密码"],
#     #     ["没有用户名有密码", "", "efg", "请输入帐号"]
#     # )
#     # excel = PyExcel(excel_name="loginCase.xls", sheet_name="login_test", sheet_value=value)
#     # excel.write_excel()
#     # excel.read_excel()
#     # test = get_excel_value(excel_name="loginCase.xls", sheet_name="login_test")
#     # print(test)