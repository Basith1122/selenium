# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# button=driver.find_element(By.XPATH,"//button['Click for JS Confirm']")
# button.click()
# time.sleep(4)
# window=driver.switch_to.alert
# print(window.text)
# window.accept()



# with importing alert
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
btn=driver.find_element(by=By.XPATH,value="//button['Click for JS Confirm']")
btn.click()
w=Alert(driver)
print("jish is bad")
w.accept()

