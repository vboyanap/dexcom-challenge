from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import Element_locator
from config import configuration as cfg
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
import os
#log = log_global()



class SeleniumLibrary:
    @staticmethod
    def login(self, url):
        """
        Description: Verify that user perform below mentioned step
        check the user edit with invalid new password
        """
        browser_url = url
        print("printing url " + str(browser_url))
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        #options = ChromeOptions()
        # options.add_argument("headless")
        # options.add_argument('--disable-gpu')
        # options.add_argument("window-size=1294,768")
        # options.add_argument("--no-sandbox")
        # desired_capabilities = options.to_capabilities()
        # desired_capabilities['acceptSslCerts'] = True
        # desired_capabilities['acceptInsecureCerts'] = True
        cwd = os.getcwd()
        print("dirrr: "+ cwd)
        base_dir = cwd+"/"+"chromedriver"
        print(base_dir)
        #log.info("exec path: %s" % base_dir)

        browser = webdriver.Chrome(chrome_options=options, executable_path=base_dir)
        browser.get_window_size(1024)
        #browser.fullscreen_window()
        browser.implicitly_wait(6)
        browser.get(browser_url)
        time.sleep(5)

        browser.find_element_by_xpath(Element_locator.home_page).click()
        time.sleep(10)
        password_form = browser. \
            find_element_by_name(Element_locator.login_password)
        username_form = browser. \
            find_element_by_name(Element_locator.login_name)
        username_form.send_keys(cfg.USER)
        password_form.send_keys(cfg.PASSWORD)
        login = browser. \
            find_element_by_xpath(Element_locator.Login_button)
        login.click()
        time.sleep(3)
        return browser