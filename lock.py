import time
from threading import Thread

THREADS = 3
def main():
    manager = ThreadManager()
    manager.start(THREADS)

class ThreadManager:
    def __init__(self):
        pass

    def start(self, threads):
        thread_refs = []
        for i in range(threads):
            t = MyThread(i)
            t.daemon = True
            print('Inicio del thread %i'%i)
            t.start()
        for t in thread_refs:
            t.join()

class MyThread(Thread):
    def __init__(self, i):
        Thread.__init__(self)
        self.i = i
    def run(self):
        while True:
            print('Hola del thread # %i'%self.i)
            timr.sleep(.25)

if __name__ == '__main__':
    main()
