# in the end this will be the start of the pipeline, let's build subfolders for scripts for each element of the pipeline/
from scipy.io import wavfile
from os import listdir
from os.path import isfile, join
from datetime import datetime
#import matplotlib.pyplot
#import matplotlib.dates
import pandas as pd
#import pygal
from pygal.style import Style
#from votes import wide as df

print("Hello team speech-project!")

mypath = "./raw_samples/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)


# create lists for data
signals_list = list()
date_list = list()
sampleId_list = list()

# loop through the list of raw samples and read the wav file
for wav_filename in onlyfiles:
    sample_rate, data = wavfile.read("./raw_samples.nosync/"+wav_filename)
    # get date rom filename and convert to datetime_object
    sample_datetime = datetime.strptime(wav_filename[0:4]+"-"+wav_filename[4:6]+"-"+wav_filename[6:8], '%Y-%m-%d')
    # get sample length in seconds
    sample_length = len(data[:,0]) / sample_rate
    # get sample id from filename
    sample_id = wav_filename[9:-4]
    # add data to lists
    signals_list.append(data)
    date_list.append(sample_datetime)
    sampleId_list.append(sample_id)
    print(sample_datetime)
    print(sample_length)
    print(sample_id)
# data has two channels - plot both

#dates = matplotlib.dates.date2num(sample_datetime)
#matplotlib.pyplot.plot_date(dates, sample_length)

# create dataframe from lists:
data_df = pd.DataFrame(
    {'id': sampleId_list,
     'date': sample_datetime,
     'length': sample_length
     })

print([data_df.date, data_df.length])
#xy_chart = pygal.XY()
#xy_chart.title = 'Sample lengths over time'
#xy_chart.add('x = 1',  [(1, -5), (1, 5)])
#xy_chart.render()
#xy_chart.render_to_file('chart.svg')


datetimeline = pygal.DateTimeLine(
    x_label_rotation=35, truncate_label=-1,
    x_value_formatter=lambda dt: dt.strftime('%d, %b %Y'))
datetimeline.add("Series",
    data_df.date
)
datetimeline.render_to_file('chart_date.svg')
print('done')

#mp3 = read_mp3
