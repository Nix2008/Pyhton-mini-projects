import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes, or N for no.\n" % get_close_matches(w, data.keys()) [0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys()) [0]]
        if yn == "N":
            return "Sorry, Word not exist"
        else:
            print("Please enter valid entry.")
        return translate(w)
    else:
        return "Please enter valid number"

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)