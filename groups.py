

def assign_groups(DC, servers, nb_groups):
    print ""
    groups = [{"group_id": i, "values": []} for i in range(nb_groups)]
    for line in DC:
        print line
        groups.sort(key=lambda g: sum([s.capacity for s in g["values"]]))
        line_servers = list(set([s for s in line if s != -1 and s is not None]))
        print line_servers
        line_servers.sort(key=lambda s: -servers[s].capacity)
        for i in range(len(line_servers)):
            server = servers[line_servers[i]]
            server.group = groups[i]["group_id"]
            groups[i]["values"].append(server)
    print ""
    print groups
    return groups
