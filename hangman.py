import random


#Begining Code
input_file = open('dictionary.txt', 'r')
input_read = input_file.read()
word_bank = input_read.split()
break1 = 62 * '*'
print(break1)
rules_ask = int(input('Hello and welcome to Hangman! This is a game of guessing\na random word will be selected and you will be given how many\nletters the word contains from the amount of dashes.\nYour job is to guess letter by letter what the word is.\nWhen you wrongly guess a letter you will be given a strike.\nYou have a total of 8 guesses before you lose the game.\nIf you would like to play type 1, if you do not then type 0: '))
#counters
game_counter = 0
win_counter = 0
loss_counter = 0
word_guess = ('')
#while loop to play
while rules_ask == 1:   
    word = random.choice(word_bank)
    turns = 0
    game_counter +=1
    correct = 0
    #while hangman loop
    while turns < 8:
        for character in word:
            #prints the guessed character or a underscore
            if character in word_guess:
                print(character)
                correct += 1
            else:
                print(str(('i'.strip('\n'))))
                incorrect = 0
                incorrect += 1

        if incorrect < 1:
            print('Congrats, you won the game!')
            win_counter += 1
        #keeps guessing the character
        guessing = input('guess one of the character of the random word: ')
        word_guess += guessing
        #increase turn
        if guessing  not in word:
            turns += 1 #when not guessed it increases the turn
        print('You still have', (8 - turns), 'more guesses in total')
        #Lose
        if turns == 8: 
            print('You lost, the word was', word)
            loss_counter += 1
    rules_ask = int(input('Type 1 to play again. Type 2 to end the game: ')) #loop stopper
    

print('\nYou played a total of',game_counter, 'games')
print('You won', win_counter, 'amount of games and lost', loss_counter, 'amount of games')
print('Goodbye')
