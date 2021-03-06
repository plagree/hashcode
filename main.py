#!/usr/bin/env python2
#-*-coding: utf-8 -*-

import sys
from groups import *
from score import *
from assignement import *
from random import *

class Server:
    def __init__(self, z, c, n):
        self.line = None
        self.column = None
        self.group = None
        self.size = z
        self.capacity = c
        self.index = n

    def __repr__(self):
        return "<Server: line: %d, column: %d, group: %d, size: %d, capacity: %d, index: %d>" % (
            self.line, self.column, self.group, self.size, self.capacity, self.index)

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
                DC = [[None for i in range(S)] for j in range(nb_lines)]
                typeline = 1
            elif typeline == 1:
                U_line += 1
                r, s = data
                DC[r][s] = -1
                if U_line == U:
                    typeline = 2
            elif typeline == 2:
                z, c = data
                servers[M_line] = Server(z, c, M_line)
                M_line += 1
    put_servers(DC, servers, nb_lines, S)
    assign_groups(DC, servers, nb_groups)


def write_output(servers):
    f = open('output.in', 'w')
    for server in servers:
        if server.group is None or server.line is None or server.column is None:
            f.write("x\n")
        else:
            f.write("%d %d %d\n" % (server.line, server.column, server.group))
    f.close()

print DC
print [(s.size, s.capacity, s.index) for s in servers.itervalues()]

previous = compute_score(servers.values(), nb_groups, nb_lines)
def switch(a, b):
    c = a.group
    a.group = b.group
    b.group = c

for i in range(500):
    a = randint(0, len(servers)-1)
    b = randint(0, len(servers)-1)
    switch(servers[a], servers[b])
    new = compute_score(servers.values(), nb_groups, nb_lines)
    if new > previous:
        previous = new
    else:
        switch(servers[a], servers[b])
    print compute_score(servers.values(), nb_groups, nb_lines)


write_output(sorted(servers.values(), key=lambda m:m.index))
