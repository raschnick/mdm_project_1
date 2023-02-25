import joblib
from flask import Flask, jsonify, render_template, request
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    cv_vocabulary = open('models/cv_vocabulary.pkl', 'rb')
    cv = joblib.load(cv_vocabulary)
    spam_model = open('models/sms_spam_model.pkl', 'rb')
    spam_predictor = joblib.load(spam_model)

    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = spam_predictor.predict(vect)
        return render_template('result.html', prediction = my_prediction)




if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True)
    app.run()
