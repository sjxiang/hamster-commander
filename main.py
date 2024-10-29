import sys
from commander import Commander


def main(args=sys.argv[1:]):

    if (len(args) == 0):
        raise Exception("请告诉我你想做什么")
    
    input = args[0]    
    
    # 生成命令
    cc = Commander.new()
    print(cc.run(input))
    
    
if __name__ == '__main__':
    main()
    
