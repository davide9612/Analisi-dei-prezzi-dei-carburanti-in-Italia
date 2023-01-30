from csv_building import CsvBuilder
from csv_cleaning import CsvPreCleaner,clean_date
from data_visualization import barplot_macroregioni,barplot_province,barplot_bandiera,multiple_barplot,time_series
import pandas as pd

if __name__ == "__main__":

#BUILDING

    urls = ["https://www.mise.gov.it/images/exportCSV/anagrafica_impianti_attivi.csv",
            "https://www.mise.gov.it/images/exportCSV/prezzo_alle_8.csv"]

    df_carburantiITA = CsvBuilder(path=f'./carburante', filename='carburante_italiano.csv', urls=urls).scrape_csv()

    # urls=[]
    # df_carburantiENG = CsvBuilder(path=f'./carburante', filename='carburante_inglese.csv', urls=urls).scrape_csv()

#######################################################################################################################

#CLEANING

#drop useful columns
df=pd.read_csv('carburante/carburante_italiano.csv')
columns_to_drop=['idImpianto', 'Gestore', 'Nome Impianto','Indirizzo','Comune','Longitudine']

#call class CsvPreCleaner
df_cleaned = CsvPreCleaner(df,columns_to_drop).pipeline()

#column Latitudine
df_cleaned=df_cleaned.astype({'Latitudine':str})
df_cleaned["Latitudine"] = df_cleaned['Latitudine'].str.replace('[^\w\s]','')
df_cleaned['Latitudine'] = df_cleaned['Latitudine'].str[:2]
df_cleaned=df_cleaned.astype({'Latitudine':float})

#column dtComu - call function clean_date
df_cleaned_date= clean_date(df_cleaned,'dtComu','YMD')
df_cleaned_date.to_csv('./carburante/carburante_italiano_pulito.csv')

########################################################################################################################

#VISUALIZATION


df=pd.read_csv('carburante/carburante_italiano_pulito.csv')

df['Macroregione'] = pd.cut(df['Latitudine'], bins=[36,41,43,48], labels=['Sud', 'Centro', 'Nord'])
dfBenz=df[(df['descCarburante']=='Benzina')]
dfDies=df[(df['descCarburante']=='Gasolio')]

barplot_macroregioni(dfBenz,'benzina')
barplot_macroregioni(dfDies,'diesel')

barplot_province(df,'carburante')
barplot_province(dfBenz,'benzina')
barplot_province(dfDies,'diesel')

barplot_bandiera(dfBenz,'benzina')
barplot_bandiera(dfDies,'diesel')


time_series(dfBenz,'benzina')
time_series(dfDies,'diesel')

multiple_barplot(dfBenz)
multiple_barplot(dfDies)