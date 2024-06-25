# 날씨 웹 스크래핑(크롤링)하기

import requests
from bs4 import BeautifulSoup

URL = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=날씨"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# select_one: 특정 태그에 있는 정보만 긁어옴  , contentes: 리스트로 들어있는 걸 알아서 쪼개줌
temp = soup.select_one('.temperature > strong').contents[1] 
print(temp)

# 선택자를 사용하는 방법 (copy selector)
# soup.select('태그명')
# soup.select('.클래스명')
# soup.select('#아이디명')

# soup.select('상위태그명 > 하위태그명 > 하위태그명')
# soup.select('상위태그명.클래스명 > 하위태그명.클래스명')

# # 태그와 속성값으로 찾는 방법
# soup.select('태그명[속성="값"]')

# # 한 개만 가져오고 싶은 경우
# soup.select_one('위와 동일')
