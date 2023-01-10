def recursive_sequence(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        seq = recursive_sequence(n-1)
        next_num = seq[-1] - seq[-2]
        seq.append(next_num)
        return seq

sequence = recursive_sequence(5)
print(sequence)