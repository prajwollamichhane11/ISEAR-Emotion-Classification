import pickle

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Loading the vectorizer
    cv = pickle.load(open("../models/vectorizer.pickle", "rb"))

    # Loading the classifier
    pickleFile = open("../models/nb_Classifier.pickle", "rb")
    naiveBayesClf = pickle.load(pickleFile)

    if request.method == "POST":
        message = request.form["message"]
        usrInp = [message]
        vect = cv.transform(usrInp)
        emoPrediction = naiveBayesClf.predict(vect)
        print(emoPrediction)

    return render_template("index.html", prediction=emoPrediction)


if __name__ == "__main__":
    app.run()