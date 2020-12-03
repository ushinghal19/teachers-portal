import os

import eventlet
import requests
import socketio
import json

from dotenv import load_dotenv
load_dotenv()

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

TEST_ENDPOINT = r'https://hookb.in/lJPDz0kkRYcrXXZWdpgN'
PROD_ENDPOINT = r''
DEV_ENDPOINT = r'http://127.0.0.1:8000/'
CURRENT_ENDPOINT = ''

@sio.event
def connect(sid: int, environ: dict) -> None:
    """
    Handler Method to process connection to Hypatia API.
    """
    print('connect ', sid)


@sio.on('expressions')
def message_expressions(sid: int, data: str) -> None:
    """Handler method to process `expression` events from the Hypatia API"""
    # print('expressions:\n', data)
    record = json.loads(data)
    print(f'Received and ignored expression of mathid {record.mathid}')
    # r = requests.post(TEST_ENDPOINT, data=data)
    print(record)


@sio.on('result')
def message_result(sid: int, data: str) -> None:
    """Handler method to process `result` events from the Hypatia API"""
    print('result:\n', data)
    record = json.loads(data)
    print(record)

    if not TEACHER_MODE:
        # logic to post errors, since this must be a student
        r = requests.post(CURRENT_ENDPOINT, data=data)
        print(r.text)
    else:
        # logic to post errors
        global ASSIGNMENT_POSTING_ENABLED
        if ASSIGNMENT_POSTING_ENABLED:
            assignment_name = os.getenv('ASSIGNMENT_NAME')
            query = {}
            r = requests.post(CURRENT_ENDPOINT, data=data)
            if r.ok:
                ASSIGNMENT_POSTING_ENABLED = False
                # This ensures that one can only post a single new assignment, with each run of
                # the program
            print(r.text)


@sio.event
def disconnect(sid: int) -> None:
    """Handler method to process `disconnect` events from the Hypatia API"""
    print('disconnect ', sid)


if __name__ == '__main__':

    # Setup Constants
    RUNNING_ENVIRONMENT = os.getenv('RUNNING_ENVIRONMENT')
    if RUNNING_ENVIRONMENT == "PROD":
        CURRENT_ENDPOINT = PROD_ENDPOINT
    elif RUNNING_ENVIRONMENT == "DEV":
        CURRENT_ENDPOINT = DEV_ENDPOINT
    else:   # Default to Test mode
        CURRENT_ENDPOINT = TEST_ENDPOINT

    TEACHER_MODE = os.getenv('TEACHER_MODE')
    ASSIGNMENT_POSTING_ENABLED = TEACHER_MODE

    eventlet.wsgi.server(eventlet.listen(('localhost', 3333)), app)
