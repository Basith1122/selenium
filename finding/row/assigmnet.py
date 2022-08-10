from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
q=driver.find_element(By.ID,"product_551").click()
e1=driver.find_element(By.ID,"travname").send_keys("basith")
e2=driver.find_element(By.ID,"travlastname").send_keys("n")
e3=driver.find_element(By.ID,"sex_1").click()
e7=driver.find_element(By.CLASS_NAME,"checkbox").click()
e8=driver.find_element(By.XPATH,"//*['@id=select2-addpaxno-container']")
ee=Select(e8).select_by_visible_text("option2")

e4=driver.find_element(By.ID,"traveltype_2").click()
e5=driver.find_element(By.ID,"fromcity").send_keys("calicit")
e6=driver.find_element(By.ID,"tocity").send_keys("bahrain")


