class Queue:
    # 队列
    def __init__(self):
        self.__list = []

    def enqueue(self,item):
    # 入队
        self.__list.append(item)

    def dequeue(self):
    # 出队
        if self.__list:
            return self.__list.pop(0)
        else:
            return None

    def is_empty(self):
    # 判空
        return self.__list == []

    def size(self):
    # 返回大小
        return len(self.__list)

if __name__ == '__main__':
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
