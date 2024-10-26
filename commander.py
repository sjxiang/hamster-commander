import os
from utils import log, dotenv_file_path, load, save


class Commander(object):
    
    def __init__(self) -> None:
        self.api_password = ''
    
    def generate_command(self, content: str) -> str:
        pass
    
    

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
    
    pass
        
if __name__ == '__main__':
    double_s = SecretStore.new()
    
    double_s.set('123456')
    assert double_s.get() == '123456'
    