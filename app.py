import os
from flask import Flask, render_template, request, jsonify
from engine import GameEngine
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
engine = GameEngine()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    cmd = request.json.get('command', '').lower().strip()
    return jsonify({"output": engine.process(cmd), "level": engine.current_level})

if __name__ == '__main__':
    app.run(port=5000)
