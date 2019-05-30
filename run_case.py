import unittest
import  HTMLTestRunner
import time


if __name__ == '__main__':
    #获取要执行的所有py文件
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover("F:\\AppiumTest\\TestCase\\", '*.py')

    #要执行的所有py文件，装入测试套件
    for case in discover:
        suite.addTests(case)
    # suite.addTest(TestLogin_0
    
    #测试结果写入测试报告
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    day  = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    result_path = "F:\\AppiumTest\\Report\\"
    report_file = result_path + "\\"+ now + "_result.html"
    fp  = open(report_file,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"appium测试报告",description=u'用例详情;')
    runner.run(suite)
    fp.close()



