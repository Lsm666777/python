from selenium import webdriver
import time
driver = webdriver.Chrome()
time.sleep(1)
driver.get('https://www.baidu.com')
time.sleep(1)
driver.maximize_window()

time.sleep(1)
driver.find_element_by_id("kw").send_keys(12306)
driver.find_element_by_id("su").click()
time.sleep(1)
a = driver.current_window_handle
time.sleep(2)
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
time.sleep(1)
b = driver.window_handles
for er in b:
    if a != er:
        driver.switch_to_window(er)
driver.find_element_by_link_text("购票").click()
