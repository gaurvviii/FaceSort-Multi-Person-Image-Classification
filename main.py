import os
import cv2
import face_recognition
import shutil
import matplotlib.pyplot as plt

# Create output folder
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Helper function to save images to respective folders
def save_image(image_path, person_id, output_dir):
    person_dir = os.path.join(output_dir, str(person_id))
    if not os.path.exists(person_dir):
        os.makedirs(person_dir)
    shutil.copy(image_path, person_dir)

# Function to process images and classify by person
def classify_images(input_folder):
    known_encodings = []
    person_id = 0
    person_map = {}
    
    for image_name in os.listdir(input_folder):
        image_path = os.path.join(input_folder, image_name)
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        
        for face_encoding in face_encodings:
            match = None
            if len(known_encodings) > 0:
                matches = face_recognition.compare_faces(known_encodings, face_encoding)
                if True in matches:
                    match = matches.index(True)
            
            if match is not None:
                save_image(image_path, match, output_dir)
            else:
                known_encodings.append(face_encoding)
                person_id += 1
                save_image(image_path, person_id, output_dir)
                person_map[person_id] = image_name
    
    print(f"Total people detected: {person_id}")
    return person_map

# Plot results
def plot_results(person_map):
    plt.bar(person_map.keys(), [1] * len(person_map))
    plt.xlabel("Person ID")
    plt.ylabel("Count")
    plt.title("Detected Individuals")
    plt.show()

if __name__ == "__main__":
    input_folder = 'task-1'  
    person_map = classify_images(input_folder)
    plot_results(person_map)
