""" Библиотека с методами для доступа к данным проекта <Абсолютный курс> """

src_url = "https://docs.google.com/spreadsheets/d/1_-cdNCIC6NgyRDj0zLJBaohXo-K8qCfxfDLbYq2JLhs/export?format=csv&id=1_-cdNCIC6NgyRDj0zLJBaohXo-K8qCfxfDLbYq2JLhs&gid=422799220"

import pandas as pd

__abs_data__ = None

def get_data():
    global __abs_data__
    if __abs_data__ is None:
        __abs_data__ = pd.read_csv(src_url,decimal=',',parse_dates=True,index_col=0)
    return __abs_data__
