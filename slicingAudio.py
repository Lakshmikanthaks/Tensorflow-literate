# Read output file names from CSV and slice input file for 1 sec duration moving window with start time of 5 sec for the entire csv file numbers 
import csv
import tqdm 
from pathlib import Path
import os

suffix = ".wav"

with open('/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Respeaker_Normalized_Source/103/All/yes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    start = 5
    for row in csv_reader:
        input_path= Path.home() / "/home/sriganesh/Desktop/temp/103_yes.wav"
        file_paths= [subp for subp in input_path.rglob('*') if  suffix == subp.suffix]
        input = str(input_path)
        output = str(row[0])
        command = f"ffmpeg -ss {start} -i {input} -t 1 -c copy {output}"
        start += 1 
        #print(command)
        #print(str(row[0]))
        os.system(command)
