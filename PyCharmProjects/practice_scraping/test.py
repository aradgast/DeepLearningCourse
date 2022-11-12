import math

def calculate_N():
    k=0
    sum_0 = (25/12)*((0.52) ** (k+1) / math.factorial(k+1))

    while abs(sum_0)>(10**-7):
        k += 1
        sum_0 = (25 / 12) * ((0.52) ** (k + 1) / math.factorial(k + 1))
        print(f'for k={k} we get {sum_0}')
    return k, (25/12)*((0.52) ** (k+1) / math.factorial(k+1))



print(calculate_N())





