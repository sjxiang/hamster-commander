import sys
from utils import chat_mode


def generate_command(input: str) -> str:
    if input is not None and len(input.strip()) > 0:
        return chat_mode(input)


def main(args=sys.argv[1:]):

    if (len(args) == 0):
        raise Exception("参数为空, 请告诉我你想做什么")
    
    content = args[0]    
    cmd = generate_command(content)
    print(cmd)
    
    
if __name__ == '__main__':
    main()
    
