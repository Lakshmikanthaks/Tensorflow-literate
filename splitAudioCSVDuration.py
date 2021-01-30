#Split audio and save as per file name and path in CSV with duration taken from CSV with starting 5 sec 

import csv
import tqdm 
from pathlib import Path
import os

suffix = ".wav"

with open('/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Publication/temp/playsound_yes_smsc.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    start = 5
    for row in csv_reader:
        input_path= Path.home() / "/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Publication/temp/elapsed.wav"
        file_paths= [subp for subp in input_path.rglob('*') if  suffix == subp.suffix]
        input = str(input_path)
        output = str(row[0])
        duration = str(row[1])
        command = f"ffmpeg -ss {start} -i {input} -t {duration} -c copy {output}"
        start = start + float(duration) 
        #print(command)
        #print(str(row[0]))
        os.system(command)
