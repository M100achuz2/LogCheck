from flask import Flask, render_template, request
from slack import search

app = Flask(__name__)


@app.route("/")
def main():
    """ home page """
    return render_template("index.html")


@app.route("/id")
def results():
    """ show table of results """
    id_device = request.values.to_dict()["id-device"]

    if not id_device:
        return render_template("error.html")  # return error in-case the user search for empty query

    match = search(id_device)
    if isinstance(match, dict):
        return render_template("results.html", info=match)  # return results
    elif isinstance(match, bool):
        return render_template("error.html")  # return error if the search getting False
    elif not match:
        return render_template("no_results.html", query=id_device)  # return no-results in case the search didn't found anything


# === TEST ===
@app.route('/error')
def error():
    return render_template('error.html')


@app.route('/no')
def no_results():
    return render_template('no_results.html')


# app.run(host="0.0.0.0")
