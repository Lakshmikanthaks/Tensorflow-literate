#Implement add silence at the start & end if audio is less than 1 sec 
#sox <oldfile> <newfile> pad <silence at beginning of file> <silence at end of file> 
#Implement trim audio at start and end if audio is more than 1 sec 
# ffmpeg -i input.wav -af "apad=pad_dur=1" output.m4a
# ffmpeg -ss 132 -i input.mp3 -t 7 output.mp3 


import os
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

train_audio_path = '/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Publication/mini_speech_commands'
sec_train_audio_path = '/home/sriganesh/PhD-SoundAnalysis/Lung_Dataset/Publication/Sec_mini_speech_commands'
labels=os.listdir(train_audio_path)

duration_of_recordings=[]
for label in labels:
    waves = [f for f in os.listdir(train_audio_path + '/'+ label) if f.endswith('.wav')]
    print(label)
    for wav in waves:
        sample_rate, samples = wavfile.read(train_audio_path + '/' + label + '/' + wav)
              
        if float(len(samples)/sample_rate) < 1.0000:
            input_file = os.path.join(train_audio_path + '/'+ label, wav)
            output_file = os.path.join(sec_train_audio_path + '/'+ label, wav)
            print(input_file)
            input = str(input_file)
            output = str(output_file)
            start = 0.0 
            end = 1.0000 - (float(len(samples)/sample_rate))
            print("If", end, len(samples))
            #command = f"sox {input} {output} pad {start} {end}"
            #os.system(command)
            command = f"ffmpeg -i {input} -af apad=whole_len=16000 {output}"
            os.system(command)
        else: 
            input_file = os.path.join(train_audio_path + '/'+ label, wav)
            output_file = os.path.join(sec_train_audio_path + '/'+ label, wav)
            print(input_file)
            input = str(input_file)
            output = str(output_file)
            start = 0.0
            end = 1.0000 - (float(len(samples)/sample_rate))
            print("Else", end, len(samples))
            if end != 0:
                #command = f"sox {input} {output} trim {start} {end}"
                #os.system(command)
                command = f"ffmpeg -ss 0 -i {input} -t 1 {output}"
                os.system(command)
            else:
                command = f"ffmpeg -ss 0 -i {input} -t 1 {output}"
                os.system(command)                
        
        duration_of_recordings.append(float(len(samples)/sample_rate))
        plt.hist(np.array(duration_of_recordings))


