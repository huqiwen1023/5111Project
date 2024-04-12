from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_text = request.form['input']
    processed_text = mbti_prediction([input_text])
    print(processed_text)
    return processed_text

def mbti_prediction(input_data):
    data=pd.read_csv('./static/mbti_1.csv')
    X_train, X_test, y_train, y_test = train_test_split(data['posts'], data['type'], test_size=0.2, random_state=123)
    tfidf = TfidfVectorizer(stop_words='english')
    X_train = tfidf.fit_transform(X_train)
    X_test = tfidf.transform(X_test)
    from sklearn.linear_model import SGDClassifier
    from sklearn.metrics import classification_report
    model3 = SGDClassifier()
    model3.fit(X_train, y_train)
    #y_predicted = model3.predict(X_test)
    input_data = tfidf.transform(input_data)
    return model3.predict(input_data)[0]


if __name__=='__main__':
    app.run()