import spacy # type: ignore
nlp = spacy.load("en_core_web_sm")

with open("nlp.txt", "r") as file:
    text = file.read()

doc = nlp(text)

print("Original Text: ", text)
print("PoS Tagging Result:")
for token in doc:
	print(f"{token.text}: {token.pos_}")
