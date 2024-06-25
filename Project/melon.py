# melon music scraping

from bs4 import BeautifulSoup # bs4 라이브러리 설치 필요 
import requests # requests 라이브러리 설치 필요 
# pip install request bs4

'''
스크래핑 하고 싶은 주소를 url에 넣어주세요
'''
url = "https://www.melon.com/chart/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# selct_one: 한 줄 씩 들고옴 / select: 해당 태그인 것들을 전부 들고옴
trs = soup.select('.lst50')

for tr in trs:
    rank = tr.select_one('.rank').text
    title = tr.select_one('.rank01 > span > a').text # <rank01><span><a>text</a></span></rank01>
    artist = tr.select_one('.rank02 > a').text
    image = tr.select_one('img')['src'] # <img src="이미지주소"> #img 주소에 src 속성

    print(rank,title, artist, image)

