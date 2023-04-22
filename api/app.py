from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from api.v2 import get_sub_url
from api.clash import main
from api.clash2 import main2
from api.raw import raw

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
    content = raw(link)
    return content
