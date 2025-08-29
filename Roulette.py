import random as ra

points = 0  # Initialize points

while True:
    user_input = input("Even or Odd (e/o): ").lower()
    print(user_input)
    if user_input not in ("e", "o"):
        print("Input Invalid")
        continue

    computer_choice = ra.randint(1, 10)

    if computer_choice % 2 == 0:
        computer_input = 'e'
    else:
        computer_input = 'o'

    print(f"U choose: {user_input} and Computer Choose: {computer_input}")
    if user_input == computer_input:
        print("U won")
        points += 10  # Add 10 points for win
    else:
        print("U lose")
        points -= 5   # Subtract 5 points for loss

    print(f"Your Points: {points}")  # Show current points

    ask = input("Countinue (y/n): ").lower()
    if ask == 'y':
        continue
    elif ask == 'n':
        print("Thank U")
        break