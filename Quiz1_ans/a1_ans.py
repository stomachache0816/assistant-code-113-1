temp_f = eval(input("請輸入華氏溫度："))
temp_c = (temp_f - 32) / 1.8

print("華氏", temp_f, "度可以轉換成攝氏", round(temp_c), "度", sep="")