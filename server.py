from flask import Flask, render_template, request, Response
import json
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    json_response = json.dumps(response, indent=4, sort_keys=False)  
    return Response(json_response, mimetype='application/json')  


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run("0.0.0.0", port = 5000, debug = True)