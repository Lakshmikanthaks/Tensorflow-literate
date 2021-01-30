#Play all files in a folder using simpleaudio module and store played sequence and play duration in CSV format

import os
import pygame
import time
from csv import writer 
from pysinewave import SineWave
import tqdm 
import wave 
import simpleaudio as sa


pygame.init()
pygame.mixer.init()

lists_of_files = [] 
from_path = '/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Publication/Sec_mini_speech_commands/yes'
lists_of_files = os.listdir(from_path)

time.sleep(10)
tone = '/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/1KHz.wav'
pygame.mixer.music.load(str(tone))
pygame.mixer.music.play()
time.sleep(5)
start_time = time.time()

for song in lists_of_files:
    if song.endswith(".wav"):
        file_path = "/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Publication/Sec_mini_speech_commands/yes/" + song
        wave_obj = sa.WaveObject.from_wave_file(file_path)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing
        #print("Playing::::: " + song)
        elapsed_time = (time.time() - start_time)
        print(elapsed_time)
        with open('/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Publication/playsound_yes_smsc.csv', 'a') as f:
            writer_object = writer(f)
            writer_object.writerow([str(file_path), str(elapsed_time)]) 
        start_time = time.time()
        while pygame.mixer.music.get_busy() == True:
            continue
