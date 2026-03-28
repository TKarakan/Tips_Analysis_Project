from src.core.base_analysis import VisualConfigMixin
from src.core.base_analysis import BaseProcessor

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class Visualizer(BaseProcessor, VisualConfigMixin):


        
    def __init__(self, df):

        BaseProcessor.__init__(self, df)
        VisualConfigMixin.__init__(self)
        
    if not os.path.exists('reports'):
        os.makedirs('reports')

       
    
    print(" Visual reports directory established.")

    def run_all_plots(self):
        print("\n " + "Generating visual reports.".center(65, "-"))

        self._plot_daily_revenue()
        self._plot_tip_relations()
        self._plot_segment_analysis()

        print(f"All charts have been saved to the 'reports/' folder")
        print("-" * 65)

    def _plot_daily_revenue(self):
        plt.figure()

        daily_data = self.df.groupby('day', observed=True)['total_bill'].sum().reset_index()

        sns.barplot( data=daily_data, 
                    x='day', 
                    y='total_bill')
        
        plt.title("Total Revenue by Day of week", fontsize = self.TITLE_SIZE)
        plt.xlabel("Day", fontsize = self.LABEL_SIZE)
        plt.ylabel("Total Bill", fontsize = self.LABEL_SIZE)

        plt.savefig("reports/daily_revenue.png")
        plt.close()

    def _plot_tip_relations(self):
        
        plt.figure()    

        sns.scatterplot(

                data=self.df,
                x='total_bill',
                y='tip',
                hue='time',
                s=100,
                alpha=0.7
            )
        plt.title("Tip vs Total Bill Analysis",fontsize = self.TITLE_SIZE)
        plt.xlabel("Total Bill", fontsize = self.LABEL_SIZE)
        plt.ylabel("Tip", fontsize = self.LABEL_SIZE)

        plt.savefig("reports/tip_relations.png")
        plt.close()

    def _plot_segment_analysis(self):

        plt.figure()

        segment_values = {s: self.df[self.df[s] ==1]['total_bill'].mean() for s in self.P_TIME_SEGMENTS}

        plot_df = pd.DataFrame(list(segment_values.items()), columns=['Segment', 'Avg_Revenue'])

        sns.barplot(data=plot_df, x='Avg_Revenue', y='Segment')
        
        plt.title("Average Revenue by Custom Time Segments", fontsize=self.TITLE_SIZE)
        plt.xlabel("Average Revenue ($)", fontsize=self.LABEL_SIZE)
        plt.ylabel("Segment", fontsize=self.LABEL_SIZE)
        
        plt.tight_layout()
        plt.savefig("reports/segment_performance.png")
        plt.close()
    
    def _plot_tip_distribution(self):
        plt.figure()
        
        temp_df = self.get_analysis_df()
        
        sns.histplot(temp_df['tip_percentage'], kde=True, color='green')
        plt.title("Distribution of Tip Percentages", fontsize=self.TITLE_SIZE)
        plt.xlabel("Tip Percentage (%)")
        plt.savefig("reports/tip_distribution.png")
        plt.close()