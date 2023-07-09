from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path="chromedriver.exe", log_path="NUL"))

# driver.get("https://en.wikipedia.org/")
# article_count = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# # article_count.click()

# search_input = driver.find_element(By.NAME, "search")
# search_button = driver.find_element(By.XPATH, '//*[@id="p-search"]/a/span[1]')
# search_button.click()
# search_input.send_keys("Python", Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("berho", Keys.TAB)
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("test", Keys.TAB)
email = driver.find_element(By.NAME, "email")
email.send_keys("test@mail.com", Keys.ENTER)