import cv2


def preprocess_image(image):


    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )


    blur = cv2.GaussianBlur(
        gray,
        (7,7),
        0
    )


    _, threshold = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY_INV +
        cv2.THRESH_OTSU
    )


    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (5,5)
    )


    clean = cv2.morphologyEx(
        threshold,
        cv2.MORPH_CLOSE,
        kernel
    )


    return clean
