
from flask import Flask, render_template, request, Blueprint, redirect,url_for
import pickle
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://khushi:emotiondetection@cluster0.o6kyn.mongodb.net/mydb?retryWrites=true&w=majority'
mongo = PyMongo(app)
emotiondetection = mongo.db.emotiondetection


@app.route('/')
def home():
    saved_emotion_classication = emotiondetection.find()
    return render_template('index.html',emotiondetection=saved_emotion_classication)


@app.route('/predict', methods=['POST'])
def predict():
    loaded_model = pickle.load(open('svm_model.sav', 'rb'))
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        print(data)
        my_prediction = loaded_model.predict(data)[0]
        emotion = int(my_prediction)
        print(my_prediction)
        emotiondetection.insert_one({'text' : message, 'emotion_prediction' : emotion})
        saved_emotion_classication = emotiondetection.find()

    return render_template('index.html', prediction=my_prediction,emotiondetection=saved_emotion_classication)



@app.route('/delete/<oid>')
def delete(oid):
    emotiondetection.delete_one({'_id': ObjectId(oid)})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
=======
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

