from src.cleaning import DataCleaner
from src.features import FeatureEngineer
from src.reports import BusinessAnalyst
from src.visuals import Visualizer
from src.predict import TipPredictor


def run_analysis():

    #1. Initialization & Cleaning Phase

    cleaner = DataCleaner()
    df_cleaned = cleaner.execute()

    # 2. Feature Engineering Phase

    engineer = FeatureEngineer(df_cleaned)
    df_featured = engineer.transform()

    # 3. Validation
    engineer.validate_data()

    #4. Reporting stage

    analyst = BusinessAnalyst(df_featured)

    #Executing the reports

    analyst.print_performance_table()
    analyst.print_strategic_insights()

    #5. Visual Reports
    visuals = Visualizer(df_featured)
    visuals.run_all_plots()

    #6. ML Tip Predictor
    predictor = TipPredictor(df_featured)
    predictor.train_and_evaluate()


 
if __name__ == "__main__":
    run_analysis()




