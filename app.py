from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/services', methods=['GET'])
def get_services():
    services = [
        {"id": 1, "title": "Web Development", "icon": "fa-globe", "description": "Responsive, fast and modern websites using HTML, CSS and JavaScript.", "tags": ["HTML", "CSS", "JavaScript"]},
        {"id": 2, "title": "Android App Development", "icon": "fa-mobile-alt", "description": "Custom Android applications for your business built with Java and Kotlin.", "tags": ["Java", "Kotlin", "Android"]},
        {"id": 3, "title": "Python Programming", "icon": "fa-code", "description": "Python scripts and automation tools to save your time and make work faster.", "tags": ["Python", "Automation", "Scripts"]},
        {"id": 4, "title": "Database Solutions", "icon": "fa-database", "description": "Efficient MySQL databases that are organized, fast and secure.", "tags": ["MySQL", "SQL", "Database"]}
    ]
    return jsonify(services)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    service = data.get('service')
    message = data.get('message')
    print(f"\n📩 New Contact Request!")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Service: {service}")
    print(f"Message: {message}\n")
    return jsonify({"status": "success", "message": "Thank you! We will reply within 24 hours."})

import os

if __name__ == '__main__':
    print("\n🚀 EshwaraTech Solutions Server Started!")

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
