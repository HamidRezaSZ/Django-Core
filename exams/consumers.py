import json

from channels.generic.websocket import WebsocketConsumer

from .models import Exam


class ExamConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.id = self.scope["url_route"]["kwargs"]["id"]
        self.accept()

    def disconnect(self, close_code):
        self.close()

    def receive(self, text_data):
        result = {"message": "Error"}
        try:
            obj = Exam.objects.get(id=int(self.id))
            result = {"message": {
                'remaining_time': str(obj.remaining_time(self.user))
            }
            }
        except Exception:
            pass

        self.send(text_data=json.dumps(result))
