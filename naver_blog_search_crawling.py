import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

# 원하는 페이지 수 만큼 크롤링하기 #
plusurl = urllib.parse.quote_plus(input("검색어를 입력하세요: "))
pageNum = 1
count = 1
i = input('몇 페이지를 크롤링 할까요? : ')
lastPage = 1 + (int(i)-1) * 10

while pageNum < lastPage + 1:
    url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusurl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pageNum}'
    html = urllib.request.urlopen(url).read()  # url을 오픈하고 읽어서 html변수 안에 저장한다.
    soup = BeautifulSoup(html, 'html.parser')  # bs를 사용해서 분석한다. 그 분석 내용을 soup 안에 저장한다.

    title = soup.find_all(class_='sh_blog_title')  # soup 중에 soup중 'sh~'라는 클래스를 가진 내용을 저장한다.
    print(f'-----------{count}페이지 결과입니다.----------')
    for i in title:
        print(i.attrs['title'])  # title 속성
        print(i.attrs['href'])  # href 속성
    print()

    pageNum += 10
    count += 1


