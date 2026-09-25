from flask import Flask, request, jsonify, render_template_string
from src.routing import route_prompt
from src.database import initialize_db, save_result

app = Flask(__name__)

initialize_db()


def simple_sentiment(text):
    negative = {
        "angry", "frustrated", "unhappy", "worst",
        "disappointing", "failed", "failure", "problem"
    }

    positive = {
        "great", "good", "excellent",
        "happy", "thanks", "thank"
    }

    words = set(text.lower().split())

    negative_count = len(words & negative)
    positive_count = len(words & positive)

    if negative_count > positive_count:
        return "Negative"

    if positive_count > negative_count:
        return "Positive"

    return "Neutral"


HTML = """
<!DOCTYPE html>
<html>
<head>

    <title>Prompt Routing System</title>

    <style>

        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 700px;
            margin: 80px auto;
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }

        h1 {
            text-align: center;
            color: #222;
        }

        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }

        textarea {
            width: 100%;
            height: 120px;
            padding: 15px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 8px;
            resize: none;
            box-sizing: border-box;
        }

        button {
            width: 100%;
            margin-top: 20px;
            padding: 15px;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            background: #222;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background: #444;
        }

        .result {
            margin-top: 30px;
            padding: 25px;
            background: #f1f5f9;
            border-radius: 10px;
        }

        .result p {
            font-size: 17px;
        }

        .label {
            font-weight: bold;
        }

    </style>

</head>

<body>

<div class="container">

    <h1>🤖 Prompt Routing System</h1>

    <p class="subtitle">
        NLP-based Prompt Classification and Routing
    </p>

    <form method="POST">

        <textarea
            name="prompt"
            placeholder="Enter your prompt here..."
            required
        >{{ prompt }}</textarea>

        <button type="submit">
            Route Prompt
        </button>

    </form>

    {% if result %}

    <div class="result">

        <p>
            <span class="label">Category:</span>
            {{ result.category }}
        </p>

        <p>
            <span class="label">Route:</span>
            {{ result.route }}
        </p>

        <p>
            <span class="label">Confidence:</span>
            {{ result.confidence }}
        </p>

        <p>
            <span class="label">Method:</span>
            {{ result.method }}
        </p>

        <p>
            <span class="label">Sentiment:</span>
            {{ result.sentiment }}
        </p>

    </div>

    {% endif %}

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    prompt = ""

    if request.method == "POST":

        prompt = request.form.get("prompt", "").strip()

        if prompt:

            result = route_prompt(prompt)

            result["prompt"] = prompt

            result["sentiment"] = simple_sentiment(prompt)

            save_result(result)

    return render_template_string(
        HTML,
        result=result,
        prompt=prompt
    )


@app.post("/route")
def route():

    data = request.get_json(silent=True) or {}

    prompt = str(data.get("prompt", "")).strip()

    if not prompt:

        return jsonify({
            "error": "prompt is required"
        }), 400

    result = route_prompt(prompt)

    result["prompt"] = prompt

    result["sentiment"] = simple_sentiment(prompt)

    save_result(result)

    return jsonify(result)


if __name__ == "__main__":

    app.run(debug=True)