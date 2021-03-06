import json
import re

with open('dictionary.json', 'r', encoding='utf-8') as j_file:
	data = json.load(j_file)

words = set()
for k in data.keys():
	words.add(k)

excluded_letters = []  # excluded letters go here, enclosed by '' and separated by commas
included_letters = []  # included letters go here
for s in words:
	wrong_state = False
	for e in excluded_letters:
		if e in s:
			wrong_state = True
	for i in included_letters:
		if i not in s:
			wrong_state = True
	if wrong_state:
		continue
	# included letters with a specific position go here, e.g. "a" in the third position is "..a.."
	word_match = re.match(r'^.....$', s)
	if word_match:
		print(s)
