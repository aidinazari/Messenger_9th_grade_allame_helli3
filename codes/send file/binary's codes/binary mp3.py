
with open('music.mp3','rb') as music:
    data=music.readlines()
    k=open('binfile1.bin','wb')
    k.writelines(data)
    k.close()

import pygame
pygame.mixer.init()
click=pygame.mixer.music.load('binfile1.bin')
pygame.mixer.music.play(0,1)
