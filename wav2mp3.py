import os
import glob
from pydub import AudioSegment

extension = '*.wav'
for audio in glob.glob(extension):
	mp3_filename = os.path.splitext(os.path.basename(audio))[0] + '.mp3'
	AudioSegment.from_file(audio).export(mp3_filename, format='mp3')
