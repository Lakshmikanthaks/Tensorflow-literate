#Copy from wave file from start time xx.xx sec from input file for the duration of yy.yy sec to output.wav 
ffmpeg -ss xx.xx -i input.wav -t yy.yy -c copy output.wav 

#Concatinate 2 wave files into one wave file 
sox input1.wav input2.wav output.wav
