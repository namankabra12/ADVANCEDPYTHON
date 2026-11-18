import threading
import time
import queue


def print_squares():
    for i in range(1, 6):
        print("Square of", i, "=", i * i)
        time.sleep(0.5)


def print_cubes():
    for i in range(1, 6):
        print("Cube of", i, "=", i ** 3)
        time.sleep(0.5)


def print_message():
    for i in range(3):
        print("Hello from thread", i + 1)
        time.sleep(0.8)


t1 = threading.Thread(target=print_squares)
t2 = threading.Thread(target=print_cubes)
t3 = threading.Thread(target=print_message)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print("All tasks finished\n")


count = 0
lock = threading.Lock()


def increase():
    global count
    for _ in range(100000):
        with lock:
            count += 1


threads = []
for _ in range(4):
    t = threading.Thread(target=increase)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("Final count:", count, "\n")


q = queue.Queue()


def producer():
    for i in range(5):
        print("Produced", i)
        q.put(i)
        time.sleep(0.3)
    q.put(None)


def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print("Consumed", item)


p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start()
c.start()
p.join()
c.join()
print("Done")
