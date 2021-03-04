#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

from convertCSV import Converter

if __name__ == '__main__':

    converter = Converter('weather.csv')
    converter.dropColumn("Day")
    converter.recordDf()