from abc import ABC, abstractmethod
import pandas as pd
import numpy as np

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        pass

class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("Data Types and Non-Null Counts")
        print()
        df.info() 
        print()

class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("Summary Statistics of Numerical Features")
        print(df.describe(include=[np.number])) 
        print()
        print("Summary Statistics of Non-Numerical Features")
        print(df.describe(include=[object]))  
        print()

class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        self.strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        self.strategy.inspect(df)

if __name__ == "__main__":
    pass