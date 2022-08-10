from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.yatra.com/")
b=driver.find_element(By.TAG_NAME,"a")
print(len(b))
for i in b:
    print(b.text)