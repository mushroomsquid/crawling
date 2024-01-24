'''
from selenium import webdriver
import time


driver=webdriver.Chrome()

driver.get("https://www.google.com")

driver.maximize_window()#창 최대화
driver.minimize_window()#창 최소화
driver.set_window_position(0,0)#창 위치 조정
driver.set_window_size(500,800)#창 크기 조정
u=["https://youtube.com","https://naver.com","https://google.com"]
d=[]
import time

for i in range(len(u)):
    driver=webdriver.Chrome()
    d.append(driver)
    time.sleep(1)

for i in range(len(u)):
    d[i].get(u[i])

input("엔터치면 창이 닫힙니다.종료할까요?")
for i in range(len(u)):
    d[i].close()


driver.set_window_size(200,300)
driver.set_window_position(0,0)
import time
f=0
for i in range(7):
    driver.set_window_position(f,f)
    f+=100
    time.sleep(1)

w=1920/2
h=1080/2
pos=[(0,0),(w,0),(0,h),(w,h)]
f=[]
for i in range(4):
    d=webdriver.Chrome()
    d.get("https://www.google.com")
    d.set_window_size(975,547)
    d.set_window_position(pos[i][0],pos[i][1])
    f.append(d)
'''
#cmd창 없애기
'''
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)
driver.get("https://www.youtube.com")
'''

#테스트 사이트 웹크롤링
'''
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)
driver.get("https://gg.gg/hyeonjin")
p='//*[@id="homePageLinks"]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_firstName"]'
e=driver.find_element('xpath',p)
e.send_keys("Hyeonjin")

p='//*[@id="id_lastName"]'
e=driver.find_element('xpath',p)
e.send_keys("Song")

p='//*[@id="id_gender"]/li[1]/label'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_username"]'
e=driver.find_element('xpath',p)
e.send_keys("mushroomsquid")

p='//*[@id="id_password"]'
e=driver.find_element('xpath',p)
e.send_keys('muscariasquid1!')

p='//*[@id="id_state"]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_state"]/option[2]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_fee"]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_fee"]/option[4]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_date"]'
e=driver.find_element('xpath',p)
e.send_keys('4/15/2011')
'''
'''
#닌텐도
from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get('https://www.nintendo.co.kr/')

p='//*[@id="ncmn-gHeader"]/div[2]/div[2]/div/div[6]/div[1]/div/div/input[1]'
e=driver.find_element('xpath',p)
e.send_keys('귀멸의 칼날 히노카미 혈풍담')

from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)

p=''
e=driver.find_element('xpath',p)
e.click()

'''
#enter치기
'''
from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)
'''

#유튜브에서 검색하기
'''
import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)


driver.get('https://www.youtube.com/results?search_query=빠뚜루돈')
time.sleep(1)
#p='//input[@id="search"]'
#e=driver.find_element('xpath',p)
#e.send_keys('빠뚜루돈')

#from selenium.webdriver.common.keys import Keys
#e.send_keys(Keys.RETURN)
#time.sleep(5)

p1='//a[@id="thumbnail"]'
elements=driver.find_elements('xpath',p1)

print(elements[3].get_attribute("href"))
time.sleep(2)

driver.get(elements[3].get_attribute("href"))


p2='//*[@id="movie_player"]/div[34]/div[2]/div[1]/button'
e1=driver.find_element('xpath',p2)
e1.click()
'''

#학교종이(늘봄초)
'''
from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get('https://v4.schoolbell-e.com/ko/gate/home?return_uri=https:%2F%2Fschoolbell-e.com%2Fko%2Fmain')
time.sleep(1)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-home/div[1]/div[3]/div[1]/div/button[1]'
e=driver.find_element('xpath',p)
e.click()
time.sleep(1)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[1]/div[1]/phone-number-input/div/input'
e=driver.find_element('xpath',p)
e.send_keys('01032808593')
time.sleep(1)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[2]/div/input'
e=driver.find_element('xpath',p)
e.send_keys('8593')
time.sleep(1)

from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)
time.sleep(3)

p='/html/body/app-root/app-main/div[1]/app-main-home/div[2]/div[1]/div[1]/app-my-group-slides/div/ngu-carousel/div/div[1]/div/ngu-tile[2]/div/div[1]/div/div'
e=driver.find_element('xpath',p)
e.click()
time.sleep(1)

file=open('학교종이.txt','w')
'''
#학교종이 안내문 출력(f 포맷팅)
'''
time.sleep(3)
for i in range(10):
    p=f'/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div[3]/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/h6/app-translation-viewer/span'
    e=driver.find_element('xpath',p)
    text=(e.text)
    file.write(text+'\n')
file.close()


'''
#텍스트 파일로 저장하기
'''0.
text='버징어'
file=open('테스트.txt','w')
file.write(text)
file.close()
'''
#네이버 뉴스 검색창 스크린캡처 하기
from selenium import webdriver
import time

s=[]

l=input("몇개:")
for i in range(0,int(l)):
    n=input("검색어:")
    s.append(n)

driver=webdriver.Chrome()
driver.maximize_window()

for i in range(len(s)):
    driver.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+str(s[i]))
    driver.save_screenshot(str(i)+".png")

