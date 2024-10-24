import os
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from collections import defaultdict
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def extract_features(model, img_path):
    img = keras_image.load_img(img_path, target_size=(224, 224))
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    features = model.predict(img_array)
    return features.flatten()

def process_images(config):
    data_directory = config['data_directory']
    output_directory = config['output_directory']
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    filenames = [os.path.join(data_directory, fname) for fname in os.listdir(data_directory) 
                 if fname.endswith(tuple(config['image_extensions']))]
    
    model = MobileNetV2(weights=config['model']['weights'], include_top=False, input_shape=config['model']['input_shape'])

    feature_list = []
    for fname in filenames:
        features = extract_features(model, fname)
        feature_list.append(features)

    feature_array = np.array(feature_list)

    dbscan = DBSCAN(eps=config['dbscan']['eps'], min_samples=config['dbscan']['min_samples'])
    labels = dbscan.fit_predict(feature_array)

    unique_labels = set(labels)
    print(f'Total individuals detected: {len(unique_labels) - (1 if -1 in unique_labels else 0)}')

    id_to_images = defaultdict(list)

    for idx, label in enumerate(labels):
        if label != -1:
            id_to_images[label].append(filenames[idx])

    # Saving images and plotting can follow

def main():
    config = load_config()
    process_images(config)

if __name__ == "__main__":
    main()
