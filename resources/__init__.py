#-*-coding:utf-8-*-
#测试用例配置参数

base_url = "http://106.39.97.90:17885/#/tools/uk/1"

# 项目根目录
proDir = "F:/project/ese_auto_test"

# 驱动目录
driverPath=proDir+"\driver\chromedriver.exe"

#测试报告头描述
description = ""
#测试报告测试人员
tester = "auto_test"

#发送邮件配置参数
Smtp_Server = 'smtp.qiye.163.com'
Smtp_Sender = 'jenkins@ecmsglobal.com'
Smtp_Sender_Password = 'Ecms@2019xx'
#Smtp_Receiver = ['[songshien@ecmsglobal.com]','[liuyi@ecmsglobal.com]','[shiht@ecmsglobal.com]']
Smtp_Receiver = ['auto_test@ecmsglobal.com']
Smtp_Receiver_pre = ['']

#测试邮箱配置
#Smtp_Server = ‘smtp.163.com‘
#Smtp_Sender = ‘[email protected]‘
#Smtp_Sender_Password = ‘Password‘
#Smtp_Receiver = [‘[email protected]‘]
#Smtp_Receiver_pre = [‘[email protected]‘]

#测试用例及报告路径配置参数
case_dir = "case"
test_report = "report"

#测试用例及报告路径配置参数
# test_dir = ‘D:\\WorkSpace\\Python\\UiTest\\test_case‘
# test_report = ‘D:\\WorkSpace\\Python\\UiTest\\test_report\\‘