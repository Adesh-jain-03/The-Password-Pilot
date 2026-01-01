from flask import Flask, render_template, request, jsonify
from checker import check_password_strength
from generator import generate_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])  # <--- MUST BE /check
def check():
    data = request.json
    email = data.get("email", "")
    password = data.get("password", "")
    
    is_strong, feedback = check_password_strength(email, password)
    return jsonify({"strong": is_strong, "feedback": feedback})

@app.route('/generate')
def generate():
    new_pass = generate_password()
    return jsonify({"password": new_pass})

if __name__ == "__main__":
    app.run(debug=True)
    