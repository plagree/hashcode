#!/usr/bin/env python
#-*-coding: utf-8 -*-

import sys

class Server:
    def __init__(self, z, c):
        self.line = None
        self.group = None
        self.size = z
        self.capacity = c

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        typeline = 0
        U_line = 0
        M_line = 0
        servers = []
        for l in f:
            l = l.rstrip('\n')
            data = l.split(' ')
            data = [int(x) for x in data]
            if typeline == 0:
                R, S, U, P, M = data
                DC = [[None for i in range(S)] for j in range(R)]
                typeline = 1
            elif typeline == 1:
                U_line += 1
                r, s = data
                DC[r][s] = -1
                if U_line == U:
                    typeline = 2
            elif typeline == 2:
                M_line += 1
                z, c = data
                servers.append(Server(z,c))







