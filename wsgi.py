from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(status="ONLINE")

@app.route('/like')
def like():
    uid = request.args.get('uid')
    if not uid:
        return jsonify(error="uid required")
    return jsonify(status=1, uid=uid)
    
