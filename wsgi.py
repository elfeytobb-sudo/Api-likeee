from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "API ONLINE", "creator": "elfeytobb"})

@app.route('/like')
def like():
    uid = request.args.get('uid')
    region = request.args.get('server_name', 'US')
    if not uid:
        return jsonify({"error": "uid required"}), 400
    return jsonify({"status": 1, "uid": uid, "server": region, "likes": "test working"})

# Vercel necesita esto
def handler(event, context):
    return app(event, context)
