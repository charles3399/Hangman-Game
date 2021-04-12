import random


def hangman():
    word_list = ["Banana","Tree","Car","Smartphone","Cat"]
    random_number = random.randint(0,4)
    word = word_list[random_number]
    wrong_guesses = 0

    stages = ["",
              "________     ",
              "|      |     ",
              "|      0     ",
              "|     /|\    ",
              "|     / \    ",
              "|            "
              ]

    remaining_letters = list(word)
    letter_board = ["_"] * len(word)
    win = False

    print('Welcome to Hangman!\n')

    while wrong_guesses < len(stages) - 1:
        guess = input("\nGuess a letter: ")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess) #If player guessed a letter it will update the first occurence of the guessed letter
            letter_board[character_index] = guess #The blank space will then be replaced by a guessed letter made by the player
            remaining_letters[character_index] = '$' #The guessed letter will be replaced by a dollar sign so that it will no longer be in the remaining letter list
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0:wrong_guesses + 1]))
        if '_' not in letter_board:
            print('\nYou win! The word was: ')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\nYou lose! The word was: {}'.format(word))

hangman()
            
