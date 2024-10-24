from abc import ABC, abstractmethod
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


class BivariateAnalysis(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        pass


class NumericalBivariateAnalysis(BivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        plt.figure(figsize=(12,8))
        sns.scatterplot(x=feature1, y=feature2, data=df)
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.title(f"{feature1} vs {feature2}")
        plt.show()


class CategoricalBivariateAnalysis(BivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        plt.figure(figsize=(12,8))
        sns.boxplot(x=feature1, y=feature2, data=df)
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.xticks(rotation=45)       
        plt.title(f"{feature1} vs {feature2}")
        plt.show()


class BivariateAnalyzer:
    def __init__(self, strategy: BivariateAnalysis):
        self.strategy = strategy

    def set_strategy(self, strategy: BivariateAnalysis):
        self.strategy = strategy

    def execute_strategy(self, df: pd.DataFrame, feature1: str, feature2: str):
        self.strategy.analyze(df, feature1, feature2)


if __name__ == "__main__":
    pass