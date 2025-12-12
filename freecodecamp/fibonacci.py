def fibonacci(n:int):
    sequence = [0,1]
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    for i in range(n):
        sequence[0],sequence[1] = sequence[1], sequence[0] + sequence[1]
    # print(sequence[0])
    return sequence[0]
# fibonacci(3)