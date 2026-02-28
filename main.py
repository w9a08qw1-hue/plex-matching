from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 설정하신 비밀 토큰입니다.
MY_TOKEN = "plex15" 

@app.route('/')
def home():
    # 주소 뒤에 ?token=plex15 가 없으면 접속을 차단합니다.
    token = request.args.get('token')
    if token != MY_TOKEN:
        return "Access Denied (Unauthorized)", 403
    return "<h1>Plex Agent is Running!</h1><p>Secure Mode Active</p>"

@app.route('/match')
def match():
    # Plex 요청 시에도 토큰이 맞는지 확인합니다.
    token = request.args.get('token')
    if token != MY_TOKEN:
        return jsonify({"error": "Unauthorized"}), 403
    
    title = request.args.get('title', 'Unknown')
    return jsonify({
        "status": "success",
        "results": [
            {"title": title, "year": 2026, "score": 100}
        ]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
