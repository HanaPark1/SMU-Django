from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

from .models import ChatMessage

class ChatConsumer(WebsocketConsumer):
		# 해당 방으로 연결
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'char_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

		# 방에서 나가기
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # 메시지 DB 저장
        ChatMessage.objects.create(room_name=self.room_name, message=message)
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    
    def chat_message(self,event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message':message
        }))