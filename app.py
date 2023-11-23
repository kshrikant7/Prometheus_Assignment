from flask import Flask
from prometheus_client import Counter, Gauge, generate_latest, REGISTRY
import psutil

app = Flask(__name__)

request_counter = Counter('flask_requests_total', 'Total number of requests received')

# Define a gauge for CPU usage
cpu_usage = Gauge('flask_cpu_usage_percent', 'CPU usage percentage')

@app.route('/metrics')
def metrics():
    # Update CPU usage gauge
    cpu_percent = psutil.cpu_percent()
    cpu_usage.set(cpu_percent)

    # Generate metrics response
    return generate_latest(REGISTRY)

@app.route('/')
def hello_world():
    request_counter.inc()
    return 'Hello World'

if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0', port=5000)
