# frontend.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    
    # Replace with your server's public IP or domain name
    response = requests.post('backend-service:9000/sum', json={'num1': num1, 'num2': num2})

    
    if response.status_code == 200:
        result = response.json().get('sum')
        return render_template('index.html', result=result)
    else:
        error = response.json().get('error')
        return render_template('index.html', error=error)

if __name__ == '__main__':
    # Listen on all IPs to expose to the internet
    app.run(host='0.0.0.0', port=8080)
