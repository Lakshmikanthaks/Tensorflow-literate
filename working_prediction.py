import filecmp
import os 
import pathlib

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tensorflow as tf

from tensorflow.keras.layers.experimental import preprocessing
from tensorflow.keras import layers
from tensorflow.keras import models
from IPython import display

import simpleaudio as sa
from tqdm import tqdm
import pyttsx3
import sys

new_model= tf.keras.models.load_model('/home/sriganesh/google/my_model.h5')
new_data_dir = pathlib.Path('/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/speech_commands_v0.01')
sample_file = new_data_dir/'up/0a7c2a8d_nohash_0.wav'

data_dir = pathlib.Path('/home/sriganesh/google/data/mini_speech_commands')
commands = np.array(tf.io.gfile.listdir(str(data_dir)))
commands = commands[commands != 'README.md']

def decode_audio(audio_binary):
  audio, _ = tf.audio.decode_wav(audio_binary)
  return tf.squeeze(audio, axis=-1)

def get_label(file_path):
  parts = tf.strings.split(file_path, os.path.sep)

  # Note: You'll use indexing here instead of tuple unpacking to enable this 
  # to work in a TensorFlow graph.
  return parts[-2] 

def get_waveform_and_label(file_path):
  label = get_label(file_path)
  audio_binary = tf.io.read_file(file_path)
  waveform = decode_audio(audio_binary)
  return waveform, label

def preprocess_dataset(files):
  files_ds = tf.data.Dataset.from_tensor_slices(files)
  output_ds = files_ds.map(get_waveform_and_label, num_parallel_calls=AUTOTUNE)
  output_ds = output_ds.map(
      get_spectrogram_and_label_id,  num_parallel_calls=AUTOTUNE)
  return output_ds

AUTOTUNE = tf.data.experimental.AUTOTUNE

def get_spectrogram(waveform):
  # Padding for files with less than 16000 samples
  zero_padding = tf.zeros([16000] - tf.shape(waveform), dtype=tf.float32)

  # Concatenate audio with padding so that all audio clips will be of the 
  # same length
  waveform = tf.cast(waveform, tf.float32)
  equal_length = tf.concat([waveform, zero_padding], 0)
  spectrogram = tf.signal.stft(
      equal_length, frame_length=255, frame_step=128)
      
  spectrogram = tf.abs(spectrogram)

  return spectrogram

def get_spectrogram_and_label_id(audio, label):
  spectrogram = get_spectrogram(audio)
  spectrogram = tf.expand_dims(spectrogram, -1)
  label_id = tf.argmax(label == commands)
  return spectrogram, label_id

c = filecmp.dircmp('/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/speech_commands_v0.01/down', '/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/mini_speech_commands/mini_speech_commands/down')

def report_recursive(dcmp):
    for name in dcmp.left_only:
        path = "/home/sriganesh/PhD-SoundAnalysis/Dataset_Working_Jan2021/speech_commands_v0.01/down"
        print(os.path.join(path, name))
        file_working = os.path.join(path, name)
        wave_obj = sa.WaveObject.from_wave_file(str(os.path.join(path, name)))
        play_obj = wave_obj.play()
        play_obj.wait_done()
        sample_ds = preprocess_dataset([str(file_working)])
        original_stdout = sys.stdout
        for spectrogram, label in sample_ds.batch(1):
          prediction = new_model(spectrogram)
          plt.bar(commands, tf.nn.softmax(prediction[0]))
          plt.title(f'Predictions for "{commands[label[0]]}"')
          plt.show()
          print(tf.nn.softmax(prediction[0]))
          with open('2_predictions.txt', 'a+') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print('\n')
            print(str(file_working), ',', str(tf.nn.softmax(prediction[0])),',',label )
            sys.stdout = original_stdout # Reset the standard output to its original value
          print(f.closed)
report_recursive(c)
