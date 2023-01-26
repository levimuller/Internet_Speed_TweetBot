from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

PROMISED_DOWN = 150
PROMISED_UP = 50
TWITTER_EMAIL = os.getenv('twitter_e')
TWITTER_PASSWORD = os.getenv('twitter_p')

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.go_click = self.driver.find_element("xpath",
                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(45)
        self.down = self.driver.find_element("xpath",
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element("xpath",
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(f"Download Speed: {self.down}")
        print(f"Upload Speed: {self.up}")

        
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(2)
        self.log_in_email = self.driver.find_element("xpath",
                                           '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(
            TWITTER_EMAIL)
        time.sleep(2)
        self.log_in_click = self.driver.find_element("xpath",
                                           '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        self.log_in_click.click()
        time.sleep(10)
        self.log_in_password = self.driver.find_element("xpath",
                                                     '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(
            TWITTER_PASSWORD)
        time.sleep(2)
        self.log_in_click_2 = self.driver.find_element("xpath",
                                                     '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        self.log_in_click_2.click()
        time.sleep(5)
        tweet_compose = self.driver.find_element("xpath",
                                                     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey @CenturyLink, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element("xpath",
                                                     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet_button.click()

        time.sleep(2)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

