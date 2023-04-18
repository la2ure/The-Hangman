import pygame
import os

pygame.init()
WIDTH, HEIGHT = 800, 500
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman Game')

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

      lives = 7

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


     