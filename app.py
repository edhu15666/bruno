import time
import random

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'zapp', version='1.0.0')


@app.route('/status')
def healthcheck():
    time.sleep(random.random() * 0.1)
    return "success", 200

@app.route('/tasks')
def tasks():
    time.sleep(random.random() * 0.3)
    return 'ok', 200

# It should return 500
@app.route('/failone')
def fail_one():
    time.sleep(random.random() * 0.5)
    return "Error 5xx", 500
# It should return 400
@app.route('/failtwo')
def fail_two():
    time.sleep(random.random() * 0.3)
    return "Error 4xx", 400

@app.route('/failthree')
def fail_three():
    time.sleep(random.random() * 0.8)
    raise Exception

if __name__ == "__main__":
    app.run(host="0.0.0.0")

@app.route('/')
def index():
    return 'Teste realizado!!!'
    
    
