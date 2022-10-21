#import pandas
import dvc.api as DvcApi


def get_data_url(path:str, version:str):
    repo = "../"
    remote= "dvc-remote"

    data_url= DvcApi.get_url(path= path, repo= repo, rev= version, remote= remote)

    return data_url
