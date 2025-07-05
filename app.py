from flask import Flask, render_template, request, redirect
import os
import json
from datetime import datetime

app = Flask(__name__, template_folder='templates')

@app.route('/')
def redirect_to_home():
    return redirect('/home')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    articles = []
    for filename in os.listdir("articles"):
        filepath = os.path.join("articles", filename)
        with open(filepath, 'r') as f:
            article_data = json.load(f)
            articles.append(article_data)
    return render_template('home_page.html', articles = articles)

@app.route('/article')
def make_article():
    return render_template('make_article.html')

@app.route('/article/<int:id>')
def article(id):
    articles = []
    for filename in os.listdir("articles"):
        filepath = os.path.join("articles", filename)
        with open(filepath, 'r') as f:
            article_data = json.load(f)
            articles.append(article_data)
    article = articles[id]
    return render_template('article.html', article=article)

@app.route('/submit_article', methods=["POST"])
def submit():
    data = {
        'title': request.form.get('title'),
        'content': request.form.get('content'),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    filename = f"{data['title'].replace(' ', '_')}.json"
    filepath = os.path.join("articles", filename)

    with open(filepath, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return redirect('/home')

@app.route('/delete_article/<int:id>')
def delete(id):
    articles = []
    for filename in os.listdir("articles"):
        filepath = os.path.join("articles", filename)
        with open(filepath, 'r') as f:
            article_data = json.load(f)
            articles.append(article_data)
    os.remove(os.path.join("articles", f"{articles[id]["title"]}.json"))
    return redirect('/home')

@app.route('/edit_article/<int:id>')
def edit(id):
    articles = []
    for filename in os.listdir("articles"):
        filepath = os.path.join("articles", filename)
        with open(filepath, 'r') as f:
            article_data = json.load(f)
            articles.append(article_data)
    article = articles[id]
    return render_template('edit_article.html', article=article)

@app.route('/save/<string:article_title>', methods=["POST"])
def save(article_title):
    data = {
        'title': request.form.get('title'),
        'content': request.form.get('content'),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    filename = f"{data['title'].replace(' ', '_')}.json"
    filepath = os.path.join("articles", f"{article_title}.json")

    with open(filepath, 'w+') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    os.rename(os.path.join("articles", f"{article_title}.json"), 
              os.path.join("articles", filename))

    return redirect('/home')

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="127.0.0.1")