from flask import Flask, jsonify

app = Flask(__name__)

iller = [
    {"ad": "Adana"},
    {"ad": "Ankara"},
    {"ad": "Istanbul"},
    {"ad": "Eskisehir"},
    {"ad": "Düzce"},
    {"ad": "Sakarya"},
    {"ad": "Tekirdağ"},
    {"ad": "Edirne"},
    {"ad": "Antalya"},
    {"ad": "Gaziantep"},
    {"ad": "Trabzon"}
]

@app.route("/")
def hello():
    return "Merhaba Python!"

@app.route("/staj")
def get_random_il():
    return jsonify(iller.pop())

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5555)
