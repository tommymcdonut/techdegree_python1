import random
#code adapted from https://www.geeksforgeeks.org/python-infinity/
high_score = float('inf')

def start_game():
    global high_score
    name = input("What is your name, friend?  ").capitalize()
    print("Welcome {}!! To...\n"
          "\n---Tommy Twizz's !MAGNIFICENT! *MAGICAL* number guessing game!!---".format(name)) 
    if high_score == float('inf'):
        print("There is no high score yet!")
    else:
        print("The current high score is {} attempts.".format(high_score))
    while True:
        print("\n{}, starting a new game... ".format(name))
        winning_number = random.randint(1, 10)
        attempts = 0
        while True:
            try:
                guess = int(input("Enter your guess between 1 and 10! "))
                if guess < 1 or guess > 10:
                    print("{}, please pick a number between 1 and 10.".format(name))
                    continue
                attempts += 1
                if guess < winning_number:
                    print("Too low! Try again.")
                elif guess > winning_number:
                    print("Too high! Try again.")
                else:
                    print("Congratulations! You guessed the number {} in {} attempts.".format(winning_number, attempts))
                    if attempts < high_score:
                        high_score = attempts
                        print("New High Score: {} attempts!".format(high_score))
                    break  
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        play_again = input("Do you want to play again, Y/N? ").lower()
        if play_again != 'y':
            print("\nThank you for playing! Your final high score is {} attempts.\nGoodbye!".format(high_score))
            break  
start_game()
