import random

start = eval(input("Please input the start(included):"))
end = eval(input("Please input the end(included):"))

key = random.randint(start,end)

guess = eval(input(f"Please guess a number between {start}(included) and {end}(included):"))

while guess != key:
    if guess > key:
        print(f"Wrong! Your guess is too high!")
        end = guess - 1
        guess = eval(input(f"Please guess a number between {start}(included) and {end}(included):"))
    else:
        print(f"Wrong! Your guess is too low!")
        start = guess + 1
        guess = eval(input(f"Please guess a number between {start}(included) and {end}(included):"))


print(f"Congrats! key is {key}!")
print("Game over!")