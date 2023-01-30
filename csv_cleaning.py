import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class CsvPreCleaner:

    def __init__(self, df, columns_to_drop):
        self.df = df
        self.columns_to_drop = columns_to_drop

    def pipeline(self):
        df_dupl_dropped = self.drop_duplicates(self.df)
        df_col_dropped = self.drop_columns(df_dupl_dropped)
        df_typed = self.explore_type(df_col_dropped)
        df_na_dropped = self.explore_na(df_typed)
        df_final = self.explore_type(df_na_dropped)
        return df_final

    def drop_duplicates(self,df):
        df_dropped = self.df.drop_duplicates()
        return df_dropped

    def drop_columns(self, df):
        df_dropped2 = df.drop([col for col in self.columns_to_drop], axis=1)
        return df_dropped2

    def explore_na(self, df):
        for column in df.columns:
            print(column, df[f'{column}'].isna().sum())
        df.dropna(inplace=True)
        return df

    def explore_type(self, df):
        for column in df.columns:
            print(column)
            print('numero stringhe', sum([1 for row in df[f'{column}'] if type(row) == str]))
            print('numero float', sum([1 for row in df[f'{column}'] if type(row) == float]))
            print('numero interi', sum([1 for row in df[f'{column}'] if type(row) == int]))
            print('numero booleani', sum([1 for row in df[f'{column}'] if type(row) == bool]))
        return df



def clean_date (df, column_name, type_date):
    if type_date == 'YM':
        df[column_name] = pd.to_datetime(df[column_name]).dt.strftime("%Y-%m")
    elif type_date == 'YMD':
        df[column_name] = pd.to_datetime(df[column_name]).dt.strftime("%Y-%m-%d")
    else:
        df[column_name] = pd.to_datetime(df[column_name]).dt.strftime("%Y")
    return df

