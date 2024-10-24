from abc import ABC, abstractmethod
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


class MultivariateAnalysis(ABC):
    @abstractmethod
    def show(self,df:pd.DataFrame):
        pass

class GenerateHeatMap(MultivariateAnalysis):
    def show(self, df:pd.DataFrame):
        plt.figure(figsize=(10, 8))
        numerical_df = df.select_dtypes(include=[int, float])
        corr_matrix = numerical_df.corr() 
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()


class GeneratePairPlot(MultivariateAnalysis):
    def show(self, df):
        sns.pairplot(df)
        plt.title("Pairplot of Dataset")
        plt.show()


class MultivariateAnalyzer:
    def __init__(self, plot: MultivariateAnalysis):
        self.plot = plot

    def set_plot(self, plot: MultivariateAnalysis):
        self.plot = plot

    def execute_plot(self, df: pd.DataFrame):
        self.plot.show(df)

if __name__ == "__main__":
    data = pd.read_csv(r'D:\Shelton\Machine Learning\Projects\HousePricePrediction\Data\extracted_data\data.csv')
    multi_analyzer = MultivariateAnalyzer(GenerateHeatMap())
    multi_analyzer.execute_plot(data)
    