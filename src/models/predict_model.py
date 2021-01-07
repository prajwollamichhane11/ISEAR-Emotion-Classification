from . import train_model


def predict_sentiment(inpText):
    inputText = inpText
    tokenizedSeq = train_model.tokenizer.texts_to_sequences([inputText])
    padSeq = train_model.pad_sequences(tokenizedSeq, maxlen=len(tokenizedSeq[0]))
    sentiment_value = train_model.model.predict(padSeq)
    return sentiment_value
