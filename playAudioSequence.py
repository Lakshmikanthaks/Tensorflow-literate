import os
import pygame
import time
from csv import writer 
from pysinewave import SineWave

pygame.init()
pygame.mixer.init()

lists_of_songs = os.listdir("/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/New_Test_DS_1SEC/yes")
time.sleep(20)
tone = '/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/1KHz.wav'
pygame.mixer.music.load(str(tone))
pygame.mixer.music.play()
time.sleep(5)

for song in tqdm(lists_of_songs):
    if song.endswith(".wav"):
        file_path = "/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/New_Test_DS_1SEC/yes/" + song
        # time.sleep(0.5)
        pygame.mixer.music.load(str(file_path))
        pygame.mixer.music.play()
        #print("Playing::::: " + song)
        with open('/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/New_Test_DS_1SEC/yes/played_sequence.csv', 'a') as f:
            writer_object = writer(f)
            writer_object.writerow([str(file_path)]) 
        while pygame.mixer.music.get_busy() == True:
            continue
