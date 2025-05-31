from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import socket
import random
import math
import os
app = Flask(__name__)
CORS(app)
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80)) 
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1" 
    finally:
        s.close()
    return ip
server_ip = get_local_ip()
print("Host IP Address:", server_ip)
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return [round(root, 4)]
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [round(root1, 4), round(root2, 4)]
@app.route('/')
def home():
    return send_from_directory(os.getcwd(), "index.html")
@app.route('/solve', methods=['GET'])
def solve():
    a = request.args.get('a', type=float) or round(random.uniform(1, 10), 4)
    b = request.args.get('b', type=float) or round(random.uniform(-10, 10), 4)
    c = request.args.get('c', type=float) or round(random.uniform(-10, 10), 4)
    roots = solve_quadratic(a, b, c)
    return jsonify({
        "a": a,
        "b": b,
        "c": c,
        "roots": roots,
        "server_ip": server_ip  
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
