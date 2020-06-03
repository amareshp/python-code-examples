import os
import fcntl
import time
import random
import errno
from multiprocessing import Process
from my_constants import constants

def lock_with_wait(file_obj):
    while True:
        try:
            fcntl.flock(file_obj, fcntl.LOCK_EX | fcntl.LOCK_NB)
            print(f'lock acquired: pid: {os.getpid()}, ppid: {os.getppid()}')
            break
        except IOError as e:
            # raise on unrelated IOErrors
            if e.errno != errno.EAGAIN:
                raise
            else:
                print(f'waiting to acquire lock: pid: {os.getpid()}, ppid: {os.getppid()}')
                time.sleep(1)

def f(file_path):
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    file_obj = open(file_path, 'w+')
    lock_with_wait(file_obj)
    # fcntl.flock(file_obj, fcntl.LOCK_EX | fcntl.LOCK_NB)
    time.sleep(20 * random.random())
    fcntl.flock(file_obj, fcntl.LOCK_UN)
    file_obj.close()

def main():
    file_path = f'{constants.BASE_PATH}/app_cntl.lck'
    processes = []
    for i in range(5):
        p1 = Process(target=f, args=(file_path,))
        p1.start()
        time.sleep(1)
        processes.append(p1)

    for p in processes:
        p.join()

    print('Done...')

if __name__ == '__main__':
    print(constants.BASE_PATH)
    main()
