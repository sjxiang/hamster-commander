import sys
import toolkit


def generate_command(content: str):
    reply = toolkit.foo(content)
    print(reply)


def main(args=sys.argv[1:]):

    if (len(args) == 0):
        raise Exception("参数为空, 请告诉我你想做什么")
    
    content = args[0]    
    generate_command(content)
   
    
    
if __name__ == '__main__':
    main()
    
