import json
import os
import requests
from datetime import datetime


def log(*args, **kwargs):
    now = datetime.now()
    formatted_date = now.strftime('%Y/%m/%d %H:%M:%S')
    print('<log>', formatted_date, *args, **kwargs)

        
def dotenv_file_path():
    current_dir = os.path.dirname(__file__)  # 获取当前脚本所在目录的路径
    return '{}/env.txt'.format(current_dir)
        

def load(path):
    """
    本函数从一个文件中载入数据并转化为 dict 或者 list
    path 是保存文件的路径
    """
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        log('load', s)
        return json.loads(s)
    

def save(data, path):
    """
    本函数把一个 dict 或者 list 写入文件
    data 是 dict 或者 list
    path 是保存文件的路径
    """
    
    # json 是一个序列化/反序列化 list/dict 的库
    # indent 是缩进
    # ensure_ascii=False 用于保存中文
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        log('save', path, s, data)
        f.write(s)


def chat_mode(input: str) -> str:
    url = "https://spark-api-open.xf-yun.com/v1/chat/completions"

    messages = [
        { "role": "system", "content": f"""
        你是一个将用户的需求转化为 linux 命令的机器人，你将用户发来的需求转化为 linux 命令行下的命令，你只回复命令本身，不回复任何其它内容。
        """},
        { "role": "user", "content": input}  # "请在此处输入你的问题!!!"
    ]
    
    json_obj = {
        "max_tokens": 4096,
        "top_k": 4,
        "temperature": 0.5,
        "messages": messages,
        "model": "generalv3.5"
    }
    
    payload = json.dumps(json_obj)       
    headers = {
        "Authorization": "Bearer xx" # 注意此处替换自己的APIPassword
    }    
    
    response = requests.request('POST', url, headers=headers, data=payload)
    json_result = json.loads(response.text)

    if 'choices' in json_result:
        return further_process(json_result)
    else:
        return json_result    


def further_process(result: dict) -> str:
    choices = result['choices']
    first_choices = choices[0]
    message = first_choices['message']
    content = message['content']
    
    return content