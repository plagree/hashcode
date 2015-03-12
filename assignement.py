from random import shuffle

def server_has_space(server, DC, line, column, S):
    if server.size+column > S:
        return False
    for j in range(column, column+server.size):
        if DC[line][j] is not None:
            return False
    return True

def put_servers(DC, servers, nb_lines, S):
    sortedServers = sorted(servers.values(), key=lambda x: [x.capacity, x.size], reverse=True)
    line = 0
    column = 0
    lines = range(nb_lines)
    #shuffle(lines)
    for server in sortedServers:
        currLine = line
        while(True):
            if server_has_space(server, DC, lines[line], column, S):
                server.line = lines[line]
                server.column = column
                for j in range(column, column+server.size):
                    DC[lines[line]][j] = server.index
                line += 1
                if line == nb_lines:
                    pass #lines = sorted(lines, key=lambda l: DC[l].count(None))
                line %= nb_lines
                break
            column += 1
            if column == S:
                column = 0
                line += 1
                line %= nb_lines
                if line == nb_lines:
                    pass #lines = sorted(lines, key=lambda l: DC[l].count(None))
                if line == currLine:
                    break

