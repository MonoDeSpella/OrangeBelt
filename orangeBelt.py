#here is a gallows game!
import random

word_list = ['math', 'literature', 'history', 'programming', 'csharp', 'onelove', 'python']

#function that gets random word from list above (:D)
def get_word():
    word = random.choice(word_list)
    return word.upper()
  
# getting current level
def display_hangman(tries):
    stages = [  # final stage: head, torso, both hands, both legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, torso, both hands, one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, torso, both hands
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, torso, one hand
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head and torso
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # first stage
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

#main function
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Guess the word')
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        guess = input('Write some letters or the whole word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You have already guessed this one', guess)
            elif guess not in word:
                print('Letter', guess, 'is not in the word')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Gj! Letter', guess, 'is in the word')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You have already guessed this word', guess)
            elif guess != word:
                print('Word', guess, 'incorrect')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Write some letters or the whole woed')
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('Gratz! You-ve guessed the right word')
    else:
        print('Unlucky! That was ' + word + '. Better luck next time')
