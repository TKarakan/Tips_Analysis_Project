# 📊 Restaurant Tip & Business Analysis Pipeline

An end-to-end Data Science project developed to analyze restaurant transactions, derive business insights, and predict tipping behavior using a **Leakage-Free Machine Learning Architecture**.

## 🚀 Key Results (Honest & Validated)
* **Realistic Predictive Power:** After resolving data leakage, the model achieved a **reliable R-squared score of 0.50**.
* **Stable Error Margin:** **Mean Absolute Error (MAE) is $0.82**, providing a trustworthy estimate across various table sizes.
* **Architectural Integrity:** Successfully decoupled analytical features from the training pipeline to ensure **0% target leakage**.

## 🏗️ Project Structure (Advanced OOP)
* `src/core/`: Houses `BaseProcessor`, providing a protected analysis environment via `get_analysis_df()`.
* `src/features.py`: Conducts feature engineering (e.g., time segmentation) without compromising target variables.
* `src/visuals.py`: Generates **4 automated visual reports** including revenue trends and tip distributions.
* `src/predict.py`: Implements a Random Forest pipeline strictly isolated from target-derived features.

## 📈 Strategic Insights for Management
* **Revenue Peak:** Saturday remains the top-performing day ($1778.40).
* **Analytical Isolation:** Metrics like `tip_percentage` are calculated **only in the reporting layer**, preventing the model from "cheating".

## 🛠️ Usage
1.  **Install Dependencies:** `pip install -r requirements.txt`
2.  **Run the Pipeline:** `python main.py`