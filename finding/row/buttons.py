from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
br=driver.find_element(By.NAME,"radioButton").click()