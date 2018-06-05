from flask import Flask, request

app = Flask(__name__, static_url_path='')

@app.route('/')
def redirect():
	return app.send_static_file('content.html')

if __name__ == "__main__":
	app.run(host= '127.0.0.1', port=5003)