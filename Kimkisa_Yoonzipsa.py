import requests
from datetime import datetime
import time
import schedule 

# slack 토큰
token = "xoxb-3605200378048-3581469081394-SKY48DARzfkkRmq8hXOjMnCg"

# 변수 목록(작동 시간/전송 멘트)
o_time = "09:05"
c_time = "17:55"



# slack 챗 봇
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text})
    print(response)


# message로 받은 인자를 파이썬 쉘과 슬랙 #채널이름 에 동시에 출력한다
def Kimkisa():
    opening_text = "안녕하세요. 빅데이터 수강생 여러분..! 김기사입니다. \N{grinning face} \n QR 출석 입력 확인해주세요. \n 오늘도 행복 코딩 하세요!"
    #클론코딩 참고용, strftime 함수 사용법
    #print(datetime.now().strftime('[%m/%d %H:%M:%S]'), opening_text)
    #strbuf = datetime.now().strftime('[%m/%d %H:%M:%S] ') + closing_text
    post_message(token, "#프리토킹", opening_text)


#schedule.every(3).seconds.do(Kimkisa)
schedule.every().monday.at(o_time).do(Kimkisa)
schedule.every().tuesday.at(o_time).do(Kimkisa)
schedule.every().wednesday.at(o_time).do(Kimkisa)
schedule.every().thursday.at(o_time).do(Kimkisa)
schedule.every().friday.at(o_time).do(Kimkisa)

def Yoonzipsa():
    closing_text = "안녕하세요, 윤집사입니다. \n 오늘도 극락코딩 하셨나요? \N{smiling face with sunglasses} \n 마지막으로 퇴실 확인 부탁드리며 \n 내일 뵙도록 하겠습니다."
    post_message(token, "#프리토킹", closing_text)

#schedule.every(3).seconds.do(Yoonzipsa)
schedule.every().monday.at(c_time).do(Yoonzipsa)
schedule.every().tuesday.at(c_time).do(Yoonzipsa)
schedule.every().wednesday.at(c_time).do(Yoonzipsa)
schedule.every().thursday.at(c_time).do(Yoonzipsa)
schedule.every().friday.at(c_time).do(Yoonzipsa)

while True:
    schedule.run_pending()
    time.sleep(1)