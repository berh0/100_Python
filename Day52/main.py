from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from random import randint

SIMILAR_ACCOUNT= 'SOME_ACCOUNT_NAME' 
INSTA_EMAIL= 'YOUR_EMAIL'
INSTA_PASSWORD= 'YOUR_PASSWORD'
 

class InstaFollower:
    def __init__(self):
        self.opt = webdriver.ChromeOptions()
        self.opt.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.opt, service=Service(executable_path="chromedriver.exe", log_path="NUL"))

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        self.username=self.driver.find_element(By.NAME,'username')
        self.username.send_keys(INSTA_EMAIL)
        self.pas = self.driver.find_element(By.NAME, 'password')
        self.pas.send_keys(INSTA_PASSWORD)
        self.button=self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(3)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(4)

    def follow(self,number=10):
        for num in range(1, number+1):        
            delay=randint(2, 8)
            time.sleep(delay)          
            try:
                follow_button = self.driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{num}]/div/div/div/div[3]/div/button')
                
                print(follow_button.text)
                if follow_button.text == "Takip Et":
                    follow_button.click()
                else:
                    pass
            except NoSuchElementException:
                pass
            
bot=InstaFollower()
bot.login()
bot.find_followers()
bot.follow()