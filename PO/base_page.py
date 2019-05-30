from  appium import  webdriver

class Base:
    def __init__(self):
        desired_caps = {}
        # 使用哪种移动平台
        desired_caps['platformName'] = 'Android'
        # Android版本
        desired_caps['platformVersion'] = '7.1.1'
        # 启动哪种设备，是真机还是模拟器？
        desired_caps['deviceName'] = 'L041807000058'
        # App的绝对路径
        # desired_caps['app'] = 'C:\\Users\\Administrator\\Downloads\\appstudent-release.apk' # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
        desired_caps['appPackage'] = 'com.strong.leke.student'  # 包名
        desired_caps['appActivity'] = 'com.strong.leke.student.app.activity.WelcomeActivity'  # Activity名
        desired_caps['unicodeKeyboard'] = True  # 使用unicodeKeyboard的编码方式来发送字符串
        desired_caps['resetKeyboard'] = True  # 将键盘给隐藏起来
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def find_element(self,element_id):
        # ''' 根据id查找元素'''
        # 参数loc  元素id
        try:
            res = self.driver.find_element_by_id(element_id)
            print(res)
            if res == 7:
               if  self.driver.find_element_by_id("com.strong.leke.student:id/tv_content").text == "我们乐课App做了优化升级，重启App即可生效，是否重启？":
                   self.driver.find_element_by_id("com.strong.leke.student:id/btn_cancel").click()
            return self.driver.find_element_by_id(element_id)
        except Exception as e:
            print(e)


    def send_keys_txt(self, element_id, key_value):
        # 文本框输入
        #element_id  文本框的id
        #key_value  要输入的内容
        try:
            element = self.find_element(element_id)
            element.send_keys(key_value)
        except Exception as e:
            print(e)

    def click(self, element_id):
        # 点击操作
        #参数element_id  被点击对象的id
        try:
            element = self.find_element(element_id)
            element.click()
        except Exception as e:
            print(e)

    def get_element_txt(self, element_id):
        #获取元素的文本
        try:
            element_txt = self.find_element(element_id).txt
            return  element_txt
        except Exception as e:
            print(e)


    def quit_driver(self):
        #退出driver
        self.driver.quit()






