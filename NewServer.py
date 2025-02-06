from fastapi import FastAPI
from upstash_redis import Redis

app = FastAPI()
kv = Redis(url="https://immortal-pup-24469.upstash.io", token="AV-VAAIjcDEyZDJjNTMwMThhNGI0MzQ0YmExOTE4ZDJkODg1YjEyNXAxMA")

@app.get("/queue/{inp}", tags=["Root"])
async def test(inp: str):
    kv.set('p1move', None)
    kv.set('p2move', None)
    print(type(inp))
    try:
        if inp not in kv.get("ip"):
            kv.set("ip", kv.get("ip") + inp + ', ')
    except:
        kv.set("ip", inp)
        kv.set("started", False)
    return {"players": len((kv.get("ip")).split(",")), "started": kv.get("started")}

@app.get("/players/")
async def players():
   return {"players": len((kv.get("ip")).split(",")), "ips": kv.get("ip")}

@app.get("/clear/")
async def clear():
    kv.delete('ip')
    kv.delete("started")

@app.get("/start/")
async def start():
    kv.set("started", True)

@app.get("/main/{spot}/{move}")
async def main(spot: str, move: str):
    if spot == '1':
        kv.set('p2move', None)
        kv.set("p1move", move)
        return {"success": "true"}
    else:
        kv.set('p1move', None)
        kv.set('p2move', move)
        return {'success': 'true'}
    
@app.get('/request')
async def request():
    return {"p1move": kv.get("p1move"), "p2move": kv.get('p2move')}