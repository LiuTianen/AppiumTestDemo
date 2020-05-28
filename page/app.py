import datetime

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from page.main_page import MainPage


class App:

    driver:WebDriver=None

    @classmethod
    def start(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "seveniruby"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        #caps["udid"] = "emulator-5556"
        caps["chromedriverExecutable"]="/Users/seveniruby/projects/chromedriver/2.20/chromedriver"
        caps["showChromedriverLog"]=True
        caps["noReset"] = True

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)


        #判断启动APP后有没有出现协议类弹窗。
        def loaded(driver):
            print(datetime.datetime.now())
            if len(cls.driver.find_elements_by_id("com.xueqiu.android:id/tv_agree")) >=1:
                cls.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()
                return True
            else:
                return False

        try:
            WebDriverWait(cls.driver, 20).until(loaded)
        except:
            print("没有弹窗")

        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()
