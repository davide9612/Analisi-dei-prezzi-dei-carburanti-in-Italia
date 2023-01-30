import pandas as pd
import requests
import io
import os

class CsvBuilder:

    def __init__(self, path, filename, urls):
        self.path = path
        self.filename = filename
        self.urls = urls

    def join_csv(self, df_join, df, n_df):
        if n_df < 2:
            return df
        else:
            df_join = pd.merge(df_join, df, how='left')
            return df_join

    def scrape_csv(self):
        try:
            n_df = 0
            df_join = pd.DataFrame
            for url in self.urls:
                n_df += 1
                req = requests.get(url).content
                df = pd.read_csv(io.StringIO(req.decode('utf-8')), sep=';', on_bad_lines='skip', header=1)
                df_join = self.join_csv(df_join, df, n_df)
            self.create_csv(df_join)

        except ConnectionError:
            print('please check your Internet connection')

    def create_csv(self, df_join):
        path = self.path
        filename = self.filename
        if not os.path.exists(path): os.makedirs(path)
        df_join.to_csv(f'{path}/{filename}', index=False, encoding='utf-8')




