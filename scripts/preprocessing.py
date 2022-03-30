from scipy.io import wavfile
from os import listdir
from os.path import isfile, join, splitext
from datetime import datetime
import pandas as pd


def getWavData(mypath):

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    # create lists for data
    signals_list = list()
    date_list = list()
    sampleId_list = list()
    sampleLength_list = list()
    sample_no = int(1)
    # loop through the list of raw samples and read the wav file
    for wav_filename in onlyfiles:
        # check filename is a wav - so as to avoid trying to read .DStore files for example
        if wav_filename[-3:] == "wav":
            print("Reading sample number " + str(sample_no))
            # read wav
            sample_rate, data = wavfile.read("./raw_samples.nosync/"+wav_filename)
            # get date rom filename and convert to datetime_object
            sample_datetime = datetime.strptime(wav_filename[0:4]+"-"+wav_filename[4:6]+"-"+wav_filename[6:8], '%Y-%m-%d')
            # get sample length in seconds
            sample_length = len(data[:,0]) / sample_rate
            # get sample id from filename
            sample_id = wav_filename[9:-4]
            # add data to lists
            signals_list.append(data)
            date_list.append(sample_datetime.date())
            sampleId_list.append(sample_id)
            sampleLength_list.append(sample_length)
            # increase counter
            sample_no = sample_no + 1

    # Create dataframe from lists
    data_df = pd.DataFrame()
    data_df['Id'] = sampleId_list
    data_df['Samples']  = signals_list
    data_df['Date'] = date_list
    data_df['Length'] = sampleLength_list

    return data_df
