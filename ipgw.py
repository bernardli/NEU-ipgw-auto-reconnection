import time
import random
import sys
from network import Network
from logger import Logger
from config import config


def main():
    net = Network()
    log = Logger()
    patience = 5
    failTimes = 0

    # 这里暂时先用阻塞式的方式
    while True:
        time.sleep(60 + random.random() * 10)
        if not net.check():
            print('net error!')

            failTimes += 1
            if failTimes == patience:
                # 连续多次连不上可能是余额不足之类的问题
                # 反正先写个限制避免登录不上还一直重连
                print('maybe something wrong')
                break
            log.save()

            if config['mode'] == '1':
                net.NonUnifiedLogin()
            elif config['mode'] == '2':
                net.unifiedLogin()
        else:
            failTimes = 0
            # print('everything ok')


if __name__ == "__main__":
    main()
