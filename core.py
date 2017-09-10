import queue
import threading
import random


class Core(object):

    def __init__(self, max_thread=10):
        self.mQueue = queue.Queue()
        self.maxThread = max_thread
        self.threadList = []

    def put_data(self, data):
        self.mQueue.put(data)

    def get_data(self):
        output = self.mQueue.get()

        return output

    def run(self):
        for i in range(0, self.maxThread):
            self.threadList.append(threading.Thread(target=self.operation))
            self.threadList[i].start()

        for i in range(0, self.maxThread):
            self.threadList[i].join()

        self.threadList = []

        for i in range(0, self.maxThread):
            self.threadList.append(threading.Thread(target=self.operation2))
            self.threadList[i].start()

        for i in range(0, self.maxThread):
            self.threadList[i].join()

    def operation(self):
        self.put_data(random.randint(1, 10))

    def operation2(self):
        print(self.get_data())

if __name__ == "__main__":
    newCore = Core()
    newCore.run()
