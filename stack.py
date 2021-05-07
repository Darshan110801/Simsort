class Node:
    ele = None
    next = None

    def __init__(self, ele):
        self.ele = ele
        self.next = None


class Stack:
    __top = None

    def __init__(self):
        self.__top = None

    def push(self, ele):
        node = Node(ele)
        node.next = self.__top
        self.__top = node

    def pop(self):
        ret_val = None
        if self.__top is not None:
            node = self.__top.next
            ret_val = self.__top.ele
            self.__top = node
        return ret_val

    def top(self):
        ret_val = None
        if self.__top is not None:
            ret_val = self.__top.ele
        return ret_val

    def is_empty(self):
        return self.__top is None
