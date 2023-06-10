import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
from os.path import exists
from os import makedirs

from customtkinter import filedialog
from pydub import AudioSegment

def wav2img_dec():
    font = {
    'color':  'white',
    'size': 16,
       }
    
    sound = AudioSegment.from_wav(filedialog.askopenfilename(title="Open a WAV file",
                                                            filetypes=(('WAV files', '*.wav'),)))
    sound = sound.set_channels(1)

    if not exists('spectrogram_files'):
        makedirs('spectrogram_files')

    sound.export('spectrogram_files/mono.wav',
                 format='wav')

    sample_rate, samples = wavfile.read('spectrogram_files/mono.wav')
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

    plt.pcolormesh(times, frequencies, spectrogram)
    plt.ylabel('Frequency [Hz]',
               fontdict=font)
    plt.xlabel('Time [sec]',
               fontdict=font)
    plt.tick_params(axis='both',
                    colors='white')

    plt.savefig('spectrogram_files/spectrogram.png',
                facecolor="#242424")
    
    plt.close()