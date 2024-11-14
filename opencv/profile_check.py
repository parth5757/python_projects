# import os
# import cv2
# import face_recognition

# # Directory where existing images are stored
# directory_path = "D:/python/python_project/opencv/Person_Images"

# # Load the uploaded image and check if it's of a person
# def is_person_in_image(image_path):
#     image = cv2.imread(image_path)
#     face_locations = face_recognition.face_locations(image)
#     return len(face_locations) > 0  # Returns True if faces are detected

# # Function to compare uploaded image with each image in directory and get match percentage
# def is_uploaded_image_different(uploaded_image_path):
#     # Load the uploaded image
#     uploaded_image = face_recognition.load_image_file(uploaded_image_path)
#     uploaded_image_encoding = face_recognition.face_encodings(uploaded_image)

#     if not uploaded_image_encoding:
#         print("No faces detected in the uploaded image.")
#         return False  # No face detected in uploaded image

#     uploaded_image_encoding = uploaded_image_encoding[0]  # First face encoding

#     # Loop through each image in the directory and compare
#     for filename in os.listdir(directory_path):
#         file_path = os.path.join(directory_path, filename)
        
#         if not os.path.isfile(file_path):
#             continue
        
#         # Load existing image
#         known_image = face_recognition.load_image_file(file_path)
#         known_image_encodings = face_recognition.face_encodings(known_image)

#         if not known_image_encodings:
#             print(f"No faces detected in {filename}.")
#             continue  # Skip images without detectable faces

#         known_image_encoding = known_image_encodings[0]  # First face encoding

#         # Calculate face distance
#         face_distance = face_recognition.face_distance([known_image_encoding], uploaded_image_encoding)[0]
#         match_percentage = (1 - face_distance) * 100  # Convert distance to a match percentage

#         # If the match percentage is above a certain threshold, consider it a match
#         if match_percentage > 50:  # Set your match threshold (e.g., 70%)
#             print(f"Uploaded image matches with {filename} with a match percentage of {match_percentage:.2f}%.")
#             return False, filename, match_percentage

#     # No matches found, uploaded image is different
#     return True, None, None

# # Example usage
# uploaded_image_path = "D:/python/python_project/opencv/Person_Images/check_image/modi.jpeg"  # Replace with the path to the uploaded image

# # Check if uploaded image is of a person
# if is_person_in_image(uploaded_image_path):
#     # Check if the image is different from those in the directory
#     is_different, matched_file, match_percentage = is_uploaded_image_different(uploaded_image_path)
    
#     if is_different:
#         print("The uploaded image is different from the existing images.")
#     else:
#         print(f"The uploaded image matches an existing image ({matched_file}) with a match percentage of {match_percentage:.2f}%.")
# else:
#     print("The uploaded image does not appear to be of a person.")



import os
import cv2
import face_recognition

# Directory where existing images are stored
directory_path = "D:/python/python_project/opencv/Person_Images"

# Load the uploaded image and check if it's of a single person with an unobstructed face
def is_single_unobstructed_face(image_path):
    image = face_recognition.load_image_file(image_path)
    face_landmarks_list = face_recognition.face_landmarks(image)
    
    if len(face_landmarks_list) != 1:
        print("The image does not contain a single, clear face.")
        return False
    
    face_landmarks = face_landmarks_list[0]
    
    # Check that essential landmarks (both eyes, nose, mouth) are detected
    if not ('left_eye' in face_landmarks and 'right_eye' in face_landmarks and 
            'nose_tip' in face_landmarks and 'top_lip' in face_landmarks and 'bottom_lip' in face_landmarks):
        print("Face landmarks are partially missing, suggesting the face may be obstructed.")
        return False

    return True

# Function to compare uploaded image with each image in directory and get match percentage
def compare_with_existing_images(uploaded_image_path):
    # Load the uploaded image
    uploaded_image = face_recognition.load_image_file(uploaded_image_path)
    uploaded_image_encodings = face_recognition.face_encodings(uploaded_image)

    if not uploaded_image_encodings:
        print("No faces detected in the uploaded image.")
        return False, []  # No face detected in uploaded image

    uploaded_image_encoding = uploaded_image_encodings[0]  # First face encoding

    # Keep track of images with match percentage above 50%
    matches = []

    # Loop through each image in the directory and compare
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if not os.path.isfile(file_path):
            continue
        
        # Load existing image
        known_image = face_recognition.load_image_file(file_path)
        known_image_encodings = face_recognition.face_encodings(known_image)

        if not known_image_encodings:
            print(f"No faces detected in {filename}.")
            continue  # Skip images without detectable faces

        known_image_encoding = known_image_encodings[0]  # First face encoding

        # Calculate face distance
        face_distance = face_recognition.face_distance([known_image_encoding], uploaded_image_encoding)[0]
        match_percentage = (1 - face_distance) * 100  # Convert distance to a match percentage

        # Store results with match percentage above 50%
        if match_percentage > 50:
            matches.append((filename, match_percentage))

    return True if matches else False, matches

# Example usage
uploaded_image_path = "D:/python/python_project/opencv/Person_Images/check_image/modi.jpeg"  # Replace with the path to the uploaded image

# Check if uploaded image is of a single unobstructed face
if is_single_unobstructed_face(uploaded_image_path):
    # Compare with images in the directory
    is_different, matched_images = compare_with_existing_images(uploaded_image_path)
    
    if is_different:
        print("The uploaded image matches existing images with the following details:")
        for filename, match_percentage in matched_images:
            print(f"- {filename} with a match percentage of {match_percentage:.2f}%")
    else:
        print("The uploaded image is different from all existing images.")
else:
    print("The uploaded image does not appear to be of a single, unobstructed person.")
