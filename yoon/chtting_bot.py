import requests
from datetime import datetime


# slack 챗 봇
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text})
    print(response)


# slack 토큰
token = "xoxb-3605200378048-3581469081394-SKY48DARzfkkRmq8hXOjMnCg"


# message로 받은 인자를 파이썬 쉘과 슬랙 #채널이름 에 동시에 출력한다
def dbgout(message):
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S] ') + message
    post_message(token, "#bot_mark1-생성", strbuf)
dbgout("안녕하세요.")