# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import Select
# import time
# driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/package-summary.html")
# driver.switch_to.frame("packageListFrame")
# time.sleep(1)
# f1=driver.find_element(By.LINK_TEXT,"org.openqa.selenium.chromium")
# f1.click()
# time.sleep(3)
# driver.maximize_window()
# driver.switch_to.default_content()
# driver.switch_to.frame("packageFrame")
# f2=driver.find_element(By.LINK_TEXT,"AddHasCasting")
# f2.click()
# time.sleep(3)
# driver.switch_to.default_content()
# driver.switch_to.frame("classFrame")
# f3=driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[1]/a")
# f3.click()
# time.sleep(5)

# switching to new tab
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# driver.get("https://login.yahoo.com/?.intl=in")
# p=driver.find_element(By.LINK_TEXT,"Privacy").click()
# driver.switch_to.window(driver.window_handles[1])
# driver.switch_to.window(driver.window_handles[0])



# # work has to be done
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# driver.get("https://www.wikipedia.org/")
# q=driver.find_element().click()
# driver.switch_to.window(driver.window_handles[1])
# driver.switch_to.window(driver.window_handles[0])