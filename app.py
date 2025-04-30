from flask import Flask, render_template

app = Flask (__name__)

@app.route("/") # http://localhost:5000/ ou http://127.0.0.1:5000/
def home():
    return render_template("index.html") # por padrão já irá retornar o arquivo index.html dentro da pasta templates