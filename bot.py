from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

chrome_driver_path = "C:\\Users\\mgmma\\Desktop\\Python Projects\\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.expected_up = 30
        self.expected_down = 1024
        self.up = None
        self.down = None

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(1)
        self.driver.find_element_by_class_name('start-text').click()
        time.sleep(40)
        self.down = float(self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '2]/div/div[2]/span').text)
        self.up = float(self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '3]/div/div[2]/span').text)

    def tweet_at_provider(self):
        self.driver.get('https://www.twitter.com/')
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div['
                                          '1]/label/div/div[2]/div/input').send_keys(os.environ.get('twitter_email'))
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div['
                                          '2]/label/div/div[2]/div/input').send_keys(os.environ.get(
            'twitter_password'))
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()
        time.sleep(2)
        if (
                self.up is not None or self.down is not None) and self.expected_up > self.up or self.expected_down > self.down:
            msg = f"Hi @Rogers, My internet speed according to speedtest.net is {self.down}down/{self.up}up while " \
                  f"Ignite Gigabit says it supports up to {self.expected_down}down/{self.expected_up}up.  Bruh! "
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                              '2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div['
                                              '3]').send_keys(
                msg)
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                              '2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div['
                                              '2]/div').click()
        elif (
                self.up is not None or self.down is not None) and self.expected_up <= self.up or self.expected_down <= self.down:
            msg = f"Hi @Rogers, My internet speed according to speedtest.net is {self.down}down/{self.up}up.  Nice work!"
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                              '2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div['
                                              '3]').send_keys(
                msg)
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/d    iv/div[2]/div/div[2]/div['
                '1]/div/div/div/div[2]/div[2]/div/div/div[2]/div').click()
        else:
            pass

        self.driver.close()
