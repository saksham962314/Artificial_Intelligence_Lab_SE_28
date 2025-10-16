def alpha_beta_pruning(node_index, depth, alpha, beta, maximizingPlayer, values, target_depth):

    if depth == target_depth:
        return values[node_index]

    if maximizingPlayer:
        value = float('-inf')
        for i in range(2):
            value = max(value, alpha_beta_pruning(node_index * 2 + i, depth + 1, alpha, beta, False, values, target_depth))
            alpha = max(alpha, value)
            if beta <= alpha:
                break 
        return value
    else:
        value = float('inf')
        for i in range(2): 
            value = min(value, alpha_beta_pruning(node_index * 2 + i, depth + 1, alpha, beta, True, values, target_depth))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


values = [3, 5, 6, 9, 1, 2, 0, -1]


target_depth = 3


optimal_value = alpha_beta_pruning(0, 0, float('-inf'), float('inf'), True, values, target_depth)

print("Leaf node values:", values)
print("Optimal value (with Alpha-Beta Pruning):", optimal_value)

