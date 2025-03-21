import cv2 # type: ignore
import easyocr # type: ignore
import re

image_path = 'test.png'
image = cv2.imread(image_path)

reader = easyocr.Reader(['en'])
results = reader.readtext(image)

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

for result in results:
    text = result[1]
    if re.match(email_pattern, text):
        print(f"Found email: {text}")
        
        top_left = tuple(result[0][0])
        bottom_right = tuple(result[0][2])       
        x1, y1 = top_left
        x2, y2 = bottom_right
        roi = image[y1:y2, x1:x2]

        blurred = cv2.GaussianBlur(roi, (15, 15), 0)
        image[y1:y2, x1:x2] = blurred

cv2.imwrite('blurred_test.png', image)
print("Blurred image saved as 'blurred_test.png'")