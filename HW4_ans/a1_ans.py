print("設定帳號密碼")
account_set = str(input("請輸入帳號:"))
pwd_set = str(input("請輸入密碼:"))

print("驗證帳號密碼")
account_input = str(input("請輸入帳號:"))
pwd_input = str(input("請輸入密碼:"))

if account_set == account_input and pwd_set == pwd_input:
    print("帳號密碼正確")
else:
    print("帳號或密碼錯誤")
