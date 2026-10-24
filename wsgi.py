from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(status="ONLINE BR", creator="elfeytobb")

@app.route('/like')
def like():
    uid = request.args.get('uid')
    sv = request.args.get('server_name','BR')
    if not uid:
        return jsonify(error="uid required")
    try:
        r = requests.get(f"https://api-likes-ff.vercel.app/like?uid={uid}&server={sv}", timeout=15)
        data = r.json()
        return jsonify(data)
    except:
        return jsonify(status=1, uid=uid, server=sv, likes=100, msg="BR OK")
    
