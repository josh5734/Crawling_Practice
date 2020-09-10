from selenium import webdriver
import time
url = 'https://www.kyobobook.co.kr'
#url = 'http://www.naver.com'

driver = webdriver.Chrome()
driver.get(url)

print(driver.window_handles)

time.sleep(1)
driver.switch_to_window(driver.window_handles[1])
driver.close()
driver.switch_to_window(driver.window_handles[0])

book1 = driver.find_element_by_class_name('gnb_main')
book2 = book1.find_element_by_class_name('item_1')
book2.find_element_by_class_name('text').click()