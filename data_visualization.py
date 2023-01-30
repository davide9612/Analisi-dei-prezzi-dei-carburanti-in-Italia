import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
import numpy as np


def barplot_macroregioni(df,carburante):

    fig, ax = plt.subplots()
    bar_colors=['tab:red','tab:green','tab:blue']
    df.groupby(["Macroregione"]).prezzo.mean().plot(kind="bar",ax=ax,color=bar_colors)
    plt.xlabel('Macroregione')
    plt.ylabel('Prezzo medio')
    plt.xticks(rotation=0)
    plt.title(f'Prezzo medio {carburante} per macroregione')
    plt.ylim(1.91,1.99)
    plt.show()

#######################################################################################################################

def barplot_bandiera(df,carburante):


    fig, ax = plt.subplots()
    bar_colors=['tab:red','tab:green','tab:blue']
    df.groupby('Bandiera')['prezzo'].agg(['mean']).sort_values(by='mean',
                                        ascending=False).iloc[np.r_[0:4, -5:-1]].plot(kind="bar",ax=ax,color=bar_colors)
    plt.xlabel('Bandiera')
    plt.ylabel('Prezzo medio')
    plt.xticks(rotation=18)
    plt.title(f'Prezzo medio {carburante} per bandiera')
    #plt.ylim(1.91,1.99)
    plt.show()

#######################################################################################################################

def barplot_province(df,carburante):

    fig, ax = plt.subplots()
    bar_colors=['tab:grey']
    df.groupby('Provincia')['prezzo'].agg(['mean']).sort_values(by='mean',
                                        ascending=False).iloc[np.r_[0:5, -6:-1]].plot(kind="bar",ax=ax,color=bar_colors)
    plt.xlabel('Province')
    plt.ylabel('Prezzo medio')
    plt.xticks(rotation=0)
    plt.title(f'Prezzo medio {carburante} per provincia')
    #plt.ylim(1.91,1.99)
    plt.show()

#######################################################################################################################

def time_series(df,carburante):
    fig, ax = plt.subplots()
    bar_colors=['tab:grey']
    df.groupby('dtComu')['prezzo'].agg(['mean']).sort_values(by='dtComu',
                                                             ascending=True).plot(kind="line",ax=ax,color=bar_colors)
    plt.xlabel('Data')
    plt.ylabel('Prezzo medio')
    plt.xticks(rotation=25)
    plt.title(f'Serie storica prezzo medio {carburante}')
    #plt.ylim(1.91,1.99)
    plt.show()

#######################################################################################################################

def multiple_barplot(df):
    df_pivot = pd.pivot_table(df,
                          values="prezzo",
                          index="Provincia",
                          columns="isSelf",
                          aggfunc='mean')

    df_pivot=df_pivot.sort_values(by=1.0)
    df_pivot = df_pivot.iloc[np.r_[0:5, -6:-1]]
    print(df_pivot)
    df_pivot.plot.bar()


