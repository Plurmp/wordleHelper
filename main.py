import json
import re

with open('dictionary.json', 'r', encoding='utf-8') as j_file:
	data = json.load(j_file)

words = set()
for k in data.keys():
	words.add(k)

for s in words:
	if not ('a' in s and 'o' in s and 'r' in s):
		continue
	word_match = re.match(r'^[acefgjklmoqrsvwxyz]{5}$', s)
	if word_match:
		print(s)
