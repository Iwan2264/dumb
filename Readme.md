# AI Lab Readme

## Setup Instructions

To get started with this project, follow the steps below:

### 1. Environment Setup
You need to activate the `iwan` environment or create a new Python virtual environment.

#### Activating `iwan` Environment
```bash
conda activate iwan
```

#### Creating a New Environment
If the `iwan` environment does not exist, create a new one:
```bash
conda create -n iwan python=3.x
conda activate iwan
```

### 2. Install Required Libraries
Install the following Python libraries:
- OpenCV
- NLTK
- EasyOCR
- spaCy
- regex

Run the following command to install them:
```bash
pip install opencv-python nltk easyocr spacy regex
```

### 3. Additional Setup
For `spaCy`, download the required language model:
```bash
python -m spacy download en_core_web_sm
```

## Project Overview
This project utilizes Python libraries such as OpenCV, NLTK, EasyOCR, spaCy, and regex for AI-related tasks. Ensure all dependencies are installed before running the code.

## Notes
- Ensure Python is installed and added to your system's PATH.
- Use the `iwan` environment for consistent dependency management.
