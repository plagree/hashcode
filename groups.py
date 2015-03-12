

def assign_groups(DC, servers, nb_groups):
    groups = [{"group_id": i, "values": []} for i in range(nb_groups)]
    for line in DC:
        groups.sort(key=lambda g: sum([s.capacity for s in g["values"]]))
        line_servers = filter(None, list(set([s if s != -1 else None for s in line])))
        line_servers.sort(key=lambda s: -servers[s].capacity)
        for i in range(len(line_servers)):
            server = servers[line_servers[i]]
            server.group = groups[i]["group_id"]
            groups[i]["values"].append(server)
    return groups
