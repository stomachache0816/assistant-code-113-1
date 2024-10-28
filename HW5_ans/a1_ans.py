import random

random_chr = ""
random_int = random.randint(0, 25)  # 0 <= random_int <= 25
if random.randint(0, 1) == 0:  # 大寫
    #  0+65 <= random_int <= 25+65
    # => 65 <= random_int <= 90
    random_chr = chr(random_int + 65)
else:  # 小寫
    #  0+97 <= random_int <= 25+97
    # => 97 <= random_int <= 122
    random_chr = chr(random_int + 97)

print("隨機產生的英文字母：", random_chr, sep="")

chance = 3
print("你目前還有", chance, "次機會。", sep="")
guess_chr = str(input("請猜隨機產生的英文字母："))
guess_int = ord(guess_chr)

if guess_chr.isupper():
    guess_int = guess_int - 65  # guess_int = guess_int - ord("A")
else:
    guess_int = guess_int - 97  # guess_int = guess_int - ord("a")

if guess_int == random_int:
    print("答對，遊戲結束。")
else:
    chance -= 1
    print("答錯，你目前還有", chance, "次機會。", sep="")
    guess_chr = str(input("請猜隨機產生的英文字母："))
    guess_int = ord(guess_chr)

    if guess_chr.isupper():
        guess_int = guess_int - 65
    else:
        guess_int = guess_int - 97

    if guess_int == random_int:
        print("答對，遊戲結束。")
    else:
        chance -= 1
        print("答錯，你目前還有", chance, "次機會。", sep="")
        guess_chr = str(input("請猜隨機產生的英文字母："))
        guess_int = ord(guess_chr)
        if guess_chr.isupper():
            guess_int = guess_int - 65
        else:
            guess_int = guess_int - 97

        if guess_int == random_int:
            print("答對，遊戲結束。")
        else:
            print("答錯，三次機會用完了，遊戲結束。")