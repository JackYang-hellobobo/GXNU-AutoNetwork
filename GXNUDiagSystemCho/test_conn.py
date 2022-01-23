import requests


def isConnected():
    try:
        baidu_html = requests.get("https://www.baidu.com", timeout=2)
        qq_html = requests.get("https://www.qq.com", timeout=2)
        bilibli_html = requests.get("https://www.bilibili.com", timeout=2)
    except:
        return False
    return True


if __name__ == "__main__":
    print(isConnected())
