import threading

import flask

app = flask.Flask("s")


@app.route("/")
def hi():
    return "ah ah ah ah stayin' alive, stayin' alive, we're ah ah ah ah STAYIN ALIVEEEEEEEEE IVEEEEE I I I IVEEEE OOOOO... immm alive! now i can die..."


def run():
    app.run("0.0.0.0")


def start():
    threading.Thread(target=run).start()
