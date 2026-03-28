from src.core.base_analysis import FeaturesConfigMixin
from src.core.base_analysis import BaseProcessor

class BusinessAnalyst(BaseProcessor,FeaturesConfigMixin):

    #Class dedicated to identifying gaps, generating insigths, and reporting.

    def __init__(self, df):
        
        BaseProcessor.__init__(self, df)
        FeaturesConfigMixin.__init__(self)
    
    #to identfy the segments with zero recorded data.
    def perform_gap_analysis(self):

        active = [s for s in self.P_TIME_SEGMENTS if self.df[s].sum() > 0]
        gaps = [s for s in self.P_TIME_SEGMENTS if self.df[s].sum() == 0]

        return active,gaps
    
    def print_performance_table(self):
        active, gaps = self.perform_gap_analysis()
        
        print("\n" + "TIPS DATASET Performance Report".center(65, "="))
        print(f"{'Segment':<25} | {'Tables':<6} | {'Avg Tip %':<10} | {'Revenue':>12}")
            
            #Iterating through segments defined
            
        for segment in active:
            data_subset = self.df[self.df[segment] == 1]
            count = len(data_subset)
            avg_tip = data_subset['tip_percentage'].mean() * 100
            rev = data_subset['total_bill'].sum()
            print(f"{segment:<25} | {count:<6} | %{avg_tip:9.2f} | {rev:>12.2f}" )

           
            
        #Reporting for gaps
        if gaps:
            print("\n" + " Data Gap Analysis".center(65, "-"))
            for g in gaps:
                print(f"{g:25} : No transactions found." )
            print("-" * 65)
    
    #to calculate and display records and actionable business recommendations
    def print_strategic_insights(self):
        best_tip_row = self.df.loc[self.df['tip_percentage'].idxmax()]
        max_bill_row = self.df.loc[self.df['total_bill'].idxmax()]
        
    #results
    
        print(f"Highest Tip: %{best_tip_row['tip_percentage']*100:.1f}")
        print(f"Gün: {best_tip_row['day']}, Vakit:{best_tip_row['time']}, Hesap: {best_tip_row['total_bill']}")

        print(f"Highest invoice: {max_bill_row['total_bill']} ")
        print(f"Gün:{max_bill_row['day']},Vakit:{best_tip_row['time']}, Tip:{max_bill_row['tip']}")

        print("=" * 50)

    # Daily Revenue Analysis to check efficiency

        daily_revenue = self.df.groupby('day', observed=True)['total_bill'].sum().sort_values()

        worst_day, best_day = daily_revenue.index[0], daily_revenue.index[-1]
        worst_rev, best_rev = daily_revenue.iloc[0], daily_revenue.iloc[-1]


        print(f"Lowest Revenue day:{worst_day.upper()} (Total: ${worst_rev:.2f})")
        print(f"Highest Revenue day: {best_day.upper()} (Toplam ciro: ${best_rev:.2f})")

        # Strategic Recommendation based on Daily Revenue Analysis:
        # 1. Staffing Optimization: Schedule employee leaves during low revenue days 
        #    and increase workforce during peak periods to ensure service quality.
        # 2. Marketing Strategy: Boost customer traffic on slower days through 
        #    targeted campaigns (e.g., set price menus, complimentary beverages).
        


      
 