import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
GPT_ID = "g-685458cfc9408191bf5a9ae37c230092"

@app.route("/", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_message}],
            tools=[{"type": "gpt", "gpt_id": GPT_ID}],
            tool_choice={"type": "gpt", "gpt_id": GPT_ID}
        )
        reply = response.choices[0].message["content"]
    except Exception as e:
        reply = "Kļūda sazinoties ar sistēmu: " + str(e)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
