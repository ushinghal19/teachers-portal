
import eventlet
import requests
import socketio
import json

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

TEST_ENDPOINT = r'https://hookb.in/lJPDz0kkRYcrXXZWdpgN'

@sio.event
def connect(sid: int, environ: dict) -> None:
    """
    Handler Method to process connection to Hypatia API.
    """
    print('connect ', sid)


@sio.on('expressions')
def message_expressions(sid, data: str):
    """Handler method to process `expression` events from the Hypatia API"""
    print('expressions:\n', data)
    record = json.loads(data)
    # TODO: Decide what to do with the expressions
    r = requests.post(TEST_ENDPOINT, data=data)
    print(r.text)


@sio.on('result')
def message_result(sid, data):
    """Handler method to process `result` events from the Hypatia API"""
    print('result:\n', data)
    record = json.loads(data)
    print(record)
    # TODO: Decide what to do with this
    r = requests.post(TEST_ENDPOINT, data=data)
    print(r.text)


@sio.event
def disconnect(sid: int) -> None:
    """Handler method to process `disconnect` events from the Hypatia API"""
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 3333)), app)
