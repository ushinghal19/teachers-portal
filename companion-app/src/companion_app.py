import os
import random

import eventlet
import requests
import socketio
import json

from dotenv import load_dotenv

from tp_gateway import create_assignment, create_error

load_dotenv()

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

TEST_ENDPOINT = r'https://hookb.in/lJPDz0kkRYcrXXZWdpgN'
PROD_ENDPOINT = r''
DEV_ENDPOINT = r'http://127.0.0.1:8000/graphql'
CURRENT_ENDPOINT = ''

POSSIBLE_ERRORS = ['Fraction Error', 'Trig Error', 'Order Of Operation'
    # 'Fraction Error', 'Divison Error', 'Trig Error', 'Possible Division By Zero',
    #                'Order Of Operation', 'Assumed Parentheses', 'Improper Distribution',
    #                'Cancelling Error', 'Square Root Error'
                   ]

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
    print(f'Received and ignored expression of mathid {record["mathid"]}')
    # print(record)


@sio.on('result')
def message_result(sid: int, data: str) -> None:
    """Handler method to process `result` events from the Hypatia API"""
    # print('result:\n', data)
    record = json.loads(data)
    print(record)

    assignment_id = '.'.join(str(record['docid']).split(sep=".")[0:2])  # selects only the first part of doc id

    if not TEACHER_MODE:
        # logic to post errors, since this must be a student
        problem_number = int(record['problem'])
        problem_number += 1
        student_name = record['username']
        if 'value' in record:
            try:
                error_id = record['value']['id']
                error_type = record['value']['type']
            except KeyError as e:
                print(e)
            if ERROR_TYPE_RANDOMIZATION:
                error_type = random.choice(POSSIBLE_ERRORS)
            r = create_error(CURRENT_ENDPOINT, assignment_id, error_id, error_type, problem_number,
                             student_name)
            print(r.text)
    else:
        # logic to post errors
        global ASSIGNMENT_POSTING_ENABLED
        if ASSIGNMENT_POSTING_ENABLED:
            assignment_name = os.getenv('ASSIGNMENT_NAME')
            teacher_id = os.getenv('TEACHER_KEY')
            teacher_name = record['username']
            assignment_file_name = record['docname']

            r = create_assignment(CURRENT_ENDPOINT, assignment_id, teacher_id, assignment_name)
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

    TEACHER_MODE = os.getenv('TEACHER_MODE') == 'True'
    ASSIGNMENT_POSTING_ENABLED = TEACHER_MODE

    ERROR_TYPE_RANDOMIZATION = os.getenv('ERROR_TYPE_MODE_RANDOM') == 'True'

    eventlet.wsgi.server(eventlet.listen(('localhost', 3333)), app)
