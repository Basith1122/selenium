from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.google.com/")
driver.find_element(By.PARTIAL_LINK_TEXT,"Gmai").click()
