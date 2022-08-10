from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
selected=driver.find_element(by=By.XPATH,value="//select[@id='dropdown-class-example']")
dd=Select(selected)
dd.select_by_visible_text("Option3")
print("basith is pottan")
