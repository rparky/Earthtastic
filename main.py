# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:58:40 2019

@author: rpark
"""

import pandas as pd
import glob

path = 'Data' # use your path
files = glob.glob(path + "/*.csv")

list_of_dfs = [pd.read_csv(file) for file in files]

df = pd.concat(list_of_dfs, axis=0, ignore_index=True)