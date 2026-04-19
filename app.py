from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Training
emails = ["invoice attached", "payment issue", "need help"]
labels = ["invoice", "complaint", "query"]

vectorizer = CountVectorizer()  
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']
    
    X_test = vectorizer.transform([text])
    result = model.predict(X_test)[0]
    
    return jsonify({"category": result})

if __name__ == "__main__":
    app.run(debug=True)
