import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.weather.go.kr/w/index.do"
# Chrome브라우저 및 get요청
browser = webdriver.Chrome()
browser.implicitly_wait(5) # 최대 (원하는)초 동안 대기
browser.get(url)
time.sleep(5)

#바람
wind_str = browser.find_element(By.CSS_SELECTOR,'#current-weather > '
                            'div.cmp-cur-weather.wbg.wbg-type2.BGDB00 > '
                            'ul.wrap-2.no-underline > li:nth-child(2) > span.val').text

#지역
area = browser.find_element(
    By.CSS_SELECTOR, 'a.serch-area-btn.accordionsecond-tit').text
#체감온도
actualTemp = browser.find_element(By.CLASS_NAME, 'chill').text
#습도
humidity_str = browser.find_element(By.CSS_SELECTOR, '#current-weather > div.cmp-cur-weather.wbg.wbg-type2.BGDB00 > ul.wrap-2.no-underline > li:nth-child(2) > span.val').text

wind_replace=float(wind_str.replace("남서","").replace("m/s", "")) #실시간으로 값이 변하기 때문에 확인해서 바람 방향을 변경해주어야한다.
wind_num = float(wind_str.split()[1])

print(f"원본데이터: {wind_str}")
print(f"바람데이터조작: {wind_replace}")
print(f"split함수사용:{wind_num}")
print(f"선택지역: {area}")
print(f"체감온도: {actualTemp}")
print(f"습도: {humidity_str}")
print(f"바람: {wind_str}")

#온도
temp = browser.find_element(By.CSS_SELECTOR, '#current-weather > div.cmp-cur-weather.wbg.wbg-type2.BGDB00 > ul.wrap-1 > li.w-icon.w-temp.no-w > span.tmp').text

#데이터수정

#replace
temp_replace = float(temp.replace("℃", ""))
#split
temp_split = float(temp.split('℃')[0])

if temp_replace > temp_replace-1:
    print('오늘 날씨가 더워요')

#스크래핑만 한 데이터
print(f"현재온도: {temp}")
#replace or split으로 조작한 데이터
print(f"조작한데이터: {temp_replace}")