from flask import Flask, render_template, request, redirect, send_file
from scraper import get_jobs
from exporter import save_to_file

app = Flask("SuperScraper")
# fake DB : dictionary 형태로 데이터 담아둔다.
db = {}

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
    # 기존에 조회했던 기록이 있다면 fake DB에서 가져온다. (for Saving time)
    checkData = db.get(word)

    if checkData:
      jobs = checkData
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")

  return render_template(
  "search.html",
  word=word,
  length = len(jobs),
  jobs = jobs
  )
  #return f"Do you want find \"{word}\" jobs?"

# Should use param(username) in instance
#@app.route("/<username>")
#def contact(username):
#  return f"Hello! {username}. How are you doing?"

@app.route("/export")
def export():
  try:
    word = request.args.get("word")
    if not word:
      raise Exception();
    jobs = db.get(word)
    if not jobs:
      raise Exception();
    save_to_file(jobs)
    # Use send_file library to file export
    return send_file("jobs.csv")
  except:
    return redirect("/")

app.run(host="0.0.0.0")