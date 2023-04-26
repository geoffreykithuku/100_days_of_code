import random
# name = input("What is your name: ")

# print("*************************************")
# print(f"Hello {name}, welcome to hangman game")
# print("*************************************")
# print("*************************************")




word_dict = ["bee", "ball", "egg", "sun", "son", "moon", "goat", "love", "true", "pen", "pig"]

random_word = random.choice(word_dict)
lives = len(random_word)
blank = []
end_of_game = False


for _ in range(len(random_word)):
    blank += "_"
    
while not end_of_game:
    guess = input("Guess a letter ").lower()

    for position in range(len(random_word)):
        letter = random_word[position]
        
        if letter == guess:
            blank[position] = letter
    
    if guess not in random_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            
    print(f"{' '.join(blank)}")

    if "_" not in blank:
        end_of_game = True
        print("You win")