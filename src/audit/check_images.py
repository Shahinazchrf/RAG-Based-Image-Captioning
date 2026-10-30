import json
import os
from PIL import Image

# Define the path to the COCO Train images directory
IMAGE_DIR = "data/raw/images/train2017"

# Define the path to the COCO Train captions annotation file
ANNOTATIONS_FILE = "data/raw/annotations/annotations/captions_train2017.json"


# Load the COCO annotations JSON file
with open(ANNOTATIONS_FILE, "r") as file:
    data = json.load(file)

# Extract the images and captions information
images = data["images"]
annotations = data["annotations"]

# Get the list of image filenames from the directory
image_files = os.listdir(IMAGE_DIR)

# Display the number of images and captions
print("Number of image files:", len(image_files))
print("Number of images:", len(images))
print("Number of captions:", len(annotations))


# Initialize an empty list to store corrupted image filenames
corrupted_images = []

# Iterate through all image files
for filename in image_files:

    # Build the complete path of the current image
    image_path = os.path.join(IMAGE_DIR, filename)

    try:
        # Open the image file
        img = Image.open(image_path)

        # Verify the image file integrity
        img.verify()

    except Exception:
        # Store the filename if the image is corrupted
        corrupted_images.append(filename)


# Display the total number of corrupted images
print("Number of corrupted images:", len(corrupted_images))