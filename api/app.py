from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from api.v2 import get_sub_url
from api.clash import main
from api.clash2 import main2
from api.raw import return_raw
from api.one import get_hub_url
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 声明一个 源 列表；重点：要包含跨域的客户端 源
origins = ["https://node-drw.pages.dev"]

# 配置 CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许访问的源
    allow_credentials=True,  # 支持 cookie
    allow_methods=["*"],  # 允许使用的请求方法
    allow_headers=["*"]  # 允许携带的 Headers
)


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


@app.get('/raw/', response_class=PlainTextResponse)
def clash2(url):
    content = return_raw(url)
    return content


@app.get('/one/')
def v2(url):
    subscription_dict = get_hub_url(url)
    return subscription_dict
