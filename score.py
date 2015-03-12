def compute_score(servers, nb_groups, nb_lines):
    score = None
    for g in range(nb_groups):
        gc = garantied_capacity(servers, nb_lines, g)
        if score is None or gc < score:
            score = gc
    return score


def garantied_capacity(servers, nb_lines, group_id):
    total_capacity = sum([s.capacity if s.group == group_id else 0 for s in servers])
    by_line = {l: [] for l in range(nb_lines)}
    for s in servers:
        if s.line is None or s.group != group_id:
            continue
        by_line[s.line].append(s)
    value = total_capacity
    for l in range(nb_lines):
        capacity = total_capacity - sum([s.capacity for s in by_line[l]])
        value = min(value, capacity)
    return value
