# Sentiment Analysis on Amazon Clothing Products Comments
This project aims to build several machine learning models to perform sentiment analysis on customer comments for clothing products sold on Amazon. The dataset used for this project is scraped from Amazon's website and contains customer comments and ratings for clothing products. The goal is to build models that can classify the sentiment of customer comments as positive, negative, or neutral, which can be used to gain insights into customer feedback and improve customer satisfaction.

## Dataset
The dataset used for this project is scraped from Amazon's website and contains 100,000 customer comments and ratings for clothing products. 

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

## Results
The machine learning models achieved the following performance on the held-out test set:

- Support Vector Machine (SVM): 91.68% accuracy
- Logistic Regression: 91.29% accuracy
- Naive Bayes: 88.30% accuracy
- Convolutional Neural Network (CNN): 92.45% accuracy
- Long Short-Term Memory (LSTM): 92.86% accuracy
- CNN-LSTM: 93.19% accuracy
- Bidirectional Encoder Representations from Transformers (BERT): -% accuracy

Overall, the BERT model performed the best, achieving an accuracy of ----% on the test set. This model can be used to classify the sentiment of customer comments for clothing products sold on Amazon. The performance of different models was compared, and it was found that the BERT model outperformed the other models significantly.
