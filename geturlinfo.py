import socket
import time
import re
from urllib.parse import urlparse
def urlinfo():
    f2=open('urlresult_%s.csv'%(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())),'a')
    a=','
    b='\n'
    f2.write("url,ip,port,scheme\n")
    with open("urls.txt", "r") as f:#把要检测的URL放进urls.txt
        for line in f:
            try:
                l = line.strip()
                url = urlparse(l)
                ip = str(url.hostname)
                port=str(url.port)
                scheme=str(url.scheme)
                if port == 'None':#URL不带端口时，通过协议来判断
                    if scheme == 'http':
                        port='80'
                    if scheme == 'https':
                        port='443'
                print(l,ip,port,scheme)
                if re.match(
                        r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                        ip):#如果URL中的hostname是IP格式，就直接写入
                        f2.write(l+a+ip+a+port+a+scheme+b)
                        
                else:
                    try:#解析成功，写入csv文件
                        getIP = socket.gethostbyname(str(ip))
                        
                        f2.write(l+a+getIP+a+port+a+scheme+b)
                    except Exception as e:#解析失败，就不存入解析出的IP，但是其他信息照样写入
                        getIP = socket.gethostbyname(str(url.path))
                        print(str(getIP))
                        f2.write(l+a+getIP+a+port+a+scheme+b)
                        
            except Exception as e:#显示未知错误
                print(e)
                f2.write(l+a+a+port+a+scheme+b)
    f2.close()
if __name__ == '__main__':
    urlinfo()
    print("END")
