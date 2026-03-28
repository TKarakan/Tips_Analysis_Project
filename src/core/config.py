import seaborn as sns

class DataConfig:
        
    DATASET_NAME = 'tips'

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
        return sns.load_dataset(DataConfig.DATASET_NAME)