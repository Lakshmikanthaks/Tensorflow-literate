#Copy from wave file from start time xx.xx sec from input file for the duration of yy.yy sec to output.wav 
ffmpeg -ss xx.xx -i input.wav -t yy.yy -c copy output.wav 

#Concatinate 2 wave files into one wave file 
sox input1.wav input2.wav output.wav

#Split 4 channel audio input to seperate channel using ffmpeg 
ffmpeg -i test.wav -map_channel 0.0.0 0.wav -map_channel 0.0.1 1.wav -map_channel 0.0.2 2.wav -map_channel 0.0.3 3.wav

#recording multi channel (4 Channel) with 16000 Sample rate audio in Raspberry Pi for Respeaker 4 Mic Hardware 
sudo arecord -Dac108 -f S32_LE -r 16000 -c 4 103_all.wav
