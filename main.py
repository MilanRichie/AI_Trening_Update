import pandas as pd

file_path=r"C:\Users\milan\Documents\VTS Apps\AI Team\Python AI ucenje\customer_segmentation.csv"

file_data = pd.read_csv(file_path)

file_data.describe()