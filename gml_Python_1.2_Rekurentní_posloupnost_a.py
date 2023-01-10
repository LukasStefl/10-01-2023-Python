def rekurentni_posloupnost(n):
    if n == 0:
        return []
    elif n == 1:
        return [2]
    else:
        L = rekurentni_posloupnost(n-1)
        L.append(3*L[-1])
        return L

print(rekurentni_posloupnost(5))