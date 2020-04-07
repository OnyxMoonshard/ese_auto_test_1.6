import os
import time
import unittest
import baseinfo
import threading


from until import common
from until import getDir
from HTMLTestReportCN import HTMLTestRunner

proDir = getDir.proDir
now = time.strftime("%Y_%m_%d_%H%M%S")

def send_report_by_email(path,filename,result):
    mail = common.send_Mail(path,filename, result)

    print(mail)
    if mail:
        print(u"邮件发送成功！")
    else:
        print(u"邮件发送失败！")


if __name__ == "__main__":

    # setting report dir
    ReportDir = os.path.join(proDir,baseinfo.test_report )

    # setting case dir
    CaseDir = os.path.join(proDir, baseinfo.case_dir)

    # search test case
    discover = unittest.defaultTestLoader.discover(start_dir=CaseDir, pattern="ese_case*.py")

    # setting report fileName
    fileName = "ESETestReport_%s.html" % now
    fp = open(os.path.join(ReportDir, fileName), 'wb')

    runner = HTMLTestRunner(stream=fp,
                            title="ESETestReport",
                            description="",
                            tester="song",
                            verbosity=2)

    result = runner.run(discover)

    fp.close()

    time.sleep(10)


    #todo 测试报告邮件提醒
    t = threading.Thread(target=send_report_by_email,args=(ReportDir,fileName,result))
    t.start()



