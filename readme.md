# Image Classification Project

This project classifies images of individuals and organizes them into separate folders based on the detected person. It uses TensorFlow and Keras for feature extraction and DBSCAN for clustering.

## Table of Contents
- [Installation]
- [Usage]
- [Project Structure]
- [Dependencies]
- [College ID]


## Installation

1. **Clone the Repository**:
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>
2. **Setup the Virtual environment** :
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
3.**Install Dependencies**:
pip install tensorflow numpy scikit-learn opencv-python matplotlib



## Usage
Prepare Your Input Data:
Create a folder named data in the project directory.
Place all your input images (JPEG or PNG) inside the data folder.
Run the Shell Script:
./execute.sh
Output:
The script will create an output folder containing subfolders for each detected individual, named by their unique IDs.
The total count of detected individuals will be printed in the terminal.
A summary plot will be generated, showing the detected individuals by their unique IDs.

## Project Structure
├── .venv/               
├── main.py              
├── execute.sh           
└── data/                
    ├── image1.jpg
    ├── image2.png
    └── image3.jpeg

## Dependencies 
Python 3.x
TensorFlow
NumPy
Scikit-learn
OpenCV
Matplotlib

## College ID

21CSU196