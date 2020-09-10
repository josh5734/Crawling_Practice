from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options

import random


driver = webdriver.Chrome() #Chrome 쓸거다
url = 'https://yscec.yonsei.ac.kr'
driver.get(url) #url을 열어라
driver.maximize_window() #있어도 되고 없어도 된다.
action = ActionChains(driver) #action이란 변수를 사용해서 드라이버를 사용하겠다.

driver.find_element_by_css_selector('#username').click()
#id = input("학번을 입력하세요: ")
action.send_keys('2016147008').perform()# perform으로 실행

time.sleep(1) #중간에 텀을 줘서 인터넷 시간오류를 제어
#pw = input("비밀번호를 입력하세요: ")
driver.find_element_by_css_selector('#password').send_keys('ta9488ut') #class할 때는 .앞에 붙인다. id는 '#'붙인다.
driver.find_element_by_css_selector('#loginbtn').click()
time.sleep(2) #로그인이 되고 나서 다음 url로 넘어가야 함

driver.get('https://yscec.yonsei.ac.kr/mod/jinotechboard/view.php?id=1560954')
time.sleep(2)

cnt = 0
while cnt < 20:
    criterion = random.randint(0, 9) #0에서 9까지 랜덤 integer를 생성
    driver.find_element_by_css_selector("#thread > ul > li:nth-child(5) > div.thread-content > h1 > a").click()
    driver.back()
    cnt += 1
    if cnt % 10 == criterion:
        time.sleep(2)
        print("finished %d", cnt, 'criterion: %d', criterion)