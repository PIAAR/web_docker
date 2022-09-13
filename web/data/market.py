import websocket, json


socket = ""

ws = websocket.WebSocketApp(socket, on_open=on_open)