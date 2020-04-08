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
- pending 正在调试中测试用例目录
- report 测试报告生成目录
    - shots 截图目录
- resources 系统资源目录
    - _init_.py 系统初始化加载的配置类
- testFile 测试用例业务数据文件目录
    - test_data.xlsx 业务数据文件
- until 系统工具类目录
- venv 系统环境和依赖目录
- run_all.py 工程入口类

## 操作说明
1. windows7 以上
2. python 3.7 以上
下载地址：https://www.python.org/downloads/windows/
3. 配置Python环境变量
4. PyCharm 2019.3.3 [Community] 版本以上
下载地址：https://www.jetbrains.com/pycharm/download/#section=windows
5. Pycharm clone 源码：[VCS]-[Get From Version Control]-填入clone地址
6. 配置Python 解释器 [File]-[Settings]-[Project Interpreter]-[齿轮图标]-[Add]
    - [Base Interpreter]选择本机Python.exe所在目录
    - [Location] 选择clone下来的工程venv目录
7. Pycharm 配置环境组件[File]-[Settings]-[Project Interpreter]-[+图标] 搜索并安装如下插件：
    - HTMLTestRunner-Python3
    - ParamUnittest
    - selenium
    - xlrd
    - unittest2
8. 右键run_all.py 并运行

## 特别说明
如果需要修改源码，请每次提交创建新的分支，分支测试通过后请申请分支合并主干请求，等待管理员审核后才能合并
## 维护人员

姓名：宋士恩  

电话：13512490903

邮箱：songshien@ecmsglobal.com


