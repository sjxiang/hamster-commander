import os
from utils import dotenv_file_path, load, save, chat_mode


class Commander(object):
    
    def __init__(self, password=None) -> None:
        self.password = password
    
    def generate_command(self, input: str) -> str:
        
        if self.is_empty():
                raise Exception('请先设置 env.txt 文件的 password')
        
        # 设置一个新的环境变量
        os.environ['password'] = self.password
        
        return chat_mode(input)
    
    
    def is_empty(self) -> bool:
        return self.password is None or len(self.password) == 0
        

class SecretStore(object):
    
    """ 密钥存储 """
     
    def __init__(self) -> None:
        self.path = ''
    
    def set(self, password: str) -> None:
        data = dict(
            password=password,
        )
        save(data, self.path)           
    
    
    def get(self):
        if self.exists():
            return load(self.path)['password']
        else:
            raise Exception('文件不存在')
    
    
    def exists(self) -> bool:
        if os.path.exists(self.path):
            return True
        else:
            return False
            
    
    @classmethod
    def new(cls):
        s = cls()
        s.__setattr__('path', dotenv_file_path())
        return s


def test_secret_store():
    double_s = SecretStore.new()
    
    password = os.urandom(23).__str__()
    double_s.set(password)
    
    assert double_s.get() == password
    
    
def test():
    test_secret_store()
    

if __name__ == '__main__':
    test()