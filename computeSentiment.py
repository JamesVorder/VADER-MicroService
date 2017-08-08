import json
from vaderSentiment import vaderSentiment as vs

sa = vs.SentimentIntensityAnalyzer()

def lambda_handler(event, context):
    sentence = event["sentence"]
    sentiment = sa.polarity_scores(sentence)
    return sentiment