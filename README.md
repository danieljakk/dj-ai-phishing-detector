# DJ AI Phishing Detector

A machine learning web application that detects phishing emails using natural language processing and a Flask-based web interface.

---

## Overview

This project is a simple phishing email detection system built using Python and Scikit-learn. It classifies email text as either phishing or legitimate based on patterns learned from a labeled dataset.

The goal of this project is to demonstrate how machine learning can be applied to basic cybersecurity problems such as email fraud detection.

---

## Features

- Classifies email text as phishing or legitimate
- Returns prediction confidence score
- Provides basic explanation based on detected patterns
- Web interface using Flask
- Trained on a custom dataset of realistic email examples

---

## Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- Joblib

---

## Project Structure

---

## How It Works

1. The model is trained on labeled email text data
2. Input email text is processed using TF-IDF vectorization
3. A classification model predicts whether the email is phishing or legitimate
4. The application displays the prediction, confidence score, and explanation signals

---

## Running the Project Locally

Install dependencies:
pip install -r requirements.txt


Train the model:
python3 train.py

Run the application:
python3 app.py

Open in browser:
http://127.0.0.1:5000


---

## Example Use Cases

- Identifying phishing emails in real time
- Educational demonstration of machine learning classification
- Introductory cybersecurity and NLP project

---

## Future Improvements

- Improve dataset size and diversity
- Use transformer-based models (BERT)
- Deploy as a public web application
- Add file upload support for email files
- Improve explanation system using feature importance

---

## Author

DJ
## Screenshots

### Home Page

![Home Page](images/home.png)

### Phishing Detection

![Phishing Detection](images/phishing.png)

### Legitimate Email Detection

![Legitimate Detection](images/legitimate.png)
