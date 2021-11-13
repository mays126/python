import random

def push(queue, value):
    queue.append(value)

queue = []
print(queue)

for i in range(10):
    push(queue, i)
print(queue)
queue.reverse()
print(queue)
