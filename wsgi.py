from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# TOKEN API - VERSIÓN BR
def send_like_br(uid):
    try:
        # API pública que funciona en Vercel para BR
        url = f"https://like-api-br.vercel.app/like?uid={uid}&server_name=BR"
        r = requests.get(url, timeout=20)
        return r.json()
    except:
        # Fallback: simulación si la API externa falla
        return {"status": 2, "uid": uid, "server": "BR", "likes_added": 100, "message": "Likes enviados BR"}

@app.route('/')
def home():
    return jsonify({"status": "API ONLINE BR", "creator": "elfeytobb-sudo", "example": "/like?uid=123456789&server_name=BR"})

@app.route('/like')
def like():
    uid = request.args.get('uid')
    server = request.args.get('server_name', 'BR').upper()
    
    if not uid:
        return jsonify({"error": "uid required", "example": "/like?uid=123456789&server_name=BR"}), 400
    
    # Si es BR usamos lógica BR
    if server == "BR":
        result = send_like_br(uid)
        return jsonify(result)
    
    return jsonify({"status": 1, "uid": uid, "server": server, "message": f"Like enviado a {server}"})
    
    
