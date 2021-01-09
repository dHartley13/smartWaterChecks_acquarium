import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Aquarium water conditions</h1><p>This site is a prototype API for testing water conditions of my fish tank.</p>"

app.run()