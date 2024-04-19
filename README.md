# Metal Classifier Project

## Introduction

Welcome to the Metal Classifier project! This project serves as a showcase of my skills in GitHub and demonstrates my proficiency in various aspects of data scraping, deep learning, exploratory data analysis (EDA), and model validation.

## Overview

The Metal Classifier project aims to classify metal music samples into different subgenres using deep learning techniques. The project utilizes data scraped from Spotify, including audio samples and album covers, to train a deep learning model. The classification is based on the mel spectrogram of 30-second Spotify samples.

## Project Components

1. **Data Scraping**: 
    - Code to scrape data, including audio samples and album covers, from Spotify.

2. **Deep Learning Model Training**:
    - Utilizes the fastai library to train a deep learning model for classifying the 30-second Spotify samples based on their mel spectrogram.

3. **Exploratory Data Analysis (EDA)**:
    - Notebook containing exploratory data analysis to gain insights into the dataset and understand its characteristics.

4. **DCGAN (Deep Convolutional Generative Adversarial Network)**:
    - Notebook attempting to create a DCGAN to generate album covers. Although not highly successful, it provides valuable insights into the challenges of generating album covers using deep learning techniques.

5. **Validation**:
    - Code for validation purposes, which involves searching for entire songs on YouTube, splitting them into 30-second files, predicting the genre based on the deep learning model for each 30-second segment, and returning the most common genre as the actual genre. 

## Challenges and Future Directions

- **Classification Difficulty**: Metal subgenres are notoriously challenging to classify due to inconsistent labeling and general similarities among subgenres.
- **Improving Results**: Currently exploring methods to enhance classification accuracy, including incorporating tabular data alongside the spectrogram.

## Conclusion

The Metal Classifier project showcases my skills in GitHub, data scraping, deep learning, exploratory data analysis, and model validation. Despite the challenges posed by the classification of metal subgenres, the project reflects my commitment to tackling complex problems and continuously improving the quality of the results.

Feel free to explore the project and provide any feedback or suggestions for improvement. Thank you for your interest!
