import pandas as pd
import numpy as np
import dvc.api as DvcApi

# ----------------------------------------------------     DVC                 ------------------------------------------
def get_data_url(path:str, version:str):
    repo = "../"
    remote= "dvc-remote"

    data_url= DvcApi.get_url(path= path, repo= repo, rev= version, remote= remote)

    return data_url



# ----------------------------------------------------     Cleaning Functions   ---------------------------------------------------
# Function to calculate missing values by column
def missing_values_table(df: pd.DataFrame) -> pd.DataFrame:
    # Total missing values
    mis_val = df.isnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)

    # dtype of missing values
    mis_val_dtype = df.dtypes

    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent, mis_val_dtype], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values', 2: 'Dtype'})

    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
    '% of Total Values', ascending=False).round(1)

    # Print some summary information
    print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
        "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")

    # Return the dataframe with missing information
    return mis_val_table_ren_columns

def categorical_describe(df: pd.DataFrame, cat_cols: list):
    des_df = df[cat_cols].astype('category').describe()
    values = des_df.values
    values[0] = values[0]/ len(df) *100
    values[-1] = values[-1]/ len(df) * 100
    cat_df = pd.DataFrame(data = values, columns= des_df.columns,
                          index = ['count %', 'unique', 'top', 'freq %'])
    return cat_df

def fix_outlier(df, column):
    df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(),df[column])
    
    return df[column]

def format_float(value):
    return f'{value:,.2f}'