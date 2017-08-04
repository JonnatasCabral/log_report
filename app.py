from flask import Flask
from log_report.reports import get_players_ranking
from flask import render_template

app = Flask('log_report')
app.config.from_object(__name__)


@app.route("/")
def ranking():
    entries = get_players_ranking()
    return render_template('ranking.html', entries=entries)
