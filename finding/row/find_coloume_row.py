# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# driver.get("https://testautomationpractice.blogspot.com/")
# rows=driver.find_elements(By.XPATH,"//table['@name=BookTable']//tr")
# column=driver.find_elements(By.XPATH,"//table['@name=BookTable']//tr[1]/th")
# print(f"numberof rows : {len(rows)}\n numberof coloum : {len(column)}")
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
ro=driver.find_elements(By.XPATH,"//*[@id='product']//tr")
co=driver.find_elements(By.XPATH,"//*[@id='product']//tr[1]/th")
print(len(ro))
print(len(co))