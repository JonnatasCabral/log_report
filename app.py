from flask import Flask
from log_report.reports import get_players_ranking
from flask import render_template
from log_report.db import MongoDB

app = Flask('log_report')
app.config.from_object(__name__)

db = MongoDB(
        database_name='quake',
        collection_name='games'
        )


@app.route("/")
def ranking():
    entries = get_players_ranking(db)
    return render_template('ranking.html', entries=entries)
