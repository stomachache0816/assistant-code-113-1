n = eval(input("請輸入購買未稅金額："))

city_tax = n * 0.02
area_tax = n * 0.04
total_tax = city_tax + area_tax
n_with_tax = n + total_tax

print("購買未稅金額：", n, sep="")
print("城市銷售稅：", city_tax, sep="")
print("區銷售稅：", area_tax, sep="")
print("總銷售稅：", total_tax, sep="")
print("總銷售額：", n_with_tax, sep="")