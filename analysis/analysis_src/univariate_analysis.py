from abc import ABC, abstractmethod
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


class UnivariateAnalysis(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature: str):
        pass


class NumericalUnivariateAnalysis(UnivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature: str):
        plt.figure(figsize=(12,8))
        sns.histplot(df[feature], kde=True, bins = 30)
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        plt.title(f"Distribution of the feature {feature}")
        plt.show()


class CategoricalUnivariateAnalysis(UnivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature: str):
        plt.figure(figsize=(12,8))
        sns.countplot(x = feature, data = df, palette='muted')
        plt.title(f'Distribution of the feature {feature}') 
        plt.xlabel(feature)
        plt.ylabel('feature')
        plt.xticks(rotation = 45)
        plt.show()

class UnivariateAnalyzer:
    def __init__(self, strategy: UnivariateAnalysis):
        self.strategy = strategy

    def execute_strategy(self, df: pd.DataFrame, feature: str):
        self.strategy.analyze(df,feature)

if __name__ == "__main__":
    pass