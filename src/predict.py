from src.core.base_analysis import MLConfigMixin
from src.core.base_analysis import BaseProcessor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class TipPredictor(BaseProcessor, MLConfigMixin):
    def __init__(self,df):

        BaseProcessor.__init__(self, df)
        MLConfigMixin.__init__(self)

        self.model = RandomForestRegressor(n_estimators=self.RF_N_ESTIMATORS, 
                                           random_state=self.RF_RANDOM_STATE
        )

    
    def _prepare_ml_data(self):

        ml_df = pd.get_dummies(self.df, columns=self.CAT_COLS, drop_first=True)

        y = ml_df[self.TARGET]
        X = ml_df.drop(columns=[self.TARGET])
        
        return X,y
    
    def train_and_evaluate(self):

        X, y = self._prepare_ml_data()
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=self.TEST_SIZE, random_state=self.RF_RANDOM_STATE)
        
        print("\n" + " ML MODEL TRAINING ".center(65, "="))
        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        mae = mean_absolute_error(y_test,predictions)
        r2 = r2_score(y_test,predictions)

        print(f" Model training Complete.")
        print(f" Mean absolute Error (MAE): ${mae:.2f}")
        print(f" R- squared score: {r2:.2f}")

        self._plot_feature_importance(X.columns)
        print(f"Feature Importance chart saved to 'reports/'.")

        return X,y

    def _plot_feature_importance(self, feature_names):

        importances = self.model.feature_importances_
        fi_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
        fi_df = fi_df.sort_values(by='Importance', ascending=False).head(10)

        plt.figure()
        sns.barplot(data=fi_df, x= 'Importance', y='Feature')
        plt.title("Key Drivers of Tipping Behavior", fontsize=self.TEST_SIZE)
        plt.tight_layout()
        plt.savefig("reports/feature_importance.png")
        plt.close()




