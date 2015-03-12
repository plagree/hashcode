
def server_has_space(server, DC, line, column, S):
    if server.size+column > S:
        return False
    for j in range(column, column+server.size):
        if DC[line][j] is not None:
            return False
    return True

def put_servers(DC, servers, nb_lines, nb_lines, S):
    sortedServers = sorted(servers.values(), key=lambda x: x.size, reverse=True)
    line = 0
    column = 0
    for server in sortedServers:
        while(True):
            if server_has_space(server, DC, line, column, S):
                for j in range(column, column+server.size):
                    DC[line][column] = server.index
                line += 1
                line %= line
                break
            column += 1
            if column == S:
                column =0
                line += 1
                line %= nb_lines

