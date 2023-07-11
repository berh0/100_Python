from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path="chromedriver.exe", log_path="NUL"))

PROMISED_DOWN = 150
PROMISED_UP = 15
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_PASSWORD = "YOUR PASSWORD"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.download = 0
        self.upload = 0

    def wait(self, seconds):
        time.sleep(seconds)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CSS_SELECTOR, '.start-button a')
        go_button.click()
        self.wait(45)
        self.download = float(self.driver.find_element(By.CSS_SELECTOR, '.download-speed').text)
        self.upload = float(self.driver.find_element(By.CSS_SELECTOR, '.upload-speed').text)
        print(self.download)
        print(self.upload)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        self.wait(2)
        login = self.driver.find_element(By.NAME, 'text')
        login.send_keys(TWITTER_EMAIL, Keys.ENTER)
        self.wait(2)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        self.wait(2)
        tweet = self.driver.find_element(By.CSS_SELECTOR, '.public-DraftStyleDefault-block')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.download} when I pay for {self.down}down/{self.up}up?")
        self.wait(2)
        send_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
        send_tweet.click()
        self.wait(2)
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if bot.download < bot.down or bot.upload < bot.up:
    bot.tweet_at_provider()
else:
    print("Internet speed is good")