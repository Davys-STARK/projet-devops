from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUETES = Counter("app_requetes_total", "Nombre de requetes")

@app.route("/")
def accueil():
    REQUETES.inc()
    return "Bonjour, version 2 c'est LONSOK YANN !"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)