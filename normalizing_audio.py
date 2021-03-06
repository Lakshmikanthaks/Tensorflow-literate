import soundfile as sf
import pyloudnorm as pyln
import os
import pygame
import time
import tqdm
import simpleaudio as sa
import pyttsx3
from pydub import AudioSegment

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

from_path = '/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/New_Test_DS_1SEC/yes'
to_path = '/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/New_Test_DS_1SEC/yes_normalized'

lists_of_files = os.listdir(from_path)
for file in lists_of_files:
    file_working = os.path.join(from_path, file)
    normalized_file = os.path.join(to_path, file)
    data, rate = sf.read(str(file_working)) # load audio (with shape (samples, channels))
    meter = pyln.Meter(rate) # create BS.1770 meter
    loudness = meter.integrated_loudness(data) # measure loudness
    sound = AudioSegment.from_file(file_working, "wav")
    normalized_sound = match_target_amplitude(sound, -20.0)
    normalized_sound.export(normalized_file, format="wav")
    normalized_data, normalized_rate = sf.read(str(normalized_file)) # load audio (with shape (samples, channels))
    normalized_loudness = meter.integrated_loudness(normalized_data) # measure loudness
    print(loudness, normalized_loudness)
