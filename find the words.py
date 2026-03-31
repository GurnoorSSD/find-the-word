import random

words = ["python", "apple", "tiger", "ocean", "rocket", "shadow"]
word = random.choice(words)

guesses_left = 6
guessed_letters = []
display = ["_"] * len(word)

# Reveal 2 random letters
for pos in random.sample(range(len(word)), 2):
    display[pos] = word[pos]
    guessed_letters.append(word[pos])

print("🎮 Word Hide & Seek Game!")
print("2 letters are already revealed. You have 6 guesses.\n")

while guesses_left > 0 and "_" in display:
    print("Word:", " ".join(display))
    print("Guessed:", ", ".join(sorted(set(guessed_letters))))
    print("Guesses left:", guesses_left)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter a valid single letter!\n")
        continue

    if guess in guessed_letters:
        print("⚠️ Already guessed!\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!\n")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("❌ Wrong!\n")
        guesses_left -= 1

if "_" not in display:
    print("🎉 You found the word:", word)
else:
    print("💀 Out of guesses! The word was:", word)
