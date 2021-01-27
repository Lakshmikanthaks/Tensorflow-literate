# Implement equivalent ffmpeg -i test.wav -map_channel 0.0.0 0.wav -map_channel 0.0.1 1.wav -map_channel 0.0.2 2.wav -map_channel 0.0.3 3.wav
# Multi Channel 
# All 4 channels simultanious save 

import csv
import tqdm 
import pathlib
from pathlib import Path
import os

suffix = ".wav"
lists_of_files = []
input_path = pathlib.Path('/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Respeaker_Normalized_Source/103/All/up') 

output_path1 = pathlib.Path('/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Respeaker_Normalized_Source/103/1/up') 
output_path2 = pathlib.Path('/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Respeaker_Normalized_Source/103/2/up') 
output_path3 = pathlib.Path('/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Respeaker_Normalized_Source/103/3/up') 
output_path4 = pathlib.Path('/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Respeaker_Normalized_Source/103/4/up') 

lists_of_files = os.listdir(input_path)
line_count = 0

for name in lists_of_files:
    input_file = os.path.join(input_path, name)
    
    output_file1 = os.path.join(output_path1, name)
    output_file2 = os.path.join(output_path2, name)
    output_file3 = os.path.join(output_path3, name)
    output_file4 = os.path.join(output_path4, name)
    
    input = str(input_file)
    
    output1 = str(output_file1)
    output2 = str(output_file2)
    output3 = str(output_file3)
    output4 = str(output_file4)
    
    command1 = f"ffmpeg -i {input} -map_channel 0.0.0 {output1}"
    command2 = f"ffmpeg -i {input} -map_channel 0.0.0 {output2}"
    command3 = f"ffmpeg -i {input} -map_channel 0.0.0 {output3}"
    command4 = f"ffmpeg -i {input} -map_channel 0.0.0 {output4}"

    os.system(command1)
    os.system(command2)
    os.system(command3)
    os.system(command4)
