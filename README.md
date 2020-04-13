# ESE项目自动化测试脚本

## 简介

此工程为ESE项目的前端功能性自动化测试脚本

## 应用目的

1. 减少部分功能性人工测试
2. 提高测试效率
3. 降低回归测试的复杂度和重复性
   
## 核心技术框架

- 开发语言：Python 3.7
- 自动化测试框架：selenium 3
- 单元测试组件：unittest2
- excel操作组件：xlrd

## 工程结构
- case 测试用例模板目录，测试用例命名规则: 项目名_case_测试用例序号 
    - ese_case1.py 英国至非中国多商品单一收货人匿名下单
    - ese_case3.py 英国至非中国多商品单一收货人登录后下单
    - ese_case4.py 英国至非中国MY PARCELS OVERVIEW
    - ese_case5.py 英国至非中国用户注册
    - ese_case6.py 英国至非中国忘记密码+重置密码
- dist 打包后的可执行文件及依赖目录
    - run_all\run_all.exe 打包后的可执行文件
- driver 浏览器驱动存放目录
- report 测试报告生成目录
    - shots 截图目录
- resources 系统资源目录
    - _init_.py 系统初始化加载的配置类
- testFile 测试用例业务数据文件目录
    - test_data.xlsx 业务数据文件
- until 系统工具类目录
- venv 系统环境和依赖目录
- run_all.py 程序主入口类

## 操作说明
### 开发环境配置
1. windows7 以上
2. python 3.7 以上
下载地址：https://www.python.org/downloads/windows/
3. 配置Python环境变量
4. PyCharm 2019.3.3 [Community] 版本以上
下载地址：https://www.jetbrains.com/pycharm/download/#section=windows
5. Pycharm clone 源码：[VCS]-[Get From Version Control]-填入clone地址
6. 配置Python 解释器 [File]-[Settings]-[Project Interpreter]-[齿轮图标]-[Add]
    - [Base Interpreter]选择本机Python.exe所在目录
    - [Location] 选择clone下来的工程venv目录，如果没有此目录请手动创建，如果目录下已经有任何文件请手动删除
7. Pycharm 配置环境组件[File]-[Settings]-[Project Interpreter]-[+图标] 搜索并安装如下插件：
    - HTMLTestRunner-Python3
    - ParamUnittest
    - selenium
    - xlrd
    - unittest2
8. 右键run_all.py 并运行

### 快速运行
1. 操作系统：windows 7 以上
2. Python解释器：Python 3.7 以上
下载地址：https://www.python.org/downloads/windows/
3. 配置Python环境变量
4. clone源码到本地任意目录, 比如：C:\ese
5. 进入本地目录C:\ese\resources,记事本打开_init_.py编辑配置文件
    - 将proDir 的值修改为本地工程根目录, 比如：C:\ese
    - tester 为测试报告中显示的测试人员姓名，可以根据情况修改
    - Smtp 开头的参数为发送测试报告的邮件服务器配置，可以根据情况修改，其中Smtp_Receiver和Smtp_Receiver_pre 支持多个邮箱，多个邮箱之间用,分隔
6. 配置完成后在C:\ese\testFile\test_data.xlsx 表格中录入测试数据并保存
7. 进入C:\ese\dist\run_all, 双击run_all.exe运行所有测试用例即可

### 快速体验
请使用远程桌面登录内网测试服务器
- 地址:192.168.100.66
- 用户名: test
- 密码: Ecms.2020
- 进入F:\project\ese_auto_test\dist\run_all
- 双击 run_all.exe 

## 特别说明
如果需要修改源码，请每次提交创建新的分支，分支测试通过后请申请分支合并主干请求，等待管理员审核后才能合并

## 维护人员

姓名：宋士恩  

电话：13512490903

邮箱：songshien@ecmsglobal.com


