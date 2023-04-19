import pygame
import os

#Setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman Game!')

#Load images
# Boucle sélectionne nos images et les stocke dans la liste imageS
images = []
for i in range(7):
    image = pygame.image.load('images/hangman' + str(i) + '.png')
    images.append(image)

#Game varialbes
hangman_status = 5

#colors
WHITE = (255,255,255)

#Setup game loop
FPS = 60 #frame per second
#Clock object qui va count à 60 frames per second qui va keep track of the time
clock = pygame.time.Clock()
run = True

#Tant que run est true, on va jouer le jeu. Quand on aura perdu/gagné ça passera à false
while run : 
    clock.tick(FPS)

    win.fill(WHITE) #Dessine par dessus le truc précédent/efface
    win.blit(images[hangman_status], (120,100)) #Blit : Dessine une image/surface -- Donne la position XY où on veut blit l'image
    pygame.display.update()

  #chaque event qui se déroule stocké dans pygame.event.get
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Quand tu cliques sur la croix pour fermer
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN: #Get the XY position de la souris sur la fenêtre
            pos = pygame.mouse.get_pos() #FYI origine XY en haut à gauche
            print(pos)

pygame.quit()



    


import random
from word import words
import string

def get_valid_word(words):
    word = random.choice(words) #Choisit au hasard un mot de la liste
    while '-' in word or ' ' in word:
            word = random.choice(words)
    return word.upper()


def hangman():
      word = get_valid_word(words)
      word_letters = set(word) #stocker lettres devinées
      alphabet = set(string.ascii_uppercase)
      used_letters = set() #lettres joueur a proposé

      lives = 6

      while len(word_letters) > 0 and lives > 0:
        #Message affiché pour les lettres déjà utilisées
        #.join transforme une liste en une string. Ce qu'on met entre '' définit l'espacement
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        #Message affiché pour le mot en recherche
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        #Récupérer l'input/la lettre du joueur
        user_letter = input('Guess a letter: ').upper()
        #Si la lettre entrée par le joueur est dans l'alphabet
        #(auquel au fur et à mesure on retire les lettres déjà testées)
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1 #Retire une vie si pas bonne lettre
                print('Letter not in word.')
        
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else :
            print('Invalid character. Please try again.')

      #Quand len(word_letters) == 0 ou lives == 0
      if lives == 0:
        print('You died, sorry. The word was', word)
      else:
        print('You guessed the word', word, '!')

hangman() 
     