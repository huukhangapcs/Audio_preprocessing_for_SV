from librosa.core import load
from preprocessing.audio import read_mfcc
mfcc = read_mfcc("1.wav")
print(mfcc.shape)