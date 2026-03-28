# 📊 Restaurant Tip & Business Analysis Pipeline

An end-to-end Data Science project developed to analyze restaurant transactions, derive business insights, and predict future tipping behavior using Machine Learning.

## 🚀 Key Results
* **High Predictive Power:** The model achieved an **R-squared score of 0.86**, explaining 86% of the variance in tipping.
* **Low Error Margin:** **Mean Absolute Error (MAE) is $0.28**, meaning our predictions are accurate within 28 cents on average.

## 🏗️ Project Structure (OOP)
* **`src/core/`**: Contains the centralized configuration and the `BaseProcessor` parent class.
* **`src/data_prep.py`**: Handles automated data cleaning and validation.
* **`src/features.py`**: Performs Feature Engineering (e.g., Weekend tags, Customer segmentation).
* **`src/visuals.py`**: Generates 4 automated business reports in the `/reports` folder.
* **`src/predict.py`**: Trains a **Random Forest Regressor** and performs **Feature Importance** analysis.

## 📈 Strategic Insights for Management
* **Revenue Peak:** Saturday (**SAT**) was identified as the top-performing day with a turnover of **$1778.40**.
* **Key Drivers:** "Total Bill" is the strongest predictor of tips, suggesting that upselling menu items directly increases staff motivation (tips).
* **Scheduling:** Data suggests prioritizing experienced staff during "Dinner" shifts for optimal service quality.

## 🛠️ Usage
1. Install dependencies: `pip install pandas seaborn scikit-learn matplotlib`
2. Run the pipeline: `python main.py`