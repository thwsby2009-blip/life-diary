"""
Music Prompt Proxy Server
小後端：接收圖片 → 送 Gemini Vision → 回傳音樂 prompt
"""
import os
import io
import base64
from flask import Flask, request, jsonify
from PIL import Image
import google.generativeai as genai

app = Flask(__name__)

# 請替換成你的 Gemini API Key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = (
    "You are a music mood master. Analyze the colors, emotions, and setting of this image. "
    "Generate a highly descriptive music prompt for Suno AI or Gemini Music. "
    "The prompt must be in English, descriptive, including genre, mood, instruments, and tempo. "
    "Do NOT include any introduction, explanations, markdown formatting, or quotation marks. "
    "Just output the prompt text directly. "
    "Example: A cozy acoustic indie pop song, warm guitar strings, raining outside mood, slow tempo, peaceful."
)

@app.route("/generate-music-prompt", methods=["POST"])
def generate():
    if not GEMINI_API_KEY:
        return jsonify({"error": "GEMINI_API_KEY not set"}), 500

    # 取得圖片（支援 base64 或 multipart）
    image_data = None

    # 1. Try base64 in JSON body
    body = request.get_json(silent=True)
    if body and "image_base64" in body:
        img_bytes = base64.b64decode(body["image_base64"])
        image_data = Image.open(io.BytesIO(img_bytes))

    # 2. Try multipart file upload
    elif request.files and "image" in request.files:
        img_file = request.files["image"]
        image_data = Image.open(img_file)

    if not image_data:
        return jsonify({"error": "No image provided"}), 400

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content([image_data, SYSTEM_PROMPT])
        return jsonify({"prompt": response.text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)