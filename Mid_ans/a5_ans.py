rate = eval(input())

if 0 < rate < 1:
    salary = 25000
    new_salary = 50000
    year = 0
    while salary < new_salary:
        salary *= (1 + rate)
        year += 1

    print(year, "年", sep="")
else:
    print("Invalid input")




