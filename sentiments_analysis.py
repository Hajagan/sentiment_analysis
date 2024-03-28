# Import necessary libraries
import pandas as pd
import spacy

# Function to perform sentiment analysis using spaCy
def analyze_sentiment(text):
    # Apply spaCy's language processing pipeline to the text
    doc = nlp(text)
    
    # Calculate the overall sentiment score
    sentiment_score = doc.sentiment.polarity
    
    # Classify sentiment as positive, negative, or neutral based on the score
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

# Function to perform data cleaning and sentiment analysis using spaCy
def clean_and_analyze_sentiment(text):
    # Check for NaN values in the review text
    if pd.isna(text):
        return None

    # Apply string manipulations: strip(), lower()
    cleaned_text = text.strip().lower()

    # Tokenize the cleaned text
    doc = nlp(cleaned_text)

    # Remove stopwords and non-alphabetic tokens
    tokens = [token.text for token in doc if token.text.isalpha() and token.text not in STOP_WORDS]

    # If there are no valid tokens, return None
    if not tokens:
        return None

    # Calculate the overall sentiment score
    sentiment_score = doc.sentiment.polarity

    # Classify sentiment as positive, negative, or neutral based on the score
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

# Function to predict sentiment for a given product review using spaCy
def predict_sentiment(review):
    # Load spaCy's English model
    nlp = spacy.load("en_core_web_sm")
    
    # Apply spaCy's language processing pipeline to the review text
    doc = nlp(review)
    
    # Calculate the overall sentiment score
    sentiment_score = doc.sentiment.polarity
    
    # Classify sentiment as positive, negative, or neutral based on the score
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Load the Amazon product reviews dataset (replace 'your_dataset.csv' with the actual file name)
dataset_path = 'your_dataset.csv'
df = pd.read_csv(dataset_path)

# Remove missing values from the "review_text" column
clean_data = df.dropna(subset=['review_text'])

# Display the cleaned data
print(clean_data[['review_text']])

# Add a new column 'Sentiment' to store the sentiment analysis result
clean_data['Sentiment'] = clean_data['review_text'].apply(clean_and_analyze_sentiment)

# Drop rows where sentiment is None after cleaning
clean_data = clean_data.dropna(subset=['Sentiment'])

# Display the cleaned dataset with the added 'Sentiment' column
print(clean_data[['review_text', 'Sentiment']])

# Save the cleaned dataset with sentiment analysis results
clean_data.to_csv('cleaned_dataset_with_sentiment.csv', index=False)

# Sample product reviews for testing the sentiment analysis function
sample_reviews = [
    "This product is amazing! I love it.",
    "The quality of this product is terrible. I regret buying it.",
    "It's an okay product, nothing special.",
    "Fast shipping and great customer service. Highly recommended!",
    "Worst purchase ever. The product broke after a few days of use.",
    "Absolutely loved it, will be buying again.",
    "Did not see any changes.",
]

# Test the sentiment analysis function on each review
for review in sample_reviews:
    predicted_sentiment = predict_sentiment(review)
    print(f"Review: {review}")
    print(f"Predicted Sentiment: {predicted_sentiment}")
    print("="*40)
