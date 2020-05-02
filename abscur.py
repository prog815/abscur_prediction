""" Библиотека с методами для доступа к данным проекта <Абсолютный курс> """

src_url = "https://docs.google.com/spreadsheets/d/1_-cdNCIC6NgyRDj0zLJBaohXo-K8qCfxfDLbYq2JLhs/export?format=csv&id=1_-cdNCIC6NgyRDj0zLJBaohXo-K8qCfxfDLbYq2JLhs&gid=422799220"

import pandas as pd
import numpy as np

__abs_data__ = None # сюда загружаем таблицу с данными

def get_data():
    """ Функция отдает (загружает сначала) таблицу с абсолютными курсами """
    global __abs_data__
    if __abs_data__ is None:
        __abs_data__ = pd.read_csv(src_url,decimal=',',parse_dates=True,index_col=0)
    return __abs_data__


def exp_sm(X,alpha=0.9):
    """ Функция для получения экспоненциального сглаживания ряда X с коэффициентом сглаживания alpha
    """
    res = np.array(X)
    for i in range(1,len(res)):
        res[i] = alpha*res[i] + (1-alpha)*res[i-1]
    return res
