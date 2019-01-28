import os 

print('Process (%s) start ...'% os.getpid())

pid = os.fork()
if pid == 0:
	print("I am child process (%s) and my parent is %s."%(os.getpid(),os.getppid()))
else:
	print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


from multiprocessing import Process, Queue 
import os, time, random 

# 写数据进程执行代码
def write(q):
	print('Process to write: %s'%os.getpid())
	for value in ['a','b','c']:
		print("Put %s to queue."% value)
		q.put(value)
		time.sleep(random.random())

# 读进程执行的代码：
def read(q):
	print('Process to read: %s'% os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.'% value)

if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))

	pw.start()
	pr.start()
	pw.join()
	pr.terminate()