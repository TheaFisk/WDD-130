
# Variable is determined

word = "ocean"
guess = " "
attempts = 0
#game begins
print("  ")
print("Welcome to the Mordle (TM) Guessing Game!")
print("The word has 5 letters!")

# loop to test the word
while guess != word:
    attempts = attempts + 1
    print("   ")
    print("Your hint is: _____")
    guess = input("What is your Guess? ")
    if len(guess) != 5:
        print("  ")
        print("That's not a 5 letter word!")
    if guess != word:
        print("Incorrect! Wrong word.")
    
    
# Found the word!
print("   ")
print("Congratulations! You found the word!")
print(f"It took you", attempts, "attempts.")
