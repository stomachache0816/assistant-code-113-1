pwd = str(input("請輸入密碼："))

is_pass = True
error_msg = ""

if len(pwd) >= 8:
    has_upper_letter = False
    for letter in pwd:
        if letter.isupper():
            has_upper_letter = True

    if has_upper_letter:
        has_numeric_letter = False
        for letter in pwd:
            if letter.isnumeric():
                has_numeric_letter = True

        if has_numeric_letter:
            print("密碼檢驗通過")
        else:
            print("密碼檢驗不通過：密碼至少含一個數字")
    else:
        print("密碼檢驗不通過：密碼至少含一個大寫英文字母")
else:
    print("密碼檢驗不通過：長度至少需8個字元")

