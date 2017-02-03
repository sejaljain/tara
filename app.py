import flask
import requests
import firebase

app = flask.Flask(__name__)

@app.route("/index.html")
def hello():
	return flask.render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, this page was not found.", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")

