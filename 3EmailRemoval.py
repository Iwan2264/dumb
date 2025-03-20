import re
import spacy # type: ignore
import nltk # type: ignore

nltk.download('punkt')
nlp = spacy.load('en_core_web_sm')
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

with open("nlp.txt", 'r') as file:
    text = file.read()

emails = re.findall(email_pattern, text)
print("Extracted Emails:", emails)

cleaned_text = re.sub(email_pattern, '', text)
print("\nText after removing email IDs:")
print(cleaned_text)

with open("cleaned_nlp.txt", "w") as file:
    file.write(cleaned_text)