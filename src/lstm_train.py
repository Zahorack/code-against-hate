import tensorflow as tf
import tensorflow.keras as keras
import tensorflow_hub as hub

import pandas as pd
import numpy as np
from sklearn.utils import shuffle

import os


filename = "C:\\Users\\oliver.holly.HQ\\Projects\\Python\\code-against-hate\\dataset\\big_dataset.csv"
df = pd.read_csv(filename, sep=',')


df = df.reset_index(drop=True)
df = shuffle(df, random_state=500)
df = df.reset_index(drop=True)

train = pd.DataFrame(df.iloc[:4000,:])
test = pd.DataFrame(df.iloc[4000:,:])

sentences = train.tweet.values
labels = train.label.values


print(test)

