# encoding:utf-8
def operateLog():
    """该方法作用是：处理生成日志中的重复行"""
    rfd=open("F:\\testresult\\logs\\resultlog.txt",'r')
    wfd=file("F:\\testresult\\logs\\resultlogNew.txt",'w')
    h={}
    for i in rfd:
        if not h.has_key(i):
            h[i]=1
            wfd.write(i)
            wfd.write("\n")

def main():
    operateLog()


if __name__=="__main__":
    main()