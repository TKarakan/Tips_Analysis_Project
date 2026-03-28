from .config import DataConfig
import matplotlib.pyplot as plt
import seaborn as sns

class BaseProcessor:

    #initialize with a dataframe or load the default tips dataset.   
    def __init__(self, df= None):
        self.df = df if df is not None else DataConfig.load_raw_data()
        self.TARGET = DataConfig.TARGET
        self.CAT_COLS = DataConfig.CAT_COLS
        self.P_TIME_SEGMENTS = DataConfig.P_TIME_SEGMENTS


    def get_analysis_df(self):
      
        temp_df = self.df.copy()
        temp_df['tip_percentage'] = temp_df['tip'] / temp_df['total_bill']
        return temp_df
 

    #to perform basic data quality and integrity check
    def validate_data(self):
        assert not self.df.empty, "ERROR : Dataset is empty"
        assert self.df.isnull().sum().sum() == 0, "ERROR: Missing values detected"

        print("Data validation is successed: No Nulls or empty sets found")
    
    def get_df(self):
        return self.df.copy()
    
class FeaturesConfigMixin:
    def __init__(self):
        


        self.WORKDAYS = DataConfig.WORKDAYS
        self.WEEKEND = DataConfig.WEEKEND

class VisualConfigMixin:

    def __init__(self):
                
        self.TITLE_SIZE = DataConfig.TITLE_SIZE
        self.LABEL_SIZE = DataConfig.LABEL_SIZE
        self.PALETTE = DataConfig.PALETTE 
                    
        self._setup_visual_defaults()

    def _setup_visual_defaults(self):
        
        sns.set_theme(style=DataConfig.PLOT_STYLE, palette=DataConfig.PALETTE)

        plt.rcParams['figure.figsize'] = DataConfig.FIG_SIZE
        plt.rcParams['axes.titlesize'] = DataConfig.TITLE_SIZE
        plt.rcParams['axes.labelsize'] = DataConfig.LABEL_SIZE
        plt.rcParams['xtick.labelsize'] = DataConfig.LABEL_SIZE - 2 
        plt.rcParams['ytick.labelsize'] = DataConfig.LABEL_SIZE - 2 
class MLConfigMixin:
    def __init__(self):

        self.RF_N_ESTIMATORS = DataConfig.RF_N_ESTIMATORS
        self.RF_RANDOM_STATE = DataConfig.RF_RANDOM_STATE
        self.TEST_SIZE = DataConfig.TEST_SIZE


               