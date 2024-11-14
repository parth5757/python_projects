import cv2
image_path = "D:/python/python_project/opencv/Person_images/modi.jpeg"
image = cv2.imread(image_path)
f = open("image.txt", "a")
f.write(f"array: {image}")
f = open("image.txt", "r")