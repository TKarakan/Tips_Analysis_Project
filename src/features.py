from .core.base_analysis import FeaturesConfigMixin
from .core.base_analysis import BaseProcessor

class FeatureEngineer(FeaturesConfigMixin, BaseProcessor):

    def __init__(self,df):
        BaseProcessor.__init__(self,df)
        FeaturesConfigMixin.__init__(self)



    def transform(self):
        print("--- Feature Engineering Pipeline Started ---")


        #since we lack granular micro data(like individual item orders),
        #bill_per_person acts as a reliable proxy to estimate the average spending
        #and service demand of a table, independent of its physical size.
            #1. Calculation Metrics           
        self.df['bill_per_person'] = self.df['total_bill'] / self.df['size']
        self.df['tip_percentage'] = self.df['tip'] / self.df['total_bill']

            #2.Segmentation
                #a. workday
        workday_mask = self.df['day'].isin(self.WORKDAYS)
        self.df['is_workday_lunch'] = (workday_mask & (self.df['time'] == 'lunch')).astype(int)
        self.df['is_workday_dinner'] = (workday_mask & (self.df['time'] == 'dinner')).astype(int)
                
                #b. weekend
        weekend_mask = self.df['day'].isin(self.WEEKEND)
        self.df['is_weekend_lunch'] = (weekend_mask & (self.df['time'] == 'lunch')).astype(int)
        self.df['is_weekend_dinner'] = (weekend_mask & (self.df['time'] == 'dinner')).astype(int)

        print("--- Feature Engineering Succesfully Completed ---")
        return self.df
    
    #to identify the segments with zero recorded data



