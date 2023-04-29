import pickle


def predict(data):
    loaded_model = pickle.load(open("rentpred.sav", 'rb'))
    return loaded_model.predict(data)
    rt = joblib.load('label_encoder.sav')
    return lr.predict(data)
    t = joblib.load('scaler.sav')
    return lr.predict(data)
