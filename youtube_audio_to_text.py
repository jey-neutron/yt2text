# Transform an audio from a YouTube video to text script with language detection.
# Author: Javed Ali (www.javedali.net)

# Description: This script will ask the user for a YouTube video URL, download the audio from the video, transform it to text, detect the language of the file and save it to a txt file.


# import required modules
import os
import subprocess

import whisper
from langdetect import detect
from pytube import YouTube


# Function to open a file
def startfile(filename):
    '''Open document with default application in Python.'''
    try:
        os.startfile(filename)
    except AttributeError:
        subprocess.call(['open', filename])


# Function to create and open a txt file
def create_and_open_txt(text, filename):
    script_dir = os.path.dirname(__file__)
    rel_path = "Transcribed/"+filename
    abs_file_path = os.path.join(script_dir, rel_path)
    # Create and write the text to a txt file
    with open(abs_file_path, "w") as file:
        file.write(text)
    print('# File success written')
    startfile(abs_file_path)

print("TRANSCRIBING: YOUTUBE URL or AUDIO DOWNLOADED")
# Ask user if audio already downloaded
udahkah = input("Input 0 if from input Youtube URL, input 1 if audio already downloaded: ")

if udahkah=='0':
    # Ask user for the YouTube video URL
    url = input("Enter the YouTube video URL: ")

    # Create a YouTube object from the URL
    yt = YouTube(url)

    # Get the audio stream
    name = yt.title
    keepcharacters = (' ','.','_')
    name = "".join(c for c in name if c.isalnum() or c in keepcharacters).rstrip()
    audio_stream = yt.streams.filter(only_audio=True).first()
    print(f"# Getting youtube title: {name}")

    # Download the audio stream
    output_path = "YoutubeAudios"
    filename = f"audio of {name[:20]}.mp3"
    audio_stream.download(output_path=output_path, filename=filename)

    print(f"# Audio downloaded to {output_path}/{filename}")

    # Load the base model and transcribe the audio
    print('# Load model')
    model = whisper.load_model("base")
    print('# Transcribing')
    result = model.transcribe(f"YoutubeAudios/{filename}", language='id', fp16=False, verbose=True)
    #result={'text':'oioio'}
    print('# Finished, loading result')
    transcribed_text = result["text"]
    print(transcribed_text)
    print()

    # Detect the language
    language = detect(transcribed_text)
    print(f"# Detected language: {language}")

elif udahkah=='1':
    # Ask user to input name of audio
    name = input("Enter filename audio (xxx.mp3, xxx only): ")
    keepcharacters = (' ','.','_')
    name = "".join(c for c in name if c.isalnum() or c in keepcharacters).rstrip()

    # Load the base model and transcribe the audio
    print('# Load model')
    model = whisper.load_model("base")
    print('# Transcribing')
    result = model.transcribe(f"YoutubeAudios/{name.strip()}.mp3", language='id', fp16=False, verbose=True)
    #result={'text':'oioio'}
    print('# Finished, loading result')
    transcribed_text = result["text"]
    print(transcribed_text)
    print()

    # Detect the language
    language = detect(transcribed_text)
    print(f"# Detected language: {language}")

else :
    raise Exception('Not accomodded')
    transcribed_text = "lorem ipsum dolor sit amet"
    name = "lorem"
    language = 'id'

# Create and open a txt file with the text
print('# Finishing transcribing')
try:
    create_and_open_txt(transcribed_text, f"output_{language}_{name[:20]}.txt")
except Exception as e:
    print(f'# Error happen: {str(e)}')
    pass
print()
