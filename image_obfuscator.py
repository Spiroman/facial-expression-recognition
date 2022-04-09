from importlib.resources import path
import face_recognition
from PIL import Image
import os
import sys

def get_initial_bounds(width, height):
    # Bounding boxe coordinates
    min_x = width
    max_x = 0
    min_y = height
    max_y = 0

    return min_x, max_x, min_y, max_y

def determine_bounds(min_x, max_x, min_y, max_y, object):
    for x, y in object:
        if min_x > x:
            min_x = x
        if max_x < x:
            max_x = x
        if min_y > y:
            min_y = y
        if max_y < y:
            max_y = y

    return min_x, max_x, min_y, max_y


def pad_bounding(min_x, max_x, min_y, max_y, padding=3):
    min_x -= padding
    max_x += padding
    min_y -= padding
    max_y += padding
    return min_x, max_x, min_y, max_y

# Recolores given range of pixel with a certain color. Defaults to black
def obfuscate_image(min_x, max_x, min_y, max_y, image, color=(0,0,0)):
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            image.putpixel((x, y), color)
    return image

def get_landmarks(image):
    image = face_recognition.load_image_file(image)
    face_landmarks_list = face_recognition.face_landmarks(image)
    left_eye = face_landmarks_list[0]['left_eye']
    right_eye = face_landmarks_list[0]['right_eye']
    top_lip = face_landmarks_list[0]['top_lip']
    bottom_lip = face_landmarks_list[0]['bottom_lip']
    return left_eye, right_eye, top_lip, bottom_lip

def create_obfuscated_images(image_name, landmarks):
    left_eye, right_eye, top_lip, bottom_lip = get_landmarks(image_name)    
    for landmark in landmarks:
        image = Image.open(image_name)
        image = image.convert("RGB")
        # Image sizes are the same in both cases so we'll arbitrarily choose the eyes...
        width, height = image.size
        min_x, max_x, min_y, max_y = get_initial_bounds(width, height)

        # Determine bounding box of Landmark
        if landmark == "eyes":
            min_x, max_x, min_y, max_y = determine_bounds(min_x, max_x, min_y, max_y, left_eye)
            min_x, max_x, min_y, max_y = determine_bounds(min_x, max_x, min_y, max_y, right_eye)
        elif landmark == "mouth":
            min_x, max_x, min_y, max_y = determine_bounds(min_x, max_x, min_y, max_y, top_lip)
            min_x, max_x, min_y, max_y = determine_bounds(min_x, max_x, min_y, max_y, bottom_lip)
        else:
            print("Error occured in landmark selection")
            exit(1)


        # Add padding
        min_x, max_x, min_y, max_y = pad_bounding(min_x, max_x, min_y, max_y, padding=3)

        # Obfuscate the image
        obfuscated_image = obfuscate_image(min_x, max_x, min_y, max_y, image)

        # Determine name
        name = image_name[image_name.rindex("/", 0, len(image_name))+1:]
        name = f"{landmark}.{name}.png"
        name = name.replace(".jpg", "")        

        # Save the image
        # obfuscated_image.save(f"both/{name}")

# directory = sys.argv[1]
directory = "../jaffejpeg"
landmarks = ("eyes", "mouth")
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.jpg'):
            image = create_obfuscated_images(f"{directory}/{file}", landmarks)
