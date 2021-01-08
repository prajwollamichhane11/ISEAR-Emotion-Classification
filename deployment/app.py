# from ../src/models import train_model


import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/predict", methods=["POST"])
# def predict():

#     df = pd.read_csv("ISEAR.csv", names=["emotion", "text"])
#     X = df["text"]

#     # Vectorization
#     cv = CountVectorizer(stop_words="english")
#     X = cv.fit(X)
#     X = cv.transform(X)

#     # Loading the classifier
#     pickleFile = open("../models/nb_Classifier.pickle", "rb")
#     naiveBayesClf = pickle.load(pickleFile)
#     pickleFile.close()

#     vector = CountVectorizer(vocabulary=cv.vocabulary_)
#     if request.method == "POST":
#         message = request.form["message"]
#         usrInp = [message]
#         vect = vector.transform(usrInp)
#         emoPrediction = naiveBayesClf.predict(vect)
#         print(emoPrediction)

#     return render_template("index.html", prediction=emoPrediction)


# @app.route("/predict", methods=["POST"])
# def predict_sentiment(inpText):
#     inputText = inpText
#     tokenizedSeq = train_model.tokenizer.texts_to_sequences([inputText])
#     padSeq = train_model.pad_sequences(tokenizedSeq, maxlen=len(tokenizedSeq[0]))
#     sentiment_value = train_model.model.predict(padSeq)
#     return sentiment_value


@app.route("/predict", methods=["POST"])
def predict():
    df = pd.read_csv("ISEAR.csv", names=["emotion", "content"])
    # Features and Labels
    le = preprocessing.LabelEncoder()
    df["emotion"] = le.fit_transform(df["emotion"])

    X = df["content"]
    y = df["emotion"]

    # Extract Feature With CountVectorizer
    cv = CountVectorizer()
    X = cv.fit_transform(X)  # Fit the Data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=42
    )

    # Naive Bayes Classifier
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    clf.score(X_test, y_test)
    if request.method == "POST":
        message = request.form["message"]
        data = [message]
        vect = cv.transform(data)
        my_prediction = clf.predict(vect)
    return render_template("index.html", prediction=my_prediction)


if __name__ == "__main__":
    app.run()