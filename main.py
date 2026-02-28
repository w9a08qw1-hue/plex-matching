from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    # 서버가 잘 돌아가는지 확인용 페이지
    return "<h1>Plex Agent is Running!</h1><p>Render + Python 3</p>"

@app.route('/match')
def match():
    # Plex가 정보를 요청할 때 응답하는 부분
    title = request.args.get('title', 'Unknown')
    return jsonify({
        "status": "success",
        "results": [
            {"title": title, "year": 2026, "score": 100}
        ]
    })

if __name__ == "__main__":
    # Render의 포트 설정에 맞게 실행
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
