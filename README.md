📊 Restaurant Tip & Business Analysis Pipeline
An end-to-end Data Science project developed to analyze restaurant transactions, derive business insights, and predict future tipping behavior using a Leakage-Free Machine Learning Architecture.

🚀 Key Results
Honest Predictive Power: After resolving data leakage, the model achieved a realistic R-squared score of 0.50, ensuring genuine generalizability.

Stable Error Margin: Mean Absolute Error (MAE) is $0.82, providing a reliable estimate of tipping behavior across various table sizes.

Architectural Integrity: Successfully decoupled analytical features from the training pipeline to ensure 0% target leakage.

🏗️ Project Structure (Advanced OOP)
src/core/: Houses BaseProcessor, the parent class providing a protected analysis environment via get_analysis_df().

src/reports.py: A dedicated BusinessAnalyst module for gap analysis and strategic performance reporting.

src/features.py: Conducts feature engineering (e.g., bill_per_person, time segmentation) without compromising target variables.

src/visuals.py: Generates 4 automated visual reports including revenue trends and tip distributions.

src/predict.py: Implements a regression pipeline that is strictly isolated from target-derived features.

📈 Strategic Insights for Management
Top Performance: Saturday (SAT) remains the peak revenue day with a turnover of $1778.40, suggesting optimal staffing is required.

Analytical Isolation: Business metrics like tip_percentage are calculated only in the reporting layer, preventing the model from "cheating" during training.

Operational Efficiency: Identified gaps in specific time segments (e.g., is_weekend_lunch), pointing to potential areas for targeted marketing campaigns.

🛠️ Usage
Clone the Repo: git clone https://github.com/TKarakan/Tips_Analysis_Project.git

Install Dependencies: pip install pandas seaborn scikit-learn matplotlib

Run the Pipeline: python main.py