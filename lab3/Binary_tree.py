from Vector import Vector
from Queue import Queue
from Stack import Stack

def parser(s):
    tokens = Vector()
    brace_counter = 0
    i = 0
    while i != len(s):
        if s[i] == '(':
            tokens.push_back(s[i])
            brace_counter += 1
        elif s[i].isnumeric():
            temp = ''
            while s[i].isnumeric():
                temp += s[i]
                i += 1
            i -= 1
            tokens.push_back(temp)
        elif s[i].isspace():
            if s[i + 1] == ')':
                tokens.push_back(None)
        elif s[i] == ')':
            tokens.push_back(s[i])
            brace_counter -= 1
        else:
            print('Error1. Incorrect input!')
            return
        i += 1
    if brace_counter != 0:
        print('Error2. Incorrect input!')
        return
    for i in range(len(tokens)):
        if tokens[i] is not None and tokens[i].isnumeric():
            tokens[i] = int(tokens[i])
    tokens.delete(0)
    tokens.delete(len(tokens) - 1)
    return tokens

class Binary_tree:
    class __node:
        def __init__(self, data, parent=None):
            self.parent = parent
            self.left = None
            self.right = None
            self.data = data
            self.height = 1

    def __init__(self, s = '( )'):
        self.is_binary_search = False
        self.is_balanced = False

        if s == '( )':
            self.root = None
            return
        tokens = parser(s)
        self.root = self.__node(tokens[0])
        cur_node = self.root
        i = 1
        while i != len(tokens):
            if tokens[i] == '(':
                if cur_node.left == None:
                    cur_node.left = self.__node(tokens[i+1], cur_node)
                    i += 2
                    cur_node = cur_node.left
                else:
                    if cur_node.left.data == None:
                        cur_node.left = None
                    if tokens[i+1] != None:
                        cur_node.right = self.__node(tokens[i+1], cur_node)
                        cur_node = cur_node.right
                    i += 2
            elif tokens[i] == ')':
                cur_node = cur_node.parent
                i += 1

    def get_binary_search_tree(self):
        new_root = self.__node(self.root.data)
        def __traverse(Node):
            if Node == None:
                 return
            cur_node = new_root
            parent = None
            while cur_node != None:
                if Node.data < cur_node.data:
                    parent = cur_node
                    cur_node = cur_node.left
                else:
                    parent = cur_node
                    cur_node = cur_node.right
            if Node.data < parent.data and Node != self.root:
                parent.left = self.__node(Node.data, parent)
            elif Node.data >= parent.data and Node != self.root:
                parent.right = self.__node(Node.data, parent)
            __traverse(Node.left)
            __traverse(Node.right)
            while parent != None:
                self.__fixheight(parent)
                parent = parent.parent
        __traverse(self.root)

        self.root = new_root
        self.is_binary_search = True

    def __searchnode(self, data):
        temp_node = self.root
        while temp_node.data != data:
            if data < temp_node.data:
                temp_node = temp_node.left
            if data > temp_node.data:
                temp_node = temp_node.right
            if temp_node is None:
                return
        return temp_node

    def search(self, data):
        if not self.is_binary_search:
            return
        temp_node = self.__searchnode(data)
        if temp_node is not None:
            print(temp_node.data, "is found!")
        else:
            print("Is not found(")

    def __height(self, Node):
        return Node.height if Node is not None else 0

    def __bfactor(self, Node):
        return self.__height(Node.right)-self.__height(Node.left)

    def __fixheight(self, Node):
        left_h = self.__height(Node.left)
        right_h = self.__height(Node.right)
        Node.height = (left_h if left_h > right_h else right_h) + 1

    def __rotateright(self, Node):
        if Node is self.root:
            self.root = Node.left
        temp_parent = Node.parent
        Node.parent = Node.left

        if Node.left.right is not None:
            Node.left.right.parent = Node
        temp_node = Node.left
        if temp_parent is not None:
            if temp_parent.right is Node:
                temp_parent.right = temp_node
            else:
                temp_parent.left = temp_node
        temp_node.parent = temp_parent
        Node.left = temp_node.right
        temp_node.right = Node
        self.__fixheight(Node)
        self.__fixheight(temp_node)

    def __rotateleft(self, Node):
        if Node is self.root:
            self.root = Node.right
        temp_parent = Node.parent
        Node.parent = Node.right

        if Node.right.left is not None:
            Node.right.left.parent = Node
        temp_node = Node.right
        if temp_parent is not None:
            if temp_parent.right is Node:
                temp_parent.right = temp_node
            else:
                temp_parent.left = temp_node
        temp_node.parent = temp_parent
        Node.right = temp_node.left
        temp_node.left = Node
        self.__fixheight(Node)
        self.__fixheight(temp_node)

    def __balance(self, Node):
        self.__fixheight(Node)
        if self.__bfactor(Node) >= 2:
            if self.__bfactor(Node.right) < 0:
                self.__rotateright(Node.right)
            return self.__rotateleft(Node)
        if self.__bfactor(Node) <= -2:
            if self.__bfactor(Node.left) > 0:
                self.__rotateleft(Node.left)
            return self.__rotateright(Node)

    def balance_tree(self):
        if not self.is_binary_search:
            return
        self.is_balanced = True
        def __traverse(Node):
            if Node == None:
                return
            __traverse(Node.left)
            __traverse(Node.right)
            self.__balance(Node)
        __traverse(self.root)

    def insert(self, data):
        if not self.is_balanced:
            return
        temp_node = self.root
        temp_parent = None
        while temp_node is not None:
            temp_parent = temp_node
            if data > temp_node.data:
                temp_node = temp_node.right
            else:
                temp_node = temp_node.left
        if data > temp_parent.data:
            temp_parent.right = self.__node(data, temp_parent)
            self.__fixheight(temp_parent.right)
        else:
            temp_parent.left = self.__node(data, temp_parent)
            self.__fixheight(temp_parent.left)
        self.__fixheight(temp_parent)

        self.balance_tree()

    def __findmin(self, Node):
        while Node.left is not None:
            Node = Node.left
        return Node

    def __removeleaf(self, Node):
        temp_parent = Node.parent
        if temp_parent.right is Node:
            temp_parent.right = None
        if temp_parent.left is Node:
            temp_parent.left = None
        if Node.right is not None:
            temp_parent.right = Node.right

    def remove(self, data):
        if not self.is_balanced:
            return
        temp_node = self.__searchnode(data)
        if temp_node is None:
            return
        if temp_node.right is None and temp_node.left is None:
            self.__removeleaf(temp_node)
        elif temp_node.right is None:
            temp_node.data = temp_node.left.data
            self.__removeleaf(temp_node.left)
        else:
            min_node = self.__findmin(temp_node.right)
            temp_node.data = min_node.data
            self.__removeleaf(min_node)
        self.balance_tree()

    def BFS(self):
        temp_node = self.root
        que = Queue()
        que.enqueue(temp_node)
        while len(que) != 0:
            temp_node = que.dequeue()
            print(temp_node.data)
            if temp_node.left is not None:
                que.enqueue(temp_node.left)
            if temp_node.right is not None:
                que.enqueue(temp_node.right)

    def DFS_straight(self):
        temp_node = self.root
        stack = Stack()
        stack.push_back(temp_node)
        while len(stack) != 0:
            temp_node = stack.pop_back()
            print(temp_node.data)
            if temp_node.right is not None:
                stack.push_back(temp_node.right)
            if temp_node.left is not None:
                stack.push_back(temp_node.left)

    def DFS_centered(self):
        temp_node = self.root
        stack = Stack()
        while temp_node is not None or len(stack) != 0:
            if temp_node is not None:
                stack.push_back(temp_node)
                temp_node = temp_node.left
            else:
                temp_node = stack.pop_back()
                print(temp_node.data)
                temp_node = temp_node.right

    def DFS_reverse(self):
        temp_node = self.root
        stack = Stack()
        lastNodeVisited = None
        while temp_node is not None or len(stack) != 0:
            if temp_node is not None:
                stack.push_back(temp_node)
                temp_node = temp_node.left
            else:
                peek = stack.last()
                if peek.right is not None and lastNodeVisited is not peek.right:
                    temp_node = peek.right
                else:
                    print(peek.data)
                    lastNodeVisited = stack.pop_back()

































