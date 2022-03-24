# in the end this will be the start of the pipeline, let's build subfolders for scripts for each element of the pipeline/
from scipy.io import wavfile
from os import listdir
from os.path import isfile, join

print("Hello team speech-project!")

mypath = "./raw_samples/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

# loop through the list of raw samples and read the wav file
for wav_filename in onlyfiles:
    samplerate, data = wavfile.read("./raw_samples/"+wav_filename)

    print(samplerate)
# data has two channels - plot both




#mp3 = read_mp3
