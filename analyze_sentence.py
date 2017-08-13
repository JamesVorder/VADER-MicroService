import json
from vaderSentiment import vaderSentiment as vs
import nltk.tokenize

sa = vs.SentimentIntensityAnalyzer()

def lambda_handler(event, context):
    sentence = event["sentence"]
    if sentence == '':
    	raise Exception("Bad request -- Sentence cannot be null.")
    if len(nltk.sent_tokenize(sentence)) > 1:
    	raise Exception("Bad request -- Only one sentence per request.")
    sentiment = sa.polarity_scores(sentence)
    return sentiment