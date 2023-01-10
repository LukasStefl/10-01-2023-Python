def recursive_sequence(a1, a2, n):
    # Initial values
    a_n = [a2, a1]
    # Recursive calculation
    for i in range(2, n):
        a_n.append(a_n[i-1] - a1 + a_n[i-2])
    return a_n

print(recursive_sequence(0, 1, 5))