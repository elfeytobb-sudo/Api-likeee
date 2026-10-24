from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(status="ONLINE BR")

@app.route('/like')
def like():
    uid = request.args.get('uid')
    sv = request.args.get('server_name','BR')
    if not uid:
        return jsonify(error="uid required")
    return jsonify(status=1, uid=uid, server=sv, likes=300)
