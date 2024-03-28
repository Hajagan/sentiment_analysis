# sentiment_analysis
Overview Welcome to the Amazon Product Sentiment Analysis project! This project focuses on analyzing sentiments expressed in Amazon product reviews using natural language processing techniques. The goal is to gain insights into customer sentiments towards various products available on the platform.

Project Structure The project is structured as follows:

Data Collection:

The dataset used for this analysis is sourced from Kaggle and is named "datafini." The dataset contains Amazon product reviews, and the primary focus is on the sentiment analysis of the review text. Data Pre-processing:

The dataset undergoes thorough pre-processing steps to ensure the accuracy of sentiment analysis. Steps include handling missing values, cleaning text data by removing stopwords and special characters, and converting text to lowercase. Sentiment Analysis:

SpaCy's en_core_web_sm model is employed for sentiment analysis. The sentiment score is calculated for each review, and sentiments are classified as positive, negative, or neutral based on the score. TextBlob Analysis:

Additionally, TextBlob is used to perform similarity and polarity analysis on sample reviews.
