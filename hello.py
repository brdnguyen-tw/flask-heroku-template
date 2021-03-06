from flask import Flask, Markup, redirect, render_template
app = Flask(__name__, static_url_path="", static_folder="data")

@app.route('/')
def hello_world():
    return render_template(
        "index.html"
    )

if __name__ == '__main__':
    app.run()
