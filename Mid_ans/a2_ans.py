score = eval(input())

if 0 <= score <= 100:
    rank = ""
    if 90 <= score <= 100:
        rank = "A"
    elif 80 <= score < 90:
        rank = "B"
    elif 70 <= score < 80:
        rank = "C"
    elif 60 <= score < 70:
        rank = "D"
    else:
        rank = "F"
else:
    print("Invalid input")
