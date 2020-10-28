
import eventlet
import socketio
import json

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)
hintCounter = 1

def gen_dict_extract(var, key, value):
    # return all elements containing key <key> set to value <value>
    # based on https://stackoverflow.com/questions/9807634/find-all-occurrences-of-a-key-in-nested-dictionaries-and-lists
    if isinstance(var, list):
        for d in var:
            for result in gen_dict_extract(d, key, value):
                yield result
    elif isinstance(var, dict):
        for k, v in var.items():
            if k == key and v == value:
                yield var
            if isinstance(v, dict) or isinstance(v, list):
                for result in gen_dict_extract(v, key, value):
                    yield result
    else:
        print('UNEXPECTED:', var)


@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)


@sio.on('expressions')
def message_expressions(sid, data):
    print('expressions:\n', data)
    # parser json to python data structure
    record = json.loads(data)
    # demo:
    #   show a yellow box around each plus expression
    #   Note: make sure to reduce opacity of the color (37 below) otherwise it will cover the math
    for node in list(gen_dict_extract(record, 'command', 'Plus')):
        sio.emit('add_box', json.dumps({
          "mathid": record["mathid"],
          "version": record["version"],
          "id": node["id"],
          "type": "math-custom",
          "hint": "This is an addition recognized by Python",
          "color": "#FFFF0037",
          "border_color": "#FFFFFFAA",
          "border_width": "3px"
        }), room=sid)


@sio.on('result')
def message_result(sid, data):
    global hintCounter
    print('result:\n', data)
    # parser json to python data structure
    record = json.loads(data)
    print(record)
    # demo:
    #   check if result has a hint, if not send one
    #   Note: "hint" prefixed with '&' is treated as HTML code
    #   Note: optional "mode" can be "set" or "append" (default)
    if not "hint" in record["value"]:
      sio.emit('set_hint', json.dumps({
          "mathid": record["mathid"],
          "version": record["version"],
          "id": record["value"]["id"],
          "type": record["value"]["type"],
          "hint": "&Hint " + str(hintCounter) + " supplied by Evan's <b>Python</b>",
          "mode": "set"
      }), room=sid)
      hintCounter += 1


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 3333)), app)
