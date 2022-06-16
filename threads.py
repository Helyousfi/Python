from time import sleep, perf_counter

def task():
    print('Starting a task...')
    sleep(1)
    print('done')
    
#-----------------------------------------------------------------------#
#--------------------------- Before threads ----------------------------#
#-----------------------------------------------------------------------#
start_time = perf_counter()
task()
task()
end_time = perf_counter()

print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')

#-----------------------------------------------------------------------#
#--------------------------- After threads -----------------------------#
#-----------------------------------------------------------------------#
start_time = perf_counter()
# create two new threads
t1 = Thread(target=task)
t2 = Thread(target=task)
# start the threads
t1.start()
t2.start()
# wait for the threads to complete
t1.join()
t2.join()
end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')



"""
# To get the return value back store the results in a database
from threading import Thread
result = {}

def foo(bar):
    print('hello {}'.format(bar))
    result[str(bar)] = bar

thread1 = Thread(target=foo, args=('world!',))
thread2 = Thread(target=foo, args=('wold2!',))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(result)
"""
