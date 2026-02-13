# Ceci est un jeu de devinette ou l'utilisateur dois deviner un chiffre generer automatiquement par la fonction random. L'utilisateur a droit a autant de tentative que necessaire jusqu'a ce qu'il trouve la bonne valeur et a chaque tentative le programme doit l'indiquer si lA valeur entrer est inferieur ou superieure a la valeur rechercher
import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        if int(guess) < number:
            print("You guessed {}. Is low than number. Try again.".format(guess))
        else:
            print("You guessed {}. SIs greatest than number. Try again.".format(guess))
