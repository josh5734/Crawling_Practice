# 와이섹 강의목록 크롤링하기
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import urllib.parse
import urllib.request
import random

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome("C:/Users/josunghyeon/Desktop/jupyter/chromedriver.exe") #Chrome 쓸거다
url = 'https://yscec.yonsei.ac.kr'
driver.get(url) #url을 열어라
driver.maximize_window() #있어도 되고 없어도 된다.
action = ActionChains(driver) #action이란 변수를 사용해서 드라이버를 사용하겠다.

driver.find_element_by_css_selector('#username').click()
#id = input("학번을 입력하세요: ")
action.send_keys('2016147008').perform()# perform으로 실행

time.sleep(1) #중간에 텀을 줘서 인터넷 시간오류를 제어
#pw = input("비밀번호를 입력하세요: ")
driver.find_element_by_css_selector('#password').send_keys('####') #class할 때는 .앞에 붙인다. id는 '#'붙인다.
driver.find_element_by_css_selector('#loginbtn').click()
time.sleep(2) #로그인이 되고 나서 다음 url로 넘어가야 함


course_list = ['1544412','1544748','1550319','1550313','1550301','1545681']
course_title = ['탐색적자료분석','공학정보처리','데이터분석','OR확률모델','데이터마이닝이론및응용','세계문학감상여행']

for id in course_list:
    print(course_title[course_list.index(id)]+" 과목의 강의공지 내용입니다.")
    driver.get("https://yscec.yonsei.ac.kr/mod/jinotechboard/view.php?id="+str(id))
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    link_title = soup.select('li > div.thread-content > h1 > a')
    link_content = soup.select('li > div.thread-content > p')

    #li 선택하고 lambda 만들어서할수있음
    cnt = len(link_title)-len(link_content)
    x = 1
    for num in range(len(link_content)):
        print("<"+str(x)+"번째 공지입니다.>")
        print("제목: "+ link_title[cnt:len(link_content)+cnt][num].get_text())
        print("내용: "+ link_content[num].get_text())
        print()
        x+=1
driver.close()























