import requests
import os
import tkinter

hosts = os.path.expandvars("%SystemRoot%") + '\\System32\\drivers\\etc\\hosts2'


def request(url):
    test = 3
    while test:
        try:
            r = requests.get(url, timeout=30)  # 设置超时
            r.encoding = 'utf-8'
            r.raise_for_status()
            return r
        except requests.Timeout as e:
            err = tkinter.Label(top, text="连接超时")
            err.pack()
            print("超时 " + str(e))
        except requests.ConnectionError as e:
            err = tkinter.Label(top, text="连接错误" + str(e))
            err.pack()
            print("连接错误 " + str(e))
        except Exception as e:
            err = tkinter.Label(top, text=str(e))
            err.pack()
            print("错误原因 " + str(e))
            break
        test -= 1


def btnStart():
    content = request('https://raw.githubusercontent.com/racaljk/hosts/master/hosts')
    try:
        f = open(hosts, 'w')
        f.write(content.text)
    except IOError as e:
        err = tkinter.Label(top, text="权限不足，请以管理员权限运行", justify='center')
        err.pack()
        print("权限不足")
        print(str(e))
    else:
        f.close()
        succeed = tkinter.Label(top, text="更新成功", justify='center')
        succeed.pack()


if __name__ == "__main__":
    top = tkinter.Tk()
    top.title('更新Hosts')
    top.geometry('320x120')
    btn = tkinter.Button(top, text="开始更新", command=btnStart)
    btn.pack()
    top.mainloop()
