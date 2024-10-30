N = eval(input("N："))

if N > 0 and N % 2 == 1:
    result = 1
    for i in range(1, N + 1, 2):
        result *= i
    print("總和：", result, sep="")
else:
    print("Invalid input")
