from WeChatPYAPI import WeChatPYApi

import time
import logging
from queue import Queue
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


logging.basicConfig(level=logging.INFO)  # 日志器
msg_queue = Queue()  # 消息队列

def on_message(msg):
    """消息回调，建议异步处理，防止阻塞"""
    print(msg)
    msg_queue.put(msg)


def on_exit(wx_id):
    """退出事件回调"""
    print("已退出：{}".format(wx_id))


def main():
    # 初次使用需要pip安装三个库：
    # pip install requests
    # pip install pycryptodomex
    # pip install psutil
    #
    # 查看帮助
    help(WeChatPYApi)

    # 实例化api对象
    w = WeChatPYApi(msg_callback=on_message, exit_callback=on_exit, logger=logging)

    # 启动微信
    w.start_wx()
    # w.start_wx(path=os.path.join(BASE_DIR, "login_qrcode.png"))  # 保存登录二维码

    # 这里需要阻塞，等待获取个人信息
    while not w.get_self_info():
        time.sleep(5)

    my_info = w.get_self_info()
    self_wx = my_info["wx_id"]
    print("登陆成功！")
    print(my_info)

    # 拉取列表（好友/群/公众号等）第一次拉取可能会阻塞，可以自行做异步处理
    # 好友列表：pull_type = 1
    # 群列表：pull_type = 2
    # 公众号列表：pull_type = 3
    # 其他：pull_type = 4
    lists = w.pull_list(self_wx=self_wx, pull_type=1)
    print(lists)

    # 获取群成员列表
    # lists = w.get_chat_room_members(self_wx=self_wx, to_chat_room="123@chatroom")
    # print(lists)

    # 发送文本消息
    w.send_text(self_wx=self_wx, to_wx="wxid_5deztcfl2fz611", msg='test\rtest')
    time.sleep(1)

    w.send_text(self_wx=self_wx, to_wx="wxid_5deztcfl2fz611", msg='test3\rtest3')
    time.sleep(1)

    while True:
        msg = msg_queue.get()
        content = msg['content']
        print(content)

if __name__ == '__main__':
    main()