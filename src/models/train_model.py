import string
import nltk

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

import keras
from keras.utils import np_utils
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model

column_names = ["Emotions", "Sentences"]
df = pd.read_csv(
    "drive/My Drive/Training_AI_Engineers/isear_dataset.csv", names=column_names
)

df.dropna(inplace=True)
nltk.download("stopwords")


def clean_text(text):
    text = text.translate(string.punctuation)
    text = text.lower().split()

    from nltk.corpus import stopwords

    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]
    text = " ".join(text)
    return text


df["Sentences"] = df["Sentences"].map(lambda x: clean_text(x))

X, y = df["Sentences"], df["Emotions"]


encoder = LabelEncoder()
encoder.fit(y)
encoded_y = encoder.transform(y)
onehot_y = np_utils.to_categorical(encoded_y)


vocab = set()
a = [vocab.add(el) for s in X.values for el in s.split(" ")]


vocabulary_size = 80896  # Select an Appropriate Vobabulary Size
padded_length = 150  # Select an Appropriate padded Length for text
tokenizer = Tokenizer(num_words=vocabulary_size)
tokenizer.fit_on_texts(X)


def preprocessing(X):
    sequences = tokenizer.texts_to_sequences(X)
    data = pad_sequences(sequences, maxlen=padded_length)
    return data


data = preprocessing(X)

X_train, X_test, y_train, y_test = train_test_split(
    data, onehot_y, test_size=0.1, random_state=101
)


learning_rate = 1e-2
numEpoch = 20
embedding_size = 200
lstm_size = 64

import tensorflow as tf
import keras
from keras import optimizers, regularizers
from keras.layers import Dense, Flatten, LSTM, Dropout, Activation
from keras.layers.embeddings import Embedding


def create_model(embedding_size=100, lstm_size=32, layer1_size=32, dropoutrate=0.3):
    model = keras.models.Sequential()
    model.add(
        Embedding(
            vocabulary_size,
            embedding_size,
            input_length=padded_length,
            embeddings_regularizer=regularizers.l1(0.001),
        )
    )
    model.add(LSTM(lstm_size, dropout=dropoutrate, recurrent_dropout=dropoutrate))
    model.add(Dense(layer1_size, activation="relu"))
    model.add(Dropout(dropoutrate, seed=seed))
    model.add(Dense(7, activation="softmax"))
    optim = optimizers.Adam(
        lr=learning_rate,
        beta_1=0.9,
        beta_2=0.999,
        epsilon=1e-08,
        decay=learning_rate / numEpoch,
    )
    model.compile(
        loss="categorical_crossentropy", optimizer=optim, metrics=["accuracy"]
    )
    return model


model = create_model(
    embedding_size=embedding_size, lstm_size=lstm_size, layer1_size=32, dropoutrate=0.3
)

history = model.fit(
    X_train, y_train, batch_size=128, validation_split=0.2, epochs=numEpoch
)

model.save("../models/isearModel.h5")