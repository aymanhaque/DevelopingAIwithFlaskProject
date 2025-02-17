"""
server.py is a file made as apart of the IBM fullstack 
developer course for practicing building AI applications with Flask
"""
from flask import Flask, request, abort
from EmotionDetection import emotion_detection
app = Flask(__name__)

"""
Below are the api routes to handle different
functions of the AI app
"""
@app.route('/')
def hello_world():
    """
    Simple function that return shello world
    """
    return 'Hello, World!'

@app.route('/emotionDetector')
def emotion_output():
    """
    Api route function for when a statement is inputted from the app. 
    Returns a statment showing how much of an emotion is 
    conveyed in the statement in the form of percentages
    """
    response = request.args.get('textToAnalyze')
    emotions = emotion_detection.emotion_detector(response)
    if emotions['dominant_emotion'] is None:
        abort(400)
    statement = f"""For the given statement, the system response is
        'anger': {emotions['anger']}, 
        'disgust':{emotions['disgust']}, 
        'fear': {emotions['fear']}, 
        'joy': {emotions['joy']}, 
        and 
        'sadness': {emotions['sadness']}. 
        The dominant emotion is {emotions['dominant_emotion']}.
        """
    return statement
@app.errorhandler(400)
def bad_request(e):
    """
    Handles errors when there is no input
    """
    return "Invalid text! Please try again!\n. Error:"+e, 400
    