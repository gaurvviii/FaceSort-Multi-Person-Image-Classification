import os
import shutil
import face_recognition

# Step 1: Function to create the output folder
def create_output_folder(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    print(f"Created output directory: {output_dir}")

# Step 2: Function to save images to the person's folder
def save_image_to_folder(image_path, person_id, output_dir):
    person_folder = os.path.join(output_dir, str(person_id))
    if not os.path.exists(person_folder):
        os.makedirs(person_folder)  # Create a new folder for this person
    shutil.copy(image_path, person_folder)  # Copy the image to the person's folder

# Step 3: Function to classify images and organize them
def classify_and_organize_images(input_folder, output_folder):
    known_encodings = []
    person_count = 0
    for image_name in os.listdir(input_folder):
        image_path = os.path.join(input_folder, image_name)

        # Step 4: Load the image and detect faces
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        for face_encoding in face_encodings:
            match_found = False
            if len(known_encodings) > 0:
                matches = face_recognition.compare_faces(known_encodings, face_encoding)
                if True in matches:
                    match_found = True
                    matched_index = matches.index(True)
                    save_image_to_folder(image_path, matched_index, output_folder)
            
            # If no match is found, treat it as a new person
            if not match_found:
                known_encodings.append(face_encoding)
                person_count += 1
                save_image_to_folder(image_path, person_count, output_folder)
    
    print(f"Total unique people detected: {person_count}")

# Main function to set up the workflow
def main():
    input_folder = 'i/Users/dhyan/Downloads/task-1'  # Replace with the path to your input folder containing the images
    output_folder = 'output'  # The folder where organized images will be saved

    # Create the output folder
    create_output_folder(output_folder)

    # Classify and organize images
    classify_and_organize_images(input_folder, output_folder)

if __name__ == "__main__":
    main()
