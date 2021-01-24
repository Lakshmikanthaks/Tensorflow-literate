import os
import pygame
import time
from csv import writer 
from pysinewave import SineWave

pygame.init()
pygame.mixer.init()

lists_of_files = [] 
from_path = '/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/Normalized/up'
lists_of_files = os.listdir(from_path)

time.sleep(15)
tone = '/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/1KHz.wav'
pygame.mixer.music.load(str(tone))
pygame.mixer.music.play()
time.sleep(5)

for song in lists_of_files:
    if song.endswith(".wav"):
        file_path = "/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/Normalized/up/" + song
        pygame.mixer.music.load(str(file_path))
        pygame.mixer.music.play()
        #print("Playing::::: " + song)
        with open('/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/Normalized/up.csv', 'a') as f:
            writer_object = writer(f)
            writer_object.writerow([str(file_path)]) 
        while pygame.mixer.music.get_busy() == True:
            continue
