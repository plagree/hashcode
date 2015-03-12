
def server_has_space(server, DC, line, column, S):
    if server.size+column > S:
        return False
    for j in range(column, column+server.size):
        if DC[line][j] is not None:
            return False
    return True

def put_servers(DC, servers, nb_lines, S):
    sortedServers = sorted(servers.values(), key=lambda x: x.size, reverse=True)
    line = 0
    column = 0
    for server in sortedServers:
        currLine = line
        while(True):
            if server_has_space(server, DC, line, column, S):
                server.line = line
                server.column = column
                for j in range(column, column+server.size):
                    DC[line][j] = server.index
                line += 1
                line %= nb_lines
                break
            column += 1
            if column == S:
                column =0
                line += 1
                line %= nb_lines
                if line == currLine:
                    break

