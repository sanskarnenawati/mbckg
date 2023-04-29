import pickle


def predict(data):
    loaded_model = pickle.load(open("C:\Users\sansk\PycharmProjects\deployed\rentpred.sav", 'rb'))
    return loaded_model.predict(data)
    rt = joblib.load('C:/Users/sansk/PycharmProjects/deployed/label_encoder.sav')
    return lr.predict(data)
    t = joblib.load('C:/Users/sansk/PycharmProjects/deployed/scaler.sav')
    return lr.predict(data)
