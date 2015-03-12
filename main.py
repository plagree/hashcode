#!/usr/bin/env python2
#-*-coding: utf-8 -*-

import sys
from score import *

class Server:
    def __init__(self, z, c, n):
        self.line = None
        self.column = None
        self.group = None
        self.size = z
        self.capacity = c
        self.index = n

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        typeline = 0
        U_line = 0
        M_line = 0
        servers = {}
        for l in f:
            l = l.rstrip('\n')
            data = l.split(' ')
            data = [int(x) for x in data]
            if typeline == 0:
                nb_lines, S, U, nb_groups, M = data
                DC = [[0 for i in range(S)] for j in range(nb_lines)]
                typeline = 1
            elif typeline == 1:
                U_line += 1
                r, s = data
                DC[r][s] = -1
                if U_line == U:
                    typeline = 2
            elif typeline == 2:
                z, c = data
                servers[M_line] = Server(z,c,M_line)
                M_line += 1

print DC
print [(s.size, s.capacity, s.index) for s in servers.itervalues()]
print compute_score(servers.values(), nb_groups, nb_lines)
