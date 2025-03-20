import nltk # type: ignore
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize, word_tokenize # type: ignore

with open("nlp.txt", "r") as file:
    text = file.read()

nltk_sentences = sent_tokenize(text)
print("Sentences Tokenized:")
print(nltk_sentences)

nltk_words = word_tokenize(text)
print("\nWords Tokenized:")
print(nltk_words)
