from flask import Flask, render_template, request, jsonify
import secrets
import string
import math

app = Flask(__name__)

# ------------------------------
# Random password generator (with entropy)
# ------------------------------
def password_generator(password_length: int = 16):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    full_pool = lower + upper + digits + symbols

    # Generate password
    password_chars = [secrets.choice(full_pool) for _ in range(password_length)]
    gen_password = "".join(password_chars)

    # Calculate entropy
    entropy = password_length * math.log2(len(full_pool))
    entropy = round(entropy)

    return gen_password, entropy

# ------------------------------
# Chunked password generator
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
    return render_template("home.html")  # Home page with links

@app.route("/chunked")
def chunked():
    return render_template("chunked.html")  # Chunked password page

@app.route("/random")
def random_page():
    return render_template("random.html")  # Random password page

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    length = int(data.get("length", 16))  # default length = 16

    password, entropy = password_generator(length)

    return jsonify({
        "password": password,
        "entropy": entropy
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

@app.route("/contact")
def contact():
    return render_template("email_reminder.html")

# ------------------------------
# RUN APP
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
