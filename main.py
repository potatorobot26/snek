import sys

#reads arguments 
program_filepath = sys.argv[1]

# read file lines 
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]

program = []
token_counter = 0
label_tracker = {}
for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    # check if line is empty
    if opcode =="":
        continue
    # check if label
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue
    #store opcode data
    program.append(opcode)
    token_counter += 1

    # handle each opcode
    if opcode == "PUSH":
        # expecting a number
        number = int(parts[1])
        program.append(number)
        token_counter += 1
    elif opcode == "PRINT":
        # parse string literal
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
        token_counter += 1
    elif opcode == "JUMP.EQ.0":
        # read a label
        label = parts[1]
        program.append(label)
        token_counter += 1 

    elif opcode == "JUMP.GT.0":
        # read a label
        label = parts[1]
        program.append(label)
        token_counter += 1 


print(program)

class Stack:
    
    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp    = -1

    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number


    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number
    
    def print_pop(self):
        number = self.pop()
        print(number)
        return number
    
    def top(self):
        return self.buf[self.sp]
    


pc = 0
stack = Stack(256)

while program[pc] != "HALT":
    opcode = program[pc]
    pc += 1

    if opcode == "PUSH":
        number = program[pc]
        pc += 1

        stack.push(number)
    
    elif opcode == "POP":
        stack.pop()
    elif opcode == "ADD":
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)

    elif opcode == "MULTIPLY":
        a = stack.pop()
        b = stack.pop()
        print(a*b)

    elif opcode == "MULTIPLY_3NUMS":
        a = stack.pop()
        b = stack.pop()
        c = stack.pop()
        print(a*b*c)

    elif opcode == "MIRROR":
        mirrored = stack.pop()
        print(mirrored)

    elif opcode == "SUB":
        a = stack.pop()
        b = stack.pop()
        stack.push(a-b)

    elif opcode == "PRINT":
        string_literal = program[pc]
        pc += 1
        print(string_literal)

    elif opcode == "READ":
        number = int(input())
        stack.push(number)

    elif opcode == "JUMP.EQ.0":
        number = stack.top()
        if number == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    
    elif opcode == "JUMP.GT.0":
        number = stack.top()
        if number > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "POP_PRINT":
        stack.print_pop()