
# The Secret Word
secret_word = "Ocean"
attempts = 6

print("Welcome to Mordle! Try to guess the 5-letter word.")

while attempts > 0:
    guess = input(f"You have {attempts} attempts left. Enter a 5-letter word: ").lower()

    if len(guess) != 5 or not guess.isalpha():
        print("Invalid input! Please enter a 5-letter word.")
        continue

    # Create feedback with underscores for missing letters
    feedback = ""
    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback += guess[i].upper()  # Correct letter in correct position
        elif guess[i] in secret_word:
            feedback += guess[i]  # Correct letter in wrong position
        else:
            feedback += "_"  # Letter not in the word

    print("Feedback:", feedback)

    if guess == secret_word:
        print("🎉 You guessed the word!")
        break

    attempts -= 1

if attempts == 0:
    print(f"Game over! The word was: {secret_word}")
