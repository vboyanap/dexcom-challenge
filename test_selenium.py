from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import configuration as cfg
from lib.seleniumlibrary import SeleniumLibrary
import pytest
base_dir = "D:/chromedriver"
#browser = webdriver.Chrome(executable_path=base_dir)
#browser.implicitly_wait(3)
import time
class TestCROProxyApi:
    @pytest.fixture(scope="class", autouse=True)
    def setup_cleanup(self, request):
        self.end_point_url = cfg.UI_Login
        print(self.end_point_url)
    def test_create_account(self):
        """
        Description: Verify that user perform,
        check the vCenter edit with valid credentials
        """
        print("entering to function")
        browser = SeleniumLibrary.login(self, cfg.UI_Login)
        time.sleep(3)