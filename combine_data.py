import csv 
import os 
import pandas as pd 
BASE_DIR = './data/'
DATA_01 = BASE_DIR + 'TKha'
DATA_02 = BASE_DIR + '3Tan'
DATA_03 = BASE_DIR + 'Ton'

DATAS_PATH =[DATA_01, DATA_02, DATA_03] 
files_path = list()
for data_path in DATAS_PATH:
    for file_name in os.listdir(data_path):
        if os.path.splitext(file_name)[1].lower() == ".csv":
            files_path.append(os.path.join(data_path, file_name))

data_frames = list()
for file_path in files_path:
    df = pd.read_csv(file_path)
    data_frames.append(df)

combine_df = pd.concat(data_frames, ignore_index=True)
combine_df.to_csv('data.csv', index=False)
