
# coding=utf-8
import time

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWework:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_get_cookie(self):
        """
        复用浏览器，获取登录后cookie,写入cookie.yaml文件
        :return:
        """
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        cookies = self.driver.get_cookies()
        with open('./cookie.yaml','w',encoding='utf-8') as f:
            yaml.safe_dump(data=cookies,stream=f)

    # @pytest.mark.skip
    def test_login(self):
        """
        使用cookie,登录企业微信首页
        :return:
        """
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        with open('./cookie.yaml','r',encoding='utf-8') as f:
            cookies = yaml.safe_load(f)
            print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        time.sleep(5)
        assert self.driver.find_element_by_xpath('//*[@class="frame_nav_item_title" and text()="首页"]').is_displayed()

    # @pytest.mark.skip
    def test_add_contacts(self):
        WebDriverWait(self.driver,timeout=5).until(expected_conditions.element_to_be_clickable((By.XPATH,'//span[@class="index_service_cnt_item_title" and text()="添加成员"]')))
        # 点击添加成员
        self.driver.find_element_by_xpath('//span[@class="index_service_cnt_item_title" and text()="添加成员"]').click()
        WebDriverWait(self.driver,timeout=5).until(expected_conditions.visibility_of_element_located((By.ID,'username')))
        # 输入用户名
        self.driver.find_element_by_id('username').send_keys('ojbk8ty')
        # 输入账号
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('jklsb767')
        # 输入手机号
        self.driver.find_element_by_id('memberAdd_phone').send_keys('13118172286')
        # 点击保存
        self.driver.find_element_by_link_text('保存').click()
        assert self.driver.find_element_by_xpath('//span[text()="ojbk8ty"]').is_displayed()

if __name__ == "__main__":
    pytest.main(['-vs','./test_cookie_Wework.py'])





