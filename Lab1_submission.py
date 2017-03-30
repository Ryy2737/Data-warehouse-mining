## import modules here 
import math
import queue
################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    sqrt_num=int(math.sqrt(x))
    return  sqrt_num # **replace** this line with your code


################# Question 2 #################

'''
x_0: initial guess
EPSILON: stop when abs(x - x_new) < EPSILON
MAX_ITER: maximum number of iterations

NOTE: you must use the default values of the above parameters, do not change them
'''
def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    i=0
    delta=x_0
    while i<MAX_ITER and delta > EPSILON:
        x_1 = x_0 - f(x_0)/fprime(x_0)
        delta = abs(x_1-x_0)
        x_0=x_1
        i=i+1
    return x_0

################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def make_tree(tokens): # do not change the heading of the function
    stack = queue.LifoQueue()
    parent, root = None, None
    for i in range(len(tokens)):
        c=tokens[i]
        if c == '[':
            stack.put_nowait(node)
            parent = stack.get_nowait()
            stack.put_nowait(parent)
        elif c == ']':
            stack.get_nowait()
            if stack.qsize() != 0:
                parent=stack.get_nowait()
                stack.put_nowait(parent)
        else:
            node = Tree()
            node.name = c
            if parent is None:
                root = node
            else:
                parent.add_child(node)
    return root 

def max_depth(root): # do not change the heading of the function
    subdepth = 0
    if root.children:
        subdepth+=1
        num=[]
        for i in root.children:
            num.append(max_depth(i))
        subdepth=max(num)
        subdepth += 1
        return subdepth
    else:
        subdepth+=1
        return subdepth # **replace** this line with your code

def max_depth(root):
    subdepth=0
    deepest=1
    if root.children:
        subdepth+=1
        for i in root.children:
            max_depth(i)
        print (subdepth)
        return subdepth
    else:
        deepest=max(deepest,subdepth)
        return subdepth



        