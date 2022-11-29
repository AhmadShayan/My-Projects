import sounddevice
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = int(input("Enter the time duration in seconds: "))  # Duration of recording
print ("Recording...\n")

record_voice = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2)
sounddevice.wait()  # Wait until recording is finished
write("output.wav", fs, record_voice)  # Save as WAV file
print("Recording completed")