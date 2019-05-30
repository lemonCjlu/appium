from PO.base_page import Base
from Common import getPrperity
from Common import  get_current_dir
import  os

module_name = "tutor\\test_login.py"
cur_path =  os.path.abspath(module_name)
property_path = get_current_dir.get_properity_dir(cur_path)

class LoginPage(Base):
    def __init__(self):
        Base.__init__(self)
        global property_path
        d = getPrperity.getProperity(property_path)
        self.loginname_id = d.get("loginname")
        self.password_id = d.get("password")
        self.submit_id = d.get("submit")

    def input_login_name(self, login_name):
        self.send_keys_txt(self.loginname_id, login_name)

    def input_login_password(self, login_password):
        self.send_keys_txt(self.password_id, login_password)

    def click_login_btn(self):
        self.click(self.submit_id)
