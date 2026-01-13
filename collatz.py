def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

user_number = int(input("Enter a number: "))

while user_number > 1:
    print(f'current user number: {user_number}')
    user_number = collatz(user_number)