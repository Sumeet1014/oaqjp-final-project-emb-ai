
"""Flask web application for the Emotion Detector project."""

from flask import Flask, request, render_template_string
from EmotionDetection import emotion_detector

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Emotion Detector</title>
</head>
<body>
    <h1>Emotion Detector</h1>
    <form method="POST">
        <label for="textToAnalyze">Enter text to analyze:</label>
        <input id="textToAnalyze" name="textToAnalyze" type="text">
        <button type="submit">Analyze</button>
    </form>
    <div id="result">{{ result }}</div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    """Display the form and process emotion analysis requests."""
    result = ""

    if request.method == "POST":
        text_to_analyze = request.form.get("textToAnalyze", "").strip()

        if not text_to_analyze:
            result = "Please enter some text to analyze."
        else:
            emotions = emotion_detector(text_to_analyze)

            if emotions["dominant_emotion"] is None:
                result = "Unable to analyze the text. Please try again."
            else:
                result = (
                    f"Dominant emotion: {emotions['dominant_emotion']}"
                )

    return render_template_string(HTML_PAGE, result=result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
