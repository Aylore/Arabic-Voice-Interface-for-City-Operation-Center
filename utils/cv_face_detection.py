"""
    Module: face_detection

    This module provides functions for detecting faces in images using the OpenCV library.


    Usage:
    - Import the module: import face_detection
    - Use the functions:
    - face_detection.detect(img)
    - face_detection.detect_batch(images)

    Note:
    - The module requires the OpenCV library to be installed.
    - The haarcascade_frontalface_default.xml file should be available in the OpenCV data directory.


    
"""


import cv2




def detect_batch(images):

    """
       
        - detect_batch(images): Detects faces in multiple images.
        - Parameters:
            - images (List[numpy.ndarray]): A list of input images in BGR format.
        - Returns:
            - List[Optional[Tuple[int, int, int, int]]]: A list of results for each image.
            - Each result is a tuple of four integers representing the (x, y) coordinates of the top-left corner of the detected face
            and the width and height of the bounding box, or None if no face is detected.
    """

    # Load the cascade
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    results = []

    for img in images:
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray, 1.1, minNeighbors=20, minSize=(50, 50)
        )

        if len(faces) > 0:
            # Extract the coordinates of the first detected face
            x, y, w, h = faces[0]
            result = (x, y, x + w, y + h)
        else:
            result = None

        results.append(result)

    return results


