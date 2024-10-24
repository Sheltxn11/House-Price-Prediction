from abc import ABC, abstractmethod
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

class MissingValuesAnalysisTemplate(ABC):
    def analyze(self,df: pd.DataFrame):
        self.identify_missing_values(df)
        self.visualize_missing_values(df)

    @abstractmethod
    def identify_missing_values(self,df: pd.DataFrame):
        pass

    def visualize_missing_values(self,df: pd.DataFrame):
        pass


class MissingValueAnalysis(MissingValuesAnalysisTemplate):
    def identify_missing_values(self, df: pd.DataFrame):
        print("Missing Values by Columns")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values>0])

    def visualize_missing_values(self, df: pd.DataFrame):
        plt.figure(figsize = (12,8))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        plt.title("Missing Value Visual Analysis")
        plt.show()


if __name__ == "__main__":
    pass

