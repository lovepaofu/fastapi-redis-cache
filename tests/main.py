from datetime import date, datetime
from decimal import Decimal

from fastapi import FastAPI, Request, Response

from fastapi_redis_cache import cache

app = FastAPI(title="FastAPI Redis Cache Test App")


@app.get("/cache_never_expire")
@cache()
def cache_never_expire(request: Request, response: Response):
    return {"success": True, "message": "this data can be cached indefinitely"}


@app.get("/cache_expires")
@cache(expire_after_seconds=8)
async def cache_expires():
    return {"success": True, "message": "this data should be cached for eight seconds"}


@app.get("/cache_json_encoder")
@cache()
def cache_json_encoder():
    return {
        "success": True,
        "start_time": datetime(2021, 4, 20, 7, 17, 17),
        "finish_by": date(2021, 4, 21),
        "final_calc": Decimal(3.14),
    }
