from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from openai import OpenAI
from datetime import datetime

# .envファイルから環境変数を読み込む
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# 日付を設定
today = datetime.today().strftime('%Y年%m月%d日')

app = Flask(__name__)

# グローバル変数でチャット履歴を保持
chat_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history
    if request.method == "POST":
        user_input = request.form["prompt"]
        chat_history.append({"role": "user", "content": user_input})

        # 新しいOpenAIクライアントでChat Completionを呼び出す
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"あなたは親切なアシスタントです。今日の日付は {today} です。"},
                *chat_history
            ]
        )

        ai_message = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": ai_message})

    return render_template("index.html", history=chat_history)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
