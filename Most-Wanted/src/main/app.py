from flask import Flask, render_template
from fbi import FBI
from AppleMusicPods import Podcasts

app = Flask(__name__)

# fetch once at startup, not on every page load
fbi = FBI()
fbi.makeDict()
murderers = fbi.fbidict


@app.route("/")
def index():
    return render_template("index.html", people=murderers)


@app.route("/person/<name>")
def person(name):
    podcast = Podcasts(name)
    shows = podcast.inspect_first_result(podcast.search_episodes())
    return render_template("person.html", name=name, shows=shows)


if __name__ == "__main__":
    app.run(debug=True)