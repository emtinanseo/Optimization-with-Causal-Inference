import pandas
import seaborn as sns
import matplotlib.pyplot as plt



# ----------------------------------------------------     Plotting Functions   ---------------------------------------------------
def plot_hist(df:pd.DataFrame, column:str, color:str, file_name= None)->None:
    # plt.figure(figsize=(15, 10))
    # fig, ax = plt.subplots(1, figsize=(10, 5))
    sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    if file_name:
        plt.savefig(file_name, bbox_inches = 'tight')
    plt.show()

def plot_count(df:pd.DataFrame, column:str, hue= None,order=None, file_name= None) -> None:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=column, order= order, hue= hue)
    if hue:
        title = f'Distribution of {column} compared for different classes of {hue}'
    else:
        title = f'Distribution of {column}'
        
    plt.title(title, size=20, fontweight='bold')
    if file_name:
        plt.savefig(file_name, bbox_inches = 'tight')
    plt.show()
    
    
def plot_pie(df:pd.DataFrame, column:str, labels= None, file_name= None)->None:
    val = df[column].value_counts()
    lab = df[column].value_counts().index
    if labels:
        lab = [labels[x] for x in lab]
    fig, ax = plt.subplots(1, figsize=(7,7))
    ax.pie(val, labels= lab, autopct='%1.1f%%', textprops= {'fontsize': 14})
    plt.title(f'Pie Chart of {column}', size=20, fontweight='bold')
    if file_name:
        plt.savefig(file_name, bbox_inches = 'tight')
    plt.show()

    
def plot_count_compare(ax, df:pd.DataFrame, column:str, hue= None, order=None, group='full data'):
    sns.countplot(ax= ax, data=df, x=column, order= order, hue= hue)
    if hue:
        ax.set_title(f'{group}: Distribution of {column} for different {hue}s')
    else:
        ax.set_title(f'{group}: Distribution of {column}')
    
    
def plot_pie_compare(ax, df:pd.DataFrame, column:str, group='full data', labels=None)->None:
    val = df[column].value_counts()
    lab = df[column].value_counts().index
    if labels:
        lab = [labels[x] for x in lab]
    ax.pie(val, labels= lab, autopct='%1.1f%%', textprops= {'fontsize': 14})
    ax.set_title(f'{group}: Pie Chart of {column}', size=20, fontweight='bold')
        
    
pd.options.display.float_format = format_float
