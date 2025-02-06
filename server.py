from fastapi import FastAPI
from upstash_redis import Redis

app = FastAPI()
kv = Redis(url="https://immortal-pup-24469.upstash.io", token="AV-VAAIjcDEyZDJjNTMwMThhNGI0MzQ0YmExOTE4ZDJkODg1YjEyNXAxMA")

@app.get("/queue/{inp}", tags=["Root"])
async def test(inp: str):
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
    