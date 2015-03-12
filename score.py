def compute_score(servers, nb_groups, nb_lines):
    score = None
    for g in range(nb_groups):
        gc = garantied_capacity(servers, nb_lines, g)
        if score is None or gc < score:
            score = gc
    return score


def garantied_capacity(servers, nb_lines, group_id):
    total_capacity = sum([s.capacity if s.group == group_id else 0 for s in servers])
    value = total_capacity
    for l in range(nb_lines):
        capacity = sum([s.capacity if s.group == group_id and s.line != l else 0 for s in servers])
        value = min(value, total_capacity - capacity)
    return value
