
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import pandas as pd

#import libraries and initiate required objects for processing
tokenizer = nltk.tokenize.TreebankWordTokenizer()
stop_words = stopwords.words("english")
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()
def process_text(text):
    #convert text to lowercase
    text= text.apply(lambda x:x.lower())
    #remove multiple spaces from text
    text= text.apply(lambda x:re.sub(' +', ' ',x))
    # remove alpha numeric characeter from text using regex
    text= text.apply(lambda x:x.lower())
    text.str.replace(r"\d+", "")
    text.str.replace('[^\w\s]','')
    text.str.replace(r"[︰-＠]", "")
    text.str.replace(r"", "")
    text.str.replace('\d+', '')
    #tokenize 
    text = text.apply(tokenizer.tokenize)
    #remove english stop words form text
    text =text.apply(lambda x: [item for item in x if item not in stop_words])
    #stemming text
    text =text.apply(lambda x: [stemmer.stem(e) for e in x])
    #stripping spaces from items of array of texts
    text=text.apply(lambda x: [e.strip() for e in x])
    #remove all the characters from array of texts if the length of item is 1
    text=text.apply( lambda x: [ y for y in x if len(y)>1 ])
    #remove all the digits from the text
    text=text.apply( lambda x: [ y for y in x if not y.isdigit()] )
    # lemattizing text
    text = text.apply(lambda x: ' '.join(lemmatizer.lemmatize(token) for token in x))
    return text