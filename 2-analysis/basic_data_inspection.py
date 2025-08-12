from abc import ABC, abstractmethod 
import pandas as pd

# Step 1: Define the Strategy interface
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        pass


# Step 2: Implement Concrete Strategies
class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("\nData Types and Non-null Counts:")
        print(df.info())


class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("\nSummary Statistics (Numerical Features):")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(df.describe(include=["O"]))


# Step 3: Implement the Context
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        self.strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        self.strategy.inspect(df)

# Step 4: Use the Strategy in the Context
if __name__ == "__main__":
    pass