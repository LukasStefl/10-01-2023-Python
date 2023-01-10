def recursive_sequence(n):
    if n == 0:
        return []
    elif n == 1:
        return [2]
    else:
        L = recursive_sequence(n-1)
        L.append(3*L[-1])
        return L

print(recursive_sequence(5))