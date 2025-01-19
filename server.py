"""
Emotion Detector Flask Server
This module provides a simple Flask server to detect emotions from input text.
"""
import json
from flask import Flask, render_template, request, Response
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the input text and return the detected emotion as JSON.
    The endpoint accepts a query parameter 'textToAnalyze',
    processes it with the emotion detection module, and returns
    the result in JSON format.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "Invalid input! Try again."

    json_response = json.dumps(response, indent=4, sort_keys=False)
    return Response(json_response, mimetype='application/json')


@app.route("/")
def render_index_page():
    """
    Render the main index page of the application.
    
    This function serves the HTML page located in the templates directory.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run("0.0.0.0", port = 5000, debug = True)
