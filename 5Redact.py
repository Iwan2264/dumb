import cv2 # type: ignore
import easyocr # type: ignore
import re
import spacy # type: ignore
nlp = spacy.load('en_core_web_sm')

image_path = 'test.png'
image = cv2.imread(image_path)

reader = easyocr.Reader(['en'])
results = reader.readtext(image)

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

for result in results:
    text = result[1]
    top_left = tuple(result[0][0])
    bottom_right = tuple(result[0][2])

    if re.match(email_pattern, text):
        print(f"Redacting email: {text}")
        cv2.rectangle(image, top_left, bottom_right, (0, 0, 0), -1)

    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            print(f"Redacting name: {ent.text}")
            cv2.rectangle(image, top_left, bottom_right, (0, 0, 0), -1)

cv2.imwrite('redacted_test.png', image)
print("Redacted image saved as 'redacted_test.png'")
