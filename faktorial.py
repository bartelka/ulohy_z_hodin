def fak(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fak(n-1)

print(fak(4))