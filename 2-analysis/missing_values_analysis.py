from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class MissingValuesAnalysisStrategy(ABC):
    def analyze(self, df: pd.DataFrame):
        self.identify_missing_values(df)
        self.visualize_missing_values(df)

    @abstractmethod
    def identify_missing_values(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def visualize_missing_values(self, df: pd.DataFrame):
        pass

class SimpleMissingValuesAnalysis(MissingValuesAnalysisStrategy):
    def identify_missing_values(self, df: pd.DataFrame):
        print("\nMissing Values Count by Column:")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])
        
    def visualize_missing_values(self, df: pd.DataFrame):
        print("\nVisualizing Missing Values:")
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        plt.title("Missing Values Heatmap")
        plt.show()


if __name__ == "__main__":
    pass