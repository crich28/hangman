import random

def wordbank():
    # pick a random word from a list in arguments
    # display the word as ____ underlines
    # probably ask would you like to play 
    list = ['many','market','marriage','material','matter','may','maybe','me','mean','measure','media','medical','meet','meeting','member','memory','mention']
    r_word = random.choice(list)
    return r_word
def worddisplay(word):
    result=''
    for ch in word:
        ch='_'
        result+=ch
    
    # for i in range(len(wordbank())):
    wrong = 0
    check= []
    while "_" in result and wrong < 6:
        w_guess = False
        guess = input(result+':')
        if len(guess) > 1:
            print("Guess should be one letter")
            continue
        elif guess in check:
            print('You guessed that before \nTry a new letter')
            continue
        else:
            for i in range(len(word)):
                if word[i] == guess:
                    result = result[:i] + word[i] + result[i+1:]
                    w_guess = True
            if not w_guess:
                wrong+=1
        check.append(guess)    
    if wrong == 6:
        print('Thats not correct')
        
        
    if wrong <=5:
        print(result)    
        print('You got it right!')
    playagain()    
        
                
                 
    
def playagain():
    again = input('Would you like to play again? ')
    if again.casefold() == 'yes':
        worddisplay(wordbank())
    print('Next time then')

def hangman():
    play = input("Would you like to play? ")
    if play.casefold() == 'y':
        worddisplay(wordbank())
    else:
        print("Maybe next time")
hangman()
# def game():
#     inp = input("Would you like to play a game? ")
#     if inp == 'yes':
#         return wordbank()

# print(game())


            
# have them guess a letter
# find all instances of the guess rword
#if matches update result
# if no match update wrong guess