#!python3
#stack implementation
class stack():
    def __init__(self):
        self.stack = []
    def push(self,thing):
        self.stack.append(thing)
    def pop(self):
        return self.stack.popleft()
    def isempty(self):
        return isempty(stack)
