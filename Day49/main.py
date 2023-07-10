from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import unquote
import time

ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path="chromedriver.exe", log_path="NUL"))
url = "https://www.linkedin.com/jobs/search/?currentJobId=3630645300&f_AL=true&f_E=2&f_WT=2&geoId=102105699&keywords=python&location=Turkey&refresh=true"
encoded_url = unquote(url)
driver.get(encoded_url)

time.sleep(2)

login_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
login_button.click()

time.sleep(2)

login = driver.find_element(By.ID, 'username')

time.sleep(2)

login.send_keys(ACCOUNT_EMAIL, Keys.TAB, ACCOUNT_PASSWORD)
login.send_keys(Keys.ENTER)


all_listings = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable .job-card-list__title')

time.sleep(5)

test = all_listings[0]
print(test.text)
test.click()

apply_button = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card')
apply_button.click()

time.sleep(2)

next_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-button--primary')
next_button.click()

time.sleep(2)

review_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-button--primary')
review_button.click()

time.sleep(2)

follow_button = driver.find_element(By.CSS_SELECTOR, '.full-height')
follow_button.send_keys(Keys.TAB,Keys.SPACE)

time.sleep(2)

submit_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-button--primary')
submit_button.click()

