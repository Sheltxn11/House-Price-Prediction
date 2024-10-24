import pandas as pd
from abc import ABC, abstractmethod
import zipfile
import os

class DataIngestor(ABC):  
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        pass

class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        if not file_path.endswith('.zip'):
            raise ValueError('The file in the specified path is not a zip file')
        
        extract_dir = os.path.join(os.path.dirname(file_path), 'extracted_data')
        os.makedirs(extract_dir, exist_ok=True)

        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        contents = os.listdir(extract_dir)
        valid_contents = [f for f in contents if f.endswith('.csv')]

        if len(valid_contents) == 0:
            raise ValueError('No CSV files found in the zip file')
        
        if len(valid_contents) > 1:
            raise ValueError('More than one CSV file found in the zip file')

        csv_file_path = os.path.join(extract_dir, valid_contents[0])

        data = pd.read_csv(csv_file_path)
        
        return data

class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        if file_extension == 'zip':
            return ZipDataIngestor()
        else:
            raise ValueError('The file extension is not supported')

if __name__ == "__main__":
    
    # file_path = r'D:\Shelton\Machine Learning\Projects\Patient-Survival\Data\archive.zip'
    # file_ext = file_path.split('.')[-1]
    # ingestor = DataIngestorFactory.get_data_ingestor(file_ext)
    # data = ingestor.ingest(file_path)

    pass