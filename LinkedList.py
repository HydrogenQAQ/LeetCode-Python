# Author: Jin

"""
单链表
"""


class Node:
    """
    节点类
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class List:
    """
    链表类
    """

    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, value):
        this_node = Node(data=value)
        if self.root is None:
            self.root = this_node
            return
        temp = self.root
        # 找到链表末尾
        while temp.next:
            temp = temp.next
        temp.next = this_node
        self.size += 1

    def __del__(self):
        pass


    def getData(self):
        pass

    def remove(self):
        pass

    def getSize(self):
        return self.size

    def getRoot(self):
        return self.root

mylist = List()
mylist.insert(2)