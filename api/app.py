from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from api.v2 import get_sub_url
from api.clash import main

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/v2')
def v2():
    subscription_dict = get_sub_url()
    return subscription_dict

@app.get('/clash',response_class=PlainTextResponse)
def clash():
    content = main()
    return content