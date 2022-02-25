# –– coding: utf-8 ––
from threading import thread

class MyThread(thread):
    def run(self):
        print('Hola del thread %s'%self.name)

for i in range(3):
    my_thread = MyThread()
    my_thread.name = i
    my_thread.start()
