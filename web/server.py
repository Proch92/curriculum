from flask import Flask, render_template
import json

app = Flask(__name__, static_url_path='')


@app.route('/')
def curr():
    f = open('content.json')
    data = json.load(f)
    return render_template('content.html', data=data)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5003)
