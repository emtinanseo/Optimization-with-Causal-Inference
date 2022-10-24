import pandas as pd
import numpy as np



class clean:
    def __init__(self):
        pass

    def out_bounds(self, df: pd.DataFrame, col_lat: str, col_long: str, boundingbox: list, drop=True):
        lat_min, lat_max, long_min, long_max = [float(x) for x in boundingbox]

        indx_lat = (df[col_lat] < lat_min) | (df[col_lat] > lat_max)
        indx_long = (df[col_long] < long_min) | (df[col_long] > long_max)
        indx = indx_lat | indx_long

        print("There are {} coordinate values out of bounds, accounting to {:.2f}% of records.".format(sum(indx), 
        sum(indx)/len(df)))

        if drop:
            df.drop(df[indx].index, inplace=True)

        return df

    def drop_outlier(self, df: pd.DataFrame, column:str, alpha= 0.05):
        indx = df[df[column] > df[column].quantile(1-alpha)].index

        return df.drop(indx, axis=0)