# in the end this will be the start of the pipeline, let's build subfolders for scripts for each element of the pipeline/
from scipy.io import wavfile
from os import listdir
from os.path import isfile, join, splitext
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
#import pygal
from pygal.style import Style
#from votes import wide as df
#import matplotlib.pyplot
#import matplotlib.dates
import datetime as dt

print("Hello team speech-project!")

mypath = "./raw_samples.nosync/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)


# create lists for data
signals_list = list()
date_list = list()
sampleId_list = list()
sampleLength_list = list()

# loop through the list of raw samples and read the wav file
for wav_filename in onlyfiles:
    # check filename is a wav - so as to avoid trying to read .DStore files for example
    if wav_filename[-3:] == "wav":
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
        print(date_list)
        print(sample_length)
        print(sample_id)

x_values = date_list
y_values = sampleLength_list


dates = ['2015-12-20','2015-09-12']
PM_25 = [80, 55]
dates = [pd.to_datetime(d) for d in dates]

plt.scatter(x_values, y_values, c ='red',marker='x')
plt.title('Sample Lengths Over Time')
plt.ylabel('Sample Length (s)')
plt.ylabel('Sample Publishing Date')
plt.show()
#xy_chart = pygal.XY()
#xy_chart.title = 'Sample lengths over time'
#xy_chart.add('x = 1',  [(1, -5), (1, 5)])
#xy_chart.render()
#xy_chart.render_to_file('chart.svg')


#datetimeline = pygal.DateTimeLine(
#    x_label_rotation=35, truncate_label=-1,
#    x_value_formatter=lambda dt: dt.strftime('%d, %b %Y'))
#datetimeline.add("Series",
#    data_df.date
#)
#datetimeline.render_to_file('chart_date.svg')
#print('done')

#mp3 = read_mp3
