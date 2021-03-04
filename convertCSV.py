#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""
import pandas as pd

class Converter:

    def __init__(self, path):
        self._path = path
        self._content = ""
        self._labels = []
        self._dataframe = ""

        self.readLabel()
        self.createVeriable()
        self.matchColumn()
        self.convert()
        self.createDf()

    #   Read Label
    def readLabel(self):
        f = open(self._path, 'r')
        text = f.readlines()
        self._content = text[1:]
        self._labels = text[0].replace('\n', "").split(',')

    def createVeriable(self):
        for l in self._labels:
            globals()[l] = []

    def matchColumn(self):
        for c in self._content:
            text = c.replace('\n', "").split(',')
            for index, l in enumerate(self._labels):
                (globals()[l]).append(text[index])

    #   Categoric data to numbers
    def convert(self):
        globals()["all"] = []
        for l in self._labels:
            encoder = list(set(globals()[l]))

            if len(encoder) == len(globals()[l]):
                encoder = globals()[l]

            globals()[l+'_npy'] = []
            for content in globals()[l]:
                for index, cntnt in enumerate(encoder):
                    if content == cntnt:
                        (globals()[l+'_npy']).append(index)
            (globals()["all"]).append(globals()[l+'_npy'])

    #   Create to Data Frame
    def createDf(self):
        self._dataframe = pd.DataFrame((globals()["all"])).transpose()
        self._dataframe.columns = self._labels

    # You can drop to column easyly
    def dropColumn(self,columnName):
        del self._dataframe[columnName]

    #   Save digit csv
    def recordDf(self):
        path_name = self._path.replace(".csv", "")
        self._dataframe.to_csv(f"{path_name}_digit.csv", index=False)


