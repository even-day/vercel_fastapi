from fastapi import FastAPI
from api.v2 import get_sub_url

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/v2')
def v2():
    subscription_dict = get_sub_url()
    return subscription_dict
