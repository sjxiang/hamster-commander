import json
import os
import requests
from datetime import datetime


def log(*args, **kwargs):
    now = datetime.now()
    formatted_date = now.strftime('%Y/%m/%d %H:%M:%S')
    print('<log>', formatted_date, *args, **kwargs)


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


def generate_process(query: str) -> str:
    """ 
    生成流程：调用星火认知大模型 Web API，根据查询生成最终回复
    :param query: 用户输入的查询
    :return: 返回生成的响应内容
    """

    # 设置
    url = "https://spark-api-open.xf-yun.com/v1/chat/completions"
    model = 'generalv3.5'
    api_key = os.getenv('password')

    # 构建生成模型所需的 prompt, 包含用户查询和检索的上下文
    prompt = f"""{query}, 记住你是一个将用户的需求转化为 linux 命令的机器人，你将用户发来的需求转化为 linux 命令行下的命令，你只回复命令本身，不回复任何其它内容。
    示例1：
    用户：打印日期
    系统：date"""
    
    # 准备请求消息, 将 prompt 作为输入
    messages = [{ "role": "user", "content": prompt}]
    
    # 调用星火认知大模型 API, 生成响应
    try:
        payload = dict(
            max_tokens=4096,
            top_k=4,
            temperature=0.5,
            messages=messages,
            model=model
        )   
        headers = {
            "Authorization": "Bearer {}".format(api_key) 
        }   
        
        response = requests.request('POST', url, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            print('\n生成过程完成.')
            return extract_content(response.json())
        else:
            print(f"请求失败：{response.status_code} - {response.text}")
            return None
        
    except Exception as e:
        print(f"大模型生成过程中发生错误：{e}")
        return None   


def extract_content(dic):
    return dic['choices'][0]['message']['content']
    

def test_extract_content():
    """ 测试是否能正确提取内容 """
    dic = {'code': 0, 'message': 'Success', 'sid': 'cha000b231a@dx192cced4bdfb8f2532', 'choices': [{'message': {'role': 'assistant', 'content': 'date'}, 'index': 0}], 'usage': {'prompt_tokens': 62, 'completion_tokens': 1, 'total_tokens': 63}}

    content = extract_content(dic)
    assert content == 'date'


def test_generate_process():
    test_items = [
        ('输出当前时间', ('date')),
        ('查看当前进程', ('ps aux')),
    ]
    
    for t in test_items:
        query, expected = t
        content = generate_process(query)    
        e = "generate process ERROR, ({}) ({}) ({})".format(query, content, expected)
        assert content == expected, e


def test():
    """
    用于测试的主函数
    """
    test_extract_content()
    

if __name__ == '__main__':
    test()
    
    
