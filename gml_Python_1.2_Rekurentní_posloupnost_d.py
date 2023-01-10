def recursive_sequence(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return 2*recursive_sequence(n-1) + recursive_sequence(n-2) - 3*recursive_sequence(n-2)

sequence = recursive_sequence(5)
print(sequence)
