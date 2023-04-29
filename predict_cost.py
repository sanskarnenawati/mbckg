import pickle


def predict(data):
    lr = pickle.load(open("rentpred.sav", 'rb'))
    return lr.predict(data)
    rt = joblib.load('label_encoder.sav')
    return lr.predict(data)
    t = joblib.load('scaler.sav')
    return lr.predict(data)
