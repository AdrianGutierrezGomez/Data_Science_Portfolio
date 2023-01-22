#Python required packages 
from pathlib import Path
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

influx_metro = pd.read_csv("afluenciastc_simple_12_2002.csv")
print(influx_metro)