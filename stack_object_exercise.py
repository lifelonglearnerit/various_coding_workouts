"""Why to build your own data type? - Because it's set of behaviours and properties in one data structure.
Building Stack Object Type:
-----------------------------------------
Stack of pancakes:
Behaviours:
>> you can put one on the top
>> you can take one from the top
>> you can add many on the top
>> you can take many from the top
------------------------------------------
Additional features:
>> creating and returning copy of itself to prevent user mutating class attribute
>> checking size of the stack
>> pretty printing stack

"""
class Stack(object):
    #  constructor
    def __init__(self):
        self.stack = []
    #  methods
    def get_stack(self):
        return self.stack.copy()
    def get_size(self):
        return f"Size of stack is {len(self.stack)}"
    def print_stack(self):
        for item in self.stack[::-1]:
            print("|_" + item + "_|")


    def add_item(self, item):
        self.stack.append(item)

    def remove_item(self):
        self.stack.pop()


    def add_many(self, item, many):
        for i in range(many):
            self.stack.append(item)

    def remove_many(self, many):
        for i in range(many):
            self.stack.pop(many)

t = Stack()
IT = Stack()
t.add_many('Cheers! t.', 5)
IT.add_many('Into the IT', 8)
print(t.get_size())
print(IT.get_size())
t.print_stack()
IT.print_stack()
