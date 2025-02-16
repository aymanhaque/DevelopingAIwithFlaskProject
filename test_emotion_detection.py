from EmotionDetection import emotion_detection

statements = ['I am glad this happened','I am really mad about this	'
                ,'I feel disgusted just hearing about this	','I am so sad about this',
                'I am really afraid that this will happen	']

for i in statements:
    print(emotion_detection.emotion_detector(i))