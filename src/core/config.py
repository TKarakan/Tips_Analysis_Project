import seaborn as sns
import pandas as pd
import os

class DataConfig:
        
    RAW_DATA_PATH = os.path.join('data', 'raw', 'tips.csv')

    P_TIME_SEGMENTS = [
        'is_workday_lunch',
        'is_workday_dinner',
        'is_weekend_lunch',
        'is_weekend_dinner'
    ]

    CAT_COLS = ['sex', 'smoker', 'day', 'time']

    TARGET = 'tip'

    WORKDAYS = ['mon', 'tue', 'wed', 'thur', 'fri']
    WEEKEND= ['sat', 'sun']

    PLOT_STYLE = "whitegrid"
    FIG_SIZE =(10,6)
    TITLE_SIZE = 16
    LABEL_SIZE = 12
    PALETTE = "viridis"

    RF_N_ESTIMATORS = 100
    RF_RANDOM_STATE = 42
    TEST_SIZE = 0.2
    
    def load_raw_data():
        if os.path.exists(DataConfig.RAW_DATA_PATH):
            return pd.read_csv(DataConfig.RAW_DATA_PATH)
        else:
            raise FileNotFoundError(f"File cannot found: {DataConfig.RAW_DATA_PATH}")