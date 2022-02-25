# –– coding: utf-8 ––
import _thread

def hola(nbr):
    print("Hola del thread %s"%nbr)

_thread.start_new_thread(hola, (0,))
_thread.start_new_thread(hola, (1,))
_thread.start_new_thread(hola, (2,))
