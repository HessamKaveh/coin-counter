import cv2
import numpy as np

from utils import preprocess_image


def detect_coins(image):

    processed = preprocess_image(image)


    contours, _ = cv2.findContours(
        processed,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )


    output = image.copy()

    count = 0


    for contour in contours:

        area = cv2.contourArea(contour)


        if area < 1000:
            continue


        perimeter = cv2.arcLength(
            contour,
            True
        )


        circularity = 0

        if perimeter != 0:

            circularity = (
                4 * np.pi * area
            ) / (
                perimeter * perimeter
            )


        if circularity > 0.5:

            count += 1


            (x, y), radius = cv2.minEnclosingCircle(
                contour
            )


            center = (
                int(x),
                int(y)
            )


            radius = int(radius)


            cv2.circle(
                output,
                center,
                radius,
                (0,255,0),
                3
            )


            cv2.putText(
                output,
                f"Coin {count}",
                (
                    center[0]-30,
                    center[1]
                ),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,0,255),
                2
            )


    return output, count
