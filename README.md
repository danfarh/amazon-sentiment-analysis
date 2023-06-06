# Sentiment Analysis on Amazon Clothing Products Comments
This project aims to build several machine learning models to perform sentiment analysis on customer comments for clothing products sold on Amazon. The dataset used for this project is scraped from Amazon's website and contains customer comments and ratings for clothing products. The goal is to build models that can classify the sentiment of customer comments as positive, negative, or neutral, which can be used to gain insights into customer feedback and improve customer satisfaction.

## Dataset
The dataset used for this project is scraped from Amazon's website and contains customer comments and ratings for clothing products. The dataset can be downloaded from this website.

## Approach
The project will use several machine learning algorithms to perform sentiment analysis on the Amazon clothing products comments dataset. The following algorithms will be used:

- Support Vector Machine (SVM)
- Logistic Regression
- Naive Bayes
- Convolutional Neural Network (CNN)
- Long Short-Term Memory (LSTM)
- CNN-LSTM
- Bidirectional Encoder Representations from Transformers (BERT)

The following steps will be taken:
- Data Preparation: The dataset will be preprocessed and cleaned to remove any noise and irrelevant information.
- Feature Extraction: The preprocessed text will be transformed into a numerical representation using techniques such as Bag-of-Words, TF-IDF, or pretrained language models.
- Model Training: The machine learning algorithms will be trained on the transformed features and ground-truth sentiment labels.
- Model Evaluation: The models will be evaluated on a held-out test set using metrics such as accuracy, precision, recall, and F1-score. The performance of different models will be compared to identify the best-performing algorithm.

## Requirements
- python
- pandas
- numpy
- tensorflow
- keras
- transformers
- scrapy
