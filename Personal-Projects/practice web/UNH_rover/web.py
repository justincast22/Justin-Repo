from flask import Flask, render_template, jsonify
import psutil
import subprocess


app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/arms")
def arms_page():
    return render_template("arms.html")

@app.route("/treads")
def treads_page():
    return render_template("treads.html")

@app.route("/cameras")
def cameras_page():
    return render_template("cameras.html")

@app.route('/cpu_usage')
def cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return jsonify({"cpu_usage": cpu_usage})

@app.route('/cpu_temp')
def cpu_temp():
    try:
        temp = subprocess.check_output(["osx-cpu-temp"]).decode().strip()
    except:
        temp = "N/A"
    return jsonify({"cpu_temp": temp})

@app.route('/cpu_freq')
def cpu_freq():
    freqs = psutil.cpu_freq(percpu=True)
    # Convert objects to dictionaries
    freqs_dict = [freq._asdict() for freq in freqs]
    return jsonify({"cpu_freq": freqs_dict})

@app.route('/memory_usage')
def memory_usage():
    memory_usage = psutil.virtual_memory().percent
    return jsonify({"memory_usage": memory_usage})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
