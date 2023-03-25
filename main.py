import random

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def read_from_file(file_name):
    choose = []
    f = open(file_name, "r")
    lines = f.readlines()
    for word in lines:
        choose.append(word.rstrip())
    f.close()
    return choose


def prepare(word):
    word_letters = []
    guessed = []
    for i in word:
        word_letters.append(i)
        guessed.append("_")
    return word_letters, guessed


def show_list_elements(l, seperateby):
    print(*l, sep=seperateby)


def main():
    cond = True
    while (cond is True):
        choose = read_from_file("texte/data.txt")
        word = random.choice(choose)
        word_letters, guessed = prepare(word)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        nr_of_mistakes = 0
        good_choice = 0
        while nr_of_mistakes < 6 and good_choice < len(word_letters):
            print(hangman[nr_of_mistakes])
            show_list_elements(guessed, " ")
            print("Choose from these letters: ")
            show_list_elements(letters, ", ")
            new_guess = input("Write here your guess: ")
            if new_guess not in letters:
                print("You have already chosen this letter")
                continue
            if new_guess in word:
                for i in range(len(word_letters)):
                    if word_letters[i] == new_guess:
                        guessed[i] = new_guess
                        good_choice = good_choice + 1
            else:
                nr_of_mistakes = nr_of_mistakes + 1
            letters.remove(new_guess)

        if nr_of_mistakes < 6:
            print(word)
            print("Congratulations! You won!!")
        else:
            print(hangman[6])
            print("You lose. Better luck next time. The solution was: " + word)

        cond = False
        play = input('If you want to play again, write "again": ')
        if play == 'again':
            cond = True


main()
