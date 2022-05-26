from slack_sdk import WebClient
import time
import schedule 

class SlackAPI:
    """
    슬랙 API 핸들러
    """
    def __init__(self, token):
        # 슬랙 클라이언트 인스턴스 생성
        self.client = WebClient(token)
        
    def get_channel_id(self, channel_name):
        """
        슬랙 채널ID 조회
        """
        # conversations_list() 메서드 호출
        result = self.client.conversations_list()
        # 채널 정보 딕셔너리 리스트
        channels = result.data['channels']
        # 채널 명이 'test'인 채널 딕셔너리 쿼리
        channel = list(filter(lambda c: c["name"] == channel_name, channels))[0]
        # 채널ID 파싱
        channel_id = channel["id"]
        return channel_id

    def get_message_ts(self, channel_id, query):
        """
        슬랙 채널 내 메세지 조회
        """
        # conversations_history() 메서드 호출
        result = self.client.conversations_history(channel=channel_id)
        # 채널 내 메세지 정보 딕셔너리 리스트
        messages = result.data['messages']
        # 채널 내 메세지가 query와 일치하는 메세지 딕셔너리 쿼리
        message = list(filter(lambda m: m["text"]==query, messages))[0]
        # 해당 메세지ts 파싱
        message_ts = message["ts"]
        return message_ts

    def post_thread_message(self, channel_id, message_ts, text):
        """
        슬랙 채널 내 메세지의 Thread에 댓글 달기
        """
        # chat_postMessage() 메서드 호출
        result = self.client.chat_postMessage(
            channel=channel_id,
            text = text,
            thread_ts = message_ts
        )
        return result

token = "xoxb-3605200378048-3581469081394-SKY48DARzfkkRmq8hXOjMnCg"
slack = SlackAPI(token)
channel_name = "bot_mark1-생성"
query = "슬랙 봇 테스트"
opening_text = "빅데이터 수강생 여러분! QR 출석 입력 확인해주세요."
closing_text = "오늘도 고생하셨습니다! 잊지말고 퇴실 QR 체크 해주세요!"

# 채널ID 파싱
# channel_id = slack.get_channel_id(channel_name)
# # 메세지ts 파싱
# message_ts = slack.get_message_ts(channel_id, query)
# # 댓글 달기
# slack.post_thread_message(channel_id, message_ts, text)


def Kimkisa():
    # 채널ID 파싱
    channel_id = slack.get_channel_id(channel_name)
    # 댓글 달기
    slack.post_thread_message(channel_id, opening_text)
o_time = "09:05"
c_time = "18:05"

schedule.every(3).seconds.do(Kimkisa)
schedule.every().monday.at(o_time).do(Kimkisa)
schedule.every().tuesday.at(o_time).do(Kimkisa)
schedule.every().wednesday.at(o_time).do(Kimkisa)
schedule.every().thursday.at(o_time).do(Kimkisa)
schedule.every().friday.at(o_time).do(Kimkisa)

def Yoonzipsa():
    # 채널ID 파싱
    channel_id = slack.get_channel_id(channel_name)
    # 댓글 달기
    slack.post_thread_message(channel_id, opening_text)


schedule.every().monday.at(c_time).do(Yoonzipsa)
schedule.every().tuesday.at(c_time).do(Yoonzipsa)
schedule.every().wednesday.at(c_time).do(Yoonzipsa)
schedule.every().thursday.at(c_time).do(Yoonzipsa)
schedule.every().friday.at(c_time).do(Yoonzipsa)


while True:
    schedule.run_pending()
    time.sleep(1)

