import cv2
from detector import detect_coins

INPUT = "../images/input/coins.jpg"
OUTPUT = "../images/output/result.jpg"

image = cv2.imread(INPUT)

if image is None:
    print("Image not found.")
    exit()

result, count = detect_coins(image)

cv2.imwrite(OUTPUT, result)

print(f"Detected Coins: {count}")

cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
