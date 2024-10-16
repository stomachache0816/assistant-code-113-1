n = eval(input("請輸入本金："))
rate = eval(input("請輸入利率："))
year = eval(input("請輸入存款年數："))
result = n * (1 + rate) ** year

print("複利為：", round(result, 2), sep="")