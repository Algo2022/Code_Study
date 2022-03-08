from sys import stdin
from collections import defaultdict

class Mem():
    def __init__(self):
        self.mem = {1: [100000, False, 0, 0]}

    def malloc(self, size):
        addr = 0
        done = False
        curr = 1
        while True:
            length, allocated, left, right = self.mem[curr]
            if not allocated:
                if not done and length > size:
                    self.mem[curr] = [size, True, left, curr+size]
                    self.mem[curr+size] = [length-size, False, curr, right]
                    if right: self.mem[right][2] = curr+size
                    done = True
                    addr = curr
                elif not done and length == size:
                    self.mem[curr] = [size, True, left, right]
                    done = True
                    addr = curr
            if not right: break
            curr = right
        return addr

    def free(self, addr):
        if addr:
            length, _, left, right = self.mem.pop(addr)
            if left and self.mem[left][1] == False:
                if right and self.mem[right][1] == False:
                    rlength, _, _, rright = self.mem.pop(right)
                    self.mem[left][0] += length + rlength
                    self.mem[left][3] = rright
                    if rright: self.mem[rright][2] = left
                else:
                    self.mem[left][0] += length
                    self.mem[left][3] = right
                    self.mem[right][2] = left
            else:
                if right and self.mem[right][1] == False:
                    rlength, _, _, rright = self.mem.pop(right)
                    self.mem[addr] = [length+rlength, False, left, rright]
                    if rright: self.mem[rright][2] = addr
                else:
                    self.mem[addr] = [length, False, left, right]

inst_list = []
for _ in range(int(stdin.readline())):
    inst_list.append(stdin.readline().strip())

mem = Mem()
env = defaultdict(int)

for inst in inst_list:
    if inst.startswith("print"):
        print(env[inst[6:-2]])
    elif inst.startswith("free"):
        mem.free(env[inst[5:-2]])
        env[inst[5:-2]] = 0
    else:
        var_name, malloc_call = inst.split("=")
        env[var_name] = mem.malloc(int(malloc_call[7:-2]))

