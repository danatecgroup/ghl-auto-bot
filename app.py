import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
GPT_ID = "g-685458cfc9408191bf5a9ae37c230092"

@app.route("/", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_message}],
            tools=[{"type": "gpt", "gpt_id": GPT_ID}],
            tool_choice={"type": "gpt", "gpt_id": GPT_ID}
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Kļūda sazinoties ar sistēmu: {e}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
