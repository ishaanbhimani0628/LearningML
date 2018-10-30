from import_data import fetch_from_url_tgz, os
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
def load_housing_data(housing_path):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing_url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz"
housing_path = "datasets/housing"
fetch_from_url_tgz(housing_url, housing_path, "housing")
#Load the Data
housing_data = load_housing_data(housing_path)
print(housing_data.head())
print(housing_data.info()) #see that there are missing items in total_bedrooms
print(housing_data.describe())

housing_data.hist(bins = 50, figsize = (20,15))
scatter_matrix(housing_data, figsize=(6,6))
#plt.show()
print(housing_data.corr())
