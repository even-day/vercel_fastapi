from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from api.v2 import get_sub_url
from api.clash import main
from api.clash2 import main2
from api.raw import return_raw
from api.one import get_hub_url

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/v2')
def v2():
    subscription_dict = get_sub_url()
    return subscription_dict


@app.get('/clash', response_class=PlainTextResponse)
def clash():
    content = main()
    return content


@app.get('/clash2', response_class=PlainTextResponse)
def clash2():
    content = main2()
    return content


@app.get('/raw/{link}', response_class=PlainTextResponse)
def clash2(link):
    content = return_raw(link)
    return content


@app.get('/one/{hub_url}')
def v2(hub_url):
    subscription_dict = get_hub_url(hub_url)
    return subscription_dict
