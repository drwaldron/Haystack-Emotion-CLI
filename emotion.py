import requests
import json
import sys

apiKey = "**API KEY**"

# https://www.haystack.ai/docs?python#analyze
def getEmotion(imageData1):
	outputType = "json"
	requestUri = "https://api.haystack.ai/api/image/analyze?output={}&apikey={}&model=emotion".format(outputType, apiKey)
	apiResponse = requests.post(requestUri, data=imageData1)
	response = json.loads(apiResponse.text)
	emotions = response["people"][0]["emotion"]["emotions"]

	return sorted(emotions, key=emotions.get, reverse=True)[0]

image1 = sys.argv[1]

with open(image1, "rb") as imageData1:
	print(getEmotion(imageData1))