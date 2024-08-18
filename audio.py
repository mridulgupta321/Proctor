import pyaudio
import wave
import speech_recognition as sr
import threading

# Define constants for the audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
AUDIO_OUTPUT = "recorded_audio.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# This flag will control when to stop recording
recording = True

def record_audio():
    global recording
    
    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    
    print("Recording...")
    frames = []
    
    while recording:
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("Recording stopped.")
    
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    
    # Save the recorded data as a WAV file
    with wave.open(AUDIO_OUTPUT, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def stop_recording():
    global recording
    recording = False

def convert_audio_to_text():
    recognizer = sr.Recognizer()

    with sr.AudioFile(AUDIO_OUTPUT) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            print("Transcription: ", text)
            # Save the transcription to test.txt
            with open("test.txt", "w") as f:
                f.write(text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == "__main__":
    # Start recording in a separate thread
    recording_thread = threading.Thread(target=record_audio)
    recording_thread.start()
    
    # Simulate a wait before stopping (you can also use input or other signals to stop)
    input("Press Enter to stop recording...")
    stop_recording()
    
    # Wait for the recording to finish
    recording_thread.join()
    
    # Convert the recorded audio to text
    convert_audio_to_text()
