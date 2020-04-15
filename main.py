from flask import Flask
app = Flask("SuperScraper")

# @ : decorator
@app.route("/")
def home():
  return "hello!"

@app.route("/contact")
def contact():
  return "Contact me!"

app.run(host="0.0.0.0")