# coding:utf-8
import time
from appium import webdriver
import  unittest
import  paramunittest
from Common import ExcelProcess
from Common import getProperity
from Common import  get_current_dir
import os
from PO.base_page import Base

#读取用例目录，属性目录
module_name = "tutor\\test_login.py"
cur_path =  os.path.abspath(module_name)
case_path = get_current_dir.get_case_dir(cur_path)
property_path = get_current_dir.get_properity_dir(cur_path)

#读取登录用例的相应列
login_case = ExcelProcess.get_execute_case_bycol(case_path)
col2 = login_case[3]
col3 = login_case[4]
col8 = login_case[8]
col10 = login_case[10]

#对登录数据进行参数化，逐行执行每条用例
parameters = zip(col2,col3,col8,col10)
@paramunittest.parametrized(*parameters)
class TestLogin(unittest.TestCase):
    def setParameters(self,login_name, password, expected_xpath, expected_result):
        self.login_name = login_name
        self.password = password
        self.expected_xpath = expected_xpath
        self.expected_result = expected_result

    
    #获取登录页面各元素控件的id
    def setUp(self):
        global property_path
        d = getPrperity.getProperity(property_path)
        self.loginname_id = d.get("loginname")
        self.password_id = d.get("password")
        self.submit_id = d.get("submit")
        self.base = Base()


# WebDriverWait(driver, 20).until(lambda the_driver: the_driver.find_element_by_id("com.strong.leke.student:id/tv_login").is_displayed())
    def testDown(self):
        time.sleep(10)
        self.base.quit_driver()
    
    #登录页面测试
    def test_login(self):
        self.base.send_keys_txt(self.loginname_id, self.login_name)
        self.base.send_keys_txt(self.password_id, self.password)
        self.base.click(self.submit_id)
        result = self.base.get_element_txt(self.expected_xpath)

        time.sleep(50)
        self.assertEqual(result, self.expected_result)








