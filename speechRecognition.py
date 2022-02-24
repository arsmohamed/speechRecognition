import librosa;
import IPython.display as ipd 
import matplotlib.pyplot as plt
import librosa.display

audio_data = 'test.wav';
x , sr = librosa.load(audio_data, sr=None)
print(type(x), type(sr))#<class 'numpy.ndarray'> <class 'int'>print(x.shape, sr)#(94316,) 22050
ipd.Audio(audio_data)
plt.figure(figsize=(14, 5))
librosa.display.waveshow(x, sr=sr)
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()