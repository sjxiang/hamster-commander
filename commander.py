import os
from utils import load, generate_process


class Commander(object):
        
    def run(self, input: str) -> str:
        return generate_process(input)

            
    def init_env(self) -> None:
        # 当前目录
        current_dir = os.path.dirname(__file__)
        # 文件路径
        path = '{}/env.txt'.format(current_dir)
        # 获取密钥
        password = load(path)['password']        
        # 设置一个新的环境变量
        os.environ['password'] = password


    @classmethod
    def new(cls):
        c = cls()
        c.init_env()        
        return c
    
