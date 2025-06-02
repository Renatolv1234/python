'''Faça um programa que abra e reproduza o audio de um arquivo mp3'''
import pygame

'''Depois de intalarmos a biblioteca preciamos iniciala com : '''

pygame.init()
'''Agora vamos carregar o audio: '''

pygame.mixer.music.load('ex021.mp3')

'''Após carregar o audio vamos tocar ele'''

pygame.mixer.music.play()

'''Agora para encerrar precisamos que ele espere a musica acabar para parar'''

pygame.event.wait()
