from flask import Flask, render_template, request, jsonify
import secrets
import string

app = Flask(__name__)

# ------------------------------
# V1: Simple random password
# ------------------------------
def password_generator(password_length: int = 16):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    full_pool = lower + upper + digits + symbols

    password_chars = [secrets.choice(full_pool) for _ in range(password_length)]
    gen_password = "".join(password_chars)

    return gen_password

# ------------------------------
# V2: Chunked password
# ------------------------------
def password_generator_v2(chunk_length: int = 4, chunk_size: int = 4):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    all_chars = lower + upper + digits
    pools = []

    for _ in range(chunk_length):
        pool = ''.join(secrets.choice(all_chars) for _ in range(chunk_size))
        pools.append(pool)

    full_pool = '-'.join(pools)
    return full_pool

# ------------------------------
# ROUTES
# ------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/v2")
def home_v2():
    return render_template("index_v2.html")

@app.route("/v3")
def home_v3():
    return render_template("index_v3.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    length = int(data.get("length", 16))  # default length = 16

    password = password_generator(length)

    return jsonify({
        "password": password
    })

@app.route("/generate_v2", methods=["POST"])
def generate_v2():
    data = request.get_json()
    chunk_length = int(data.get("chunk_length", 4))
    chunk_size = int(data.get("chunk_size", 4))

    password = password_generator_v2(chunk_length, chunk_size)

    return jsonify({
        "password": password
    })

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/email_reminder")
def email_reminder():
    return render_template("email_reminder.html")

# ------------------------------
# RUN APP
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
