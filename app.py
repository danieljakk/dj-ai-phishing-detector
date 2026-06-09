from flask import Flask, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")


def explain(email):
    email = email.lower()
    reasons = []

    patterns = {
        "urgent": "high urgency language detected",
        "verify": "requests account verification",
        "click": "contains external link prompt",
        "password": "mentions sensitive credential (password)",
        "account": "references account access or security",
        "bank": "financial institution reference",
        "gift": "possible reward/scam incentive",
        "free": "unusual free reward claim"
    }

    for word, reason in patterns.items():
        if word in email:
            reasons.append(reason)

    return "; ".join(reasons) if reasons else "no strong phishing indicators detected"


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    email_text = ""

    if request.method == "POST":
        email_text = request.form["email"]

        prediction = model.predict([email_text])[0]

        # confidence score
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba([email_text])[0]
            confidence = round(max(prob) * 100, 2)
        else:
            confidence = "N/A"

        reasons = explain(email_text)

        if prediction == "phishing":
            risk_note = "Model detected phishing patterns based on training data."
        else:
            risk_note = "Message appears consistent with normal communication patterns."

        result = f"""
        <div style="font-size:24px;"><b>{prediction.upper()}</b></div>
        <div style="font-size:18px;">{confidence}% confidence</div>

        <div style="margin-top:10px; font-size:16px;">
        Why: {reasons}
        </div>

        <div style="margin-top:10px; font-size:14px; opacity:0.8;">
        {risk_note}
        </div>
        """

    return f"""
    <html>
    <head>
        <title>DJ AI Phishing Detector</title>

        <style>
        body {{
            font-family: Arial;
            background: linear-gradient(135deg, #667eea, #764ba2);
            text-align: center;
            padding: 40px;
            color: white;
        }}

        .box {{
            background: white;
            padding: 25px;
            border-radius: 12px;
            width: 60%;
            margin: auto;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
            color: black;
        }}

        textarea {{
            width: 90%;
            height: 150px;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }}

        button {{
            padding: 12px 25px;
            background-color: #4CAF50;
            color: white;
            border: none;
            margin-top: 10px;
            cursor: pointer;
            border-radius: 8px;
            font-size: 16px;
        }}

        button:hover {{
            background-color: #45a049;
        }}
        </style>
    </head>

    <body>
        <h1>DJ AI Phishing Detector</h1>

        <p style="font-size:14px; opacity:0.7;">
            DJ/AI-PHISHING-DETECTOR
        </p>

        <div class="box">
            <h2>Analyze Email Security Risk</h2>

            <form method="POST">
                <textarea name="email" placeholder="Paste an email here...">{email_text}</textarea><br>
                <button type="submit">Analyze</button>
            </form>

            <div style="margin-top:20px;">
                {result}
            </div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
