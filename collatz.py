def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

user_number = int(input("Enter a number: "))

print(user_number)

while user_number != 1:
    user_number = collatz(user_number)
    print(user_number)