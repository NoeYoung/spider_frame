import queue
import threading


class Core(object):

    def __init__(self, max_thread=10):
        self.mQueue = queue.Queue()
        self.maxThread = max_thread
        self.threadList = []

    def put_data(self, data):
        self.mQueue.put(data)

    def get_data(self):
        try:
            output = self.mQueue.get(block=False)
        except queue.Empty:
            return "None"

        return output

    def run(self):
        for i in range(1, self.maxThread+1):
            self.threadList[i] = threading.Thread(target=self.operation)
            self.threadList[i].start()

        for i in range(1, self.maxThread+1):
            self.threadList[i].join()

    def operation(self):
        pass

if __name__ == "__main__":
    threading._main_thread
