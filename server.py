from flask import Flask, render_template, redirect
app = Flask(__name__)
# app.secret_key("Coding is fun")

@app.route("/")
def start_page():
    return redirect("/play")

@app.route("/play")
@app.route("/play/<int:num>")
@app.route("/play/<int:num>/<string:color>")
def populate_page(num = 1, color = "aqua"):
    return render_template("index.html", num = num, color = color)


if __name__ == '__main__':
    app.run(debug=True)
