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

#获取用例目录及属性目录
module_name = "mall\\goods_list.py"
cur_path =  os.path.abspath(module_name)
case_path = get_current_dir.get_case_dir(cur_path)
property_path = get_current_dir.get_properity_dir(cur_path)

#读取用例，获取相应列的内容
case_xml = ExcelProcess.get_execute_case_bycol(case_path)
col2 = case_xml[3]
col3 = case_xml[4]
col8 = case_xml[8]
col10 = case_xml[10]

#参数化相应列，使得可以逐行执行用例，测试“我的商城”按钮
parameters = zip(col2,col3,col8,col10)
@paramunittest.parametrized(*parameters)
class TestGoodsList(unittest.TestCase):
    #参数化设置，登录名，密码，期望控件的xpath和期望控件的结果
    def setParameters(self,login_name, password, expected_xpath, expected_result):
        self.login_name = login_name
        self.password = password
        self.expected_xpath = expected_xpath
        self.expected_result = expected_result

    #获取元素属性
    def setUp(self):
        global property_path
        d = getProperity.getProperity(property_path)
        self.mall_btn_id = d.get("mall_button")
        self.base = Base()


    def testDown(self):
        time.sleep(10)
        self.base.quit_driver()


    def test_mall(self):
        #用户登录
        self.base.send_keys_txt("com.strong.leke.student:id/login_username", self.login_name)
        self.base.send_keys_txt("com.strong.leke.student:id/login_password", self.password)
        self.base.click("com.strong.leke.student:id/btn_login")
        
        #“点击我的商城”按钮
        time.sleep(10)
        self.base.click(self.mall_btn_id)
        result = self.base.get_element_txt(self.expected_xpath)
        
        #预期与实际断言
        time.sleep(10)
        self.assertEqual(result, self.expected_result)








