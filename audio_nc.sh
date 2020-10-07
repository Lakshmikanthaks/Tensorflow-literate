#!/bin/bash 
INPUT_STRING = hello 
while [ "$INPUT_STRING" != "c" ] 
do
    echo "Press C to stop the script execution" 
    arecord -Dac108 -f S32_LE -r 48000 -c 4 --max-file-time 20 --use-strftime /home/pi/record/listen-%H-%M-%S-%v.wav | nc -l 3333
    read INPUT_STRING
done 
