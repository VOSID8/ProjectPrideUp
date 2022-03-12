from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from .models import Message
from shop import models as md
import datetime

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket connected...", event)

        print("Channel layer...", self.channel_layer) #default channel layer of project
        print("Channel name...", self.channel_name) #channel name

        async_to_sync(self.channel_layer.group_add)('group', self.channel_name) #add current channel to group, create group if doesn't exist

        self.send({
            'type': 'websocket.accept'
        })
    
    def websocket_receive(self, event):
        print("Message received from client...", event)

        message = json.loads(event['text'])
        message['user'] = str(self.scope['user'])
        message['timestamp'] = str(datetime.datetime.now())
        print(message)

        try:
            seller = md.Seller.objects.get(user=self.scope['user'])
        except:
            raise StopConsumer
        msg = Message(user=seller, message=message['msg'])
        msg.save()
        
        async_to_sync(self.channel_layer.group_send)('group', {
            'type': 'chat.message',
            'message': json.dumps(message)
        })

    def chat_message(self, event):
        self.send({
            'type': 'websocket.send',
            'text': event['message'],
        })
    
    def websocket_disconnect(self, event):
        print("Websocket disconnected...", event)

        print("Channel layer...", self.channel_layer)
        print("Channel name...", self.channel_name)

        async_to_sync(self.channel_layer.group_discard)('group', self.channel_name) #remove(discard) current channel from group
        
        raise StopConsumer