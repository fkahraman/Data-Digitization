#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

import pandas as pd
from convertCSV import Converter

if __name__ == '__main__':

    """
        Usage Type 1
    """
    converter = Converter(path='weather.csv')
    converter.dropColumn("Day") # Optional
    converter.recordDf()

    """
        Usage Type 2
    """
    df = pd.read_csv('weather.csv')
    converter = Converter(df=df)
    converter.recordDf()