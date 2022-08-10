from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
l=driver.find_element(by=By.ID,value="Email").send_keys("")
p=driver.find_element(by=By.ID,value="Password").send_keys("")
ck=driver.find_element(by=By.ID,value="RememberMe").click()
