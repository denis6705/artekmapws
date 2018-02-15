import asyncio
import datetime
import random
import websockets
from ping3 import *
import json

with open('nodes.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
    nodes = json.load(fh) #загружаем из файла данные в словарь data
	
async def sendpings(websocket, path):
    while True:
        pings = dict()
        for key in nodes:
            pings[key] = []
            pings[key].append(ping(nodes[key][0], 1))
            if pings[key][0] == None : pings[key][0] = -1
            pings[key].append(nodes[key][1])
            pings[key].append(nodes[key][2])
            
        await websocket.send(json.dumps(pings,ensure_ascii=False))
        await asyncio.sleep(5)

start_server = websockets.serve(sendpings, '0.0.0.0', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
