import tensorflow as tf
import tensorflow.keras as keras
import tensorflow_hub as hub

import pandas as pd
import numpy as np
from sklearn.utils import shuffle

import os
from tensorflow.keras.regularizers import l2


def create_model(input_length):
    p_W, p_U, p_dense, p_emb = 0.75, 0.75, 0.5, 0.5
    weight_decay, batch_size, maxlen = 1e-4, 10, 500
    model = keras.models.Sequential()
    model.add(keras.layers.LSTM(1024, input_shape=(1, input_length),
                   kernel_regularizer=l2(weight_decay),
                   recurrent_regularizer=l2(weight_decay),
                   dropout=p_W,
                   recurrent_dropout=p_U))
    model.add(keras.layers.Dropout(p_dense))
    model.add(keras.layers.Dense(1024,
                    kernel_regularizer=l2(weight_decay),
                    activation='relu'
                    ))
    model.add(keras.layers.Dropout(p_dense))
    model.add(keras.layers.Dense(1, kernel_regularizer=l2(weight_decay),
                    activation='sigmoid'
                    ))
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    return model


filename = "C:\\Users\\oliver.holly.HQ\\Projects\\Python\\code-against-hate\\dataset\\big_dataset.csv"
df = pd.read_csv(filename, sep=',')


# df = df.reset_index(drop=True)
df = shuffle(df, random_state=500)
df = df.reset_index(drop=True)

train = pd.DataFrame(df.iloc[:4000,:])
test = pd.DataFrame(df.iloc[4000:,:])

x_train= train.iloc[:,4:132].values
x_test= test.iloc[:,4:132].values

y_train= train.iloc[:,1:2].values
y_test= test.iloc[:,1:2].values


# x_train= train['normalized_text'].values
# x_test= test['normalized_text'].values
#
# y_train= train['label'].values
# y_test= test['label'].values

print(train)

# y_train= train.iloc[:,1:2].values
# y_test= test.iloc[:,1:2].values
#
# model = create_model(x_test.shape[1])
# loss, acc = model.evaluate(x_test,  y_test, verbose=2)
# print("Untrained model, accuracy: {:5.2f}%".format(100*acc))
