from flask import Flask
from flask import request

from db import increase_views_count, get_view_stats

app = Flask(__name__)


@app.route("/visit", methods=["GET"])
def visit_resource():
    increase_views_count(request)
    return f"Hi, your IP is {request.remote_addr}."


@app.route("/stats", methods=["GET"])
def stats_resource():
    return get_view_stats()


if __name__ == '__main__':
    app.run(debug=True)
