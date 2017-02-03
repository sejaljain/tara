import flask
import requests
import python-firebase

app = Flask(__name__)

@app.route("/")
def hello():
	return flask.render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, this page was not found.", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")




