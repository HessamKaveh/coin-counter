# Coin Counter using OpenCV

A computer vision project for automatic coin detection and counting using OpenCV.

The system detects circular objects from an input image and counts the number of coins.


## Features

- Image preprocessing
- Grayscale conversion
- Gaussian blur
- Thresholding
- Contour detection
- Circularity-based filtering
- Automatic coin counting


## Pipeline


Input Image

↓

Grayscale

↓

Gaussian Blur

↓

Thresholding

↓

Contour Detection

↓

Circle Filtering

↓

Coin Count



## Installation


Clone repository:

```bash
git clone https://github.com/HessamKaveh/coin-counter.git

```

Create virtual environment

python3 -m venv venv

source venv/bin/activate

Install requirements:

pip install -r requirements.txt

## Usage

Put your image here:

images/input/coins.jpg



## Run

cd src

python main.py

## Author
Hessam Kaveh — Research Fellow, Italian Institute of Technology




