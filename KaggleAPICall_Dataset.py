import os
import pandas
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.model_list_cli()

#api.dataset_download_files(<name of author/name of dataset>', path='./', unzip=True)

api.dataset_download_files('barelydedicated/bank-customer-churn-modeling', path='./', unzip=True)