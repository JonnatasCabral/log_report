from flask import Flask
from .reports import players_ranking
from flask import render_template

app = Flask('log_report')
app.config.from_object(__name__)


@app.route("/")
def hello():
    entries = players_ranking()
    return render_template('ranking.html', entries=entries)
