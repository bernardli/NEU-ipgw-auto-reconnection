import time


class Logger:
    def __init__(self):
        pass

    def save(self):
        with open('./history.txt', 'a') as f:
            currTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write(currTime + '\n')
