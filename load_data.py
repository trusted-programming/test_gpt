import json

f = open('test_pairs.json')
data = json.load(f)
for item in data:
	if len(item["before"].split()) < 50:
		print("----------")
		print(item["before"])
		print(item["after"])