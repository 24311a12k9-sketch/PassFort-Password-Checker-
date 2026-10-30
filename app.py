
from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = None
    password = ""

    if request.method == "POST":
        password = request.form.get("password", "")

        rules = {
            "At least 8 characters": len(password) >= 8,
            "Contains an uppercase letter": bool(re.search(r"[A-Z]", password)),
            "Contains a lowercase letter": bool(re.search(r"[a-z]", password)),
            "Contains a digit": bool(re.search(r"\d", password)),
            "Contains a special symbol": bool(re.search(r"[^a-zA-Z0-9\s]", password)),
            "No whitespace": not bool(re.search(r"\s", password))
        }

        passed = sum(rules.values())

        results = {
            "rules": rules,
            "passed": passed,
            "total": len(rules),
            "secure": all(rules.values())
        }

    return render_template(
        "index.html",
        results=results,
        password=password
    )

if __name__ == "__main__":
    app.run(debug=True)
