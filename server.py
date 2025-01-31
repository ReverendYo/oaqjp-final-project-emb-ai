''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_detection():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detection()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response=emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    #Displaying in f-string for return statement for screenshot
    return (
        f"For the given statement, the system response is:"
        f"Anger: {response['anger']}, Disgust: {response['disgust']},"
        f"Fear: {response['fear']}, Joy: {response['joy']},"
        f"Sadness: {response['sadness']}, Dominant Emotion: {response['dominant_emotion']}"
    ), 200

@app.route('/')
def index():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
