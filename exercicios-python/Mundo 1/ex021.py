# Exercício 21 – Tocando um MP3

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('musica1.mp3')
pygame.mixer.music.play()

print=input('Pressione ENTER para parar a música')
