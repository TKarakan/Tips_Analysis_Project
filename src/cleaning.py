from .core.base_analysis import BaseProcessor


class DataCleaner(BaseProcessor):
    #Handles end to end data cleaning including deduplication, standardization and domain specific validation

    def execute(self):

        print(f"\n--- Data Cleaning Pipeline Starts with ({len(self.df)} rows) ---")

        #1. Deduplication

        initial_count = len(self.df)
        self.df = self.df.drop_duplicates()
        
        print(f"Duplicates removed: {initial_count - len(self.df)} rows deleted.")

        #2. Standardization(Lower, Strip & Formatting)
        for col in self.CAT_COLS:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(str).str.lower().str.strip()
        print(f"Text in {self.CAT_COLS} standardized.")

        #3. Missing Data & Domain Logic

        numeric_cols = self.df.select_dtypes(include=['number']).columns
        self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].median())
        self.df= self.df[self.df['total_bill'] > 0]

        #4. Type Optimization for memory

        for col in self.CAT_COLS:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype('category')
        print("Memory optimized: Selected columns are categorized")
        
        return self.df

