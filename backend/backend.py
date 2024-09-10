# backend.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide both num1 and num2"}), 400
    try:
        total = float(num1) + float(num2)
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400
    return jsonify({"sum": total})

if __name__ == '__main__':
    # Listen on all IPs to expose to the internet
    app.run(host='0.0.0.0', port=9000)
