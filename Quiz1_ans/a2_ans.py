a = eval(input("請輸入a："))
b = eval(input("請輸入b："))
c = eval(input("請輸入c："))

result = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print("Result：", result, sep="")