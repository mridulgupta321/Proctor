import speech_recognition as sr
import pyaudio
import wave
import os
import threading
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

p = pyaudio.PyAudio()  # Create an interface to PortAudio

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100

def read_audio(stream, filename):
    frames = []  # Initialize array to store frames
    for _ in range(0, int(fs / chunk * 10)):  # Record for 10 seconds
        data = stream.read(chunk)
        frames.append(data)
    
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    # Stop and close the stream
    stream.stop_stream()
    stream.close()

def save_audios(i):
    stream = p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)
    filename = f'record{i}.wav'
    read_audio(stream, filename)

def convert(i):
    if i >= 0:
        sound = f'record{i}.wav'
        r = sr.Recognizer()
        with sr.AudioFile(sound) as source:
            r.adjust_for_ambient_noise(source)
            print("Converting Audio To Text and saving to file..... ") 
            audio = r.listen(source)
        try:
            value = r.recognize_google(audio)
            os.remove(sound)
            result = f"{value}"
            with open("test.txt", "a") as f:
                f.write(result + " ")
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print(f"{e}")
        except KeyboardInterrupt:
            pass

def remove_stop_words(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(data)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    with open('final.txt', 'w') as f:
        for ele in filtered_sentence:
            f.write(ele + ' ')

def compare_texts(paper_path, final_path):
    with open(paper_path, 'r') as file:
        data = file.read()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(data)
    filtered_questions = [w for w in word_tokens if not w in stop_words]
    with open(final_path, 'r') as file:
        data = file.read()
    word_tokens = word_tokenize(data)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    def common_member(a, b):
        a_set = set(a)
        b_set = set(b)
        return a_set.intersection(b_set) if len(a_set.intersection(b_set)) > 0 else []
    comm = common_member(filtered_questions, filtered_sentence)
    print('Number of common elements:', len(comm))
    print(comm)

def process_audio_and_text():
    flag = False
    for i in range(30 // 10):  # Number of total seconds to record / Number of seconds per recording
        t1 = threading.Thread(target=save_audios, args=[i]) 
        x = i - 1
        t2 = threading.Thread(target=convert, args=[x])  # send one earlier than being recorded
        t1.start() 
        t2.start() 
        t1.join() 
        t2.join() 
        if i == 2:
            flag = True
    if flag:
        convert(i)
    p.terminate()
    remove_stop_words("test.txt")
    compare_texts("paper.txt", "final.txt")

# process_audio_and_text()