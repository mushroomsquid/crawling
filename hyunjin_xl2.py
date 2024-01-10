
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags = CREATE_NO_WINDOW   
driver = webdriver.Chrome(service = serv)

import time, datetime
import os#폴더 만드는 모듈
import openpyxl

now=str(datetime.datetime.now())[:16]#지금 시간을 15번째 칸까지 자르기
folderName=now.replace(":","_")#위에 있는 now에서 :을 _로 바꾸기
os.mkdir(folderName)#folderName을 폴더 이름으로 해서 폴더 만들기

key_word=["대입전형"]

wb=openpyxl.Workbook()#액셀 열기

for i in range(len(key_word)):#key_word리스트의 길이만큼 반복
    ws=wb.create_sheet()#워크시트 만들기
    ws.title=key_word[i]#워크시트 이름 정하기
    url= "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=" + key_word[i]
    driver.get(url)
    time.sleep(2)
