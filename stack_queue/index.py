# https://www.interviewcake.com/question/python/queue-two-stacks

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if len(self.stack2) < 1:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

queue = MyQueue()
queue.enqueue('bob')
queue.enqueue('sam')
queue.enqueue('alex')
print('dequeue', queue.dequeue())
queue.enqueue('rebecca')
print(queue.dequeue(), queue.dequeue(), queue.dequeue())