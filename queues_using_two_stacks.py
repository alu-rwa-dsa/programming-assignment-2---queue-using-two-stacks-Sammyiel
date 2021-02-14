# Starting with stacks class

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None


# To be linked to stacks class

class Queue:
    def __init__(self):
        self.front = Stack()
        self.end = Stack()

    def enqueue(self, x):
        self.end.push(x)

    def dequeue(self):
        if self.front:
            return self.front.pop()
        return self.replace_front().pop()

    def peek(self):
        if self.front:
            return self.front.top()
        return self.replace_front().top()

    def replace_front(self):
        while self.end:
            self.front.push(self.end.pop())
        return self.front


# Function to read from standard input

def from_stdin():
    lines = input().strip()
    line = lines.split()
    the_type = int(line[0])

    if len(line) == 1:
        return (the_type, None)

    num = int(line[1])

    return the_type, num


# Calling all functions

def main():
    q = Queue()
    queries = int(input().strip())

    for z in range(queries):
        the_type, num = from_stdin()

        if the_type == 1:
            q.enqueue(num)

        elif the_type == 2:
            q.dequeue()

        elif the_type == 3:
            print(q.peek())


if __name__ == '__main__':
    main()
