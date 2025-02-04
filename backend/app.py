from flask import Flask, jsonify, request
import requests
import fetch_news
import mod_data

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to TheWhatReport"})

@app.route('/trending')
def trending():
    trends = mod_data.getTopWords()
    return trends

@app.route('/headlines')
def headlines():
    query = request.args.get('query', 'world')
    headlines = fetch_news.fetch_news_keyword(query)
    return jsonify(headlines)

if __name__ == '__main__':
    app.run(debug=True)

