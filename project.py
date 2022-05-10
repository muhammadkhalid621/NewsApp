from flask import Flask, redirect, url_for, render_template, request
from scrapper import articles

app = Flask(__name__, template_folder='./templates')

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("main_page.html")

@app.route("/news")
def login():
    final_list = articles()    
    return render_template("news.html", list=final_list)


if __name__ == "__main__":
    app.run(debug=True)