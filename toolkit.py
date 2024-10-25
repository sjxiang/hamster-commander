import requests
import json


prompt = "你是一个将用户的需求转化为 linux 命令的机器人，你将用户发来的需求转化为 linux 命令行下的命令，你只回复命令本身，不回复任何其它内容。\n"


def foo(content: str) -> str:
    url = "https://spark-api-open.xf-yun.com/v1/chat/completions"
    
    data = {
        "max_tokens": 4096,
        "top_k": 4,
        "temperature": 0.5,
        "messages": [
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": content  # "请在此处输入你的问题!!!"
            }
        ]
    }
    data["model"] = "generalv3.5"           
    header = {
        "Authorization": "Bearer xx" # 注意此处替换自己的APIPassword
    }    
    response = requests.post(url, headers=header, json=data)  
    
    return response.text
