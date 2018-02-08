import asyncio
import datetime
import random
import websockets
from ping3 import *
import json

nodes = {
	"Хрустальный"   : ["172.20.255.10",     3790, 590],
	"Янтарный"      : ["172.20.255.11",	3780, 740],
	"ФОК"           : ["172.20.255.12",	3740, 970],
	"Морской"       : ["172.20.255.20",	3510, 1230],
	"ЦДО"           : ["172.20.255.30",	1700, 1300],
	"Вожатый"       : ["172.20.255.40",	2960, 260],
	"Залупа"	: ["172.20.20.20",      400,  400],
	"Залупа2"	: ["172.20.20.21",      800,  800]
	}
	
async def sendpings(websocket, path):
    while True:
        pings = dict()
        for key in nodes:
            pings[key] = []
            pings[key].append(ping(nodes[key][0], 1))
            if pings[key][0] == None : pings[key][0] = -1
            pings[key].append(nodes[key][1])
            pings[key].append(nodes[key][2])
            
        await websocket.send(json.dumps(pings,ensure_ascii=False,separators=(',',':')))
        await asyncio.sleep(10)

start_server = websockets.serve(sendpings, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
