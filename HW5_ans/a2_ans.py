count = 0

for i in range(1, 100 + 1):
    if i % 2 == 0:
        count += 1
        if count % 10 == 0:
            print(f"{i:>3}", end="\n")
        else:
            print(f"{i:>3}", end=" ")