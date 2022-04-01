# in the end this will be the start of the pipeline, let's build subfolders for scripts
# for each element of the pipeline.

import plotting
import preprocessing


print("Hello team speech-project!")

mypath = "./raw_samples.nosync/"

# collect samples and some meta-data into a dataframe
data_df = preprocessing.getWavData(mypath)
# plot sample length against time
plotting.feature_time_scatter(data_df.Date,data_df.Length)

