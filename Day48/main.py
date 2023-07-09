from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
 
options = webdriver.ChromeOptions()
# Keep the browser open after the script is done
options.add_experimental_option("detach", True)
 
driver = webdriver.Chrome(options=options, service=Service(executable_path="chromedriver.exe", log_path="NUL"))

# driver.get("https://www.amazon.com.tr/Samsung-970-EVO-PLUS-NVMe/dp/B07MBQPQ62/ref=sr_1_12?crid=NO0OB3MJ9OBZ&keywords=ssd&qid=1688839804&sprefix=%2Caps%2C287&sr=8-12&th=1")
driver.get("https://www.python.org/")

# # Find element by class  
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

# # Find element by name
# search_bar = driver.find_element(By.NAME, "field-keywords")
# search_bar.send_keys("SSD")

# # Find element by CSS selector
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# # Find element by XPATH
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute("href"))

upcoming_events_dates = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last div ul li time")
for date in upcoming_events_dates:
    print(date.text)

upcoming_events_names = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last div ul li a")
for name in upcoming_events_names:
    print(name.text)

end_list = [{"name":name.text, "date":start_date.text } for name, start_date in zip(upcoming_events_names, upcoming_events_dates)]
print(end_list)

# # Find the add to cart button and click it
# driver.find_element(By.ID, "add-to-cart-button").click()

# # Close just the current tab
# driver.close()
# Close the entire browser
driver.quit()
