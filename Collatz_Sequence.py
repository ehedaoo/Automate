def collatz(ret):
    if ret%2 == 0:
        print(ret//2)
        return (ret//2)
    elif ret%2 == 1:
        print(3*ret+1)
        return (3*ret+1)


num = int(input("Enter number: "))
while num != 1:
    num = collatz(num)