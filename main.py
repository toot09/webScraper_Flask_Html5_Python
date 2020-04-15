from flask import Flask, render_template, request, redirect
from scraper import get_jobs
app = Flask("SuperScraper")

# @ : decorator
@app.route("/")
def home():
  # render_template get html template
  return render_template("main.html")

@app.route("/search")
def search():
  #request.args
  word = request.args.get("word")
  # 입력값이 None(null)이면 소문자처리, 입력값없으면 홈으로(/) redirect
  if word: 
    word = word.lower()
    jobs = get_jobs(word)
    print(jobs)
  else:
    return redirect("/")
  return render_template("search.html",word=word)
  #return f"Do you want find \"{word}\" jobs?"

# Should use param(username) in instance
#@app.route("/<username>")
#def contact(username):
#  return f"Hello! {username}. How are you doing?"

app.run(host="0.0.0.0")