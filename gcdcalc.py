def nwd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

a = int(input("enter a: "))
b = int(input("enter b: "))
print('greatest commom divisor of a and b is:')
print(nwd(a, b))