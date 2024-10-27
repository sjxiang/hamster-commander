import sys
from utils import chat_mode
from commander import Commander, SecretStore


def main(args=sys.argv[1:]):

    if (len(args) == 0):
        raise Exception("请告诉我你想做什么")
    
    input = args[0]    
    
    # 获取密钥
    ss = SecretStore.new()
    password = ss.get()
    
    # 生成命令
    cc = Commander(password)
    print(cc.generate_command(input))
    
    
if __name__ == '__main__':
    main()
    
