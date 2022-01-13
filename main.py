import json
import re

with open('dictionary.json', 'r', encoding='utf-8') as j_file:
	data = json.load(j_file)

words = set()
for k in data.keys():
	words.add(k)

excluded_letters = ['a', 'b']  # excluded letters go here, enclosed by '' and separated by commas
included_letters = ['e', 'g']  # included letters go here
for s in words:
	for e in excluded_letters:
		if e in s:
			continue
	for i in included_letters:
		if i not in s:
			continue
	# included letters with a specific position go here, e.g. "a" in the third position is "..a.."
	word_match = re.match(r'^.e...$', s)
	if word_match:
		print(s)
