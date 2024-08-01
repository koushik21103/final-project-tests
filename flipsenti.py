import nltk
nltk.download('vader_lexicon')

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load the cleaned CSV file
df = pd.read_csv('cleanflip.csv')

# Initialize the VADER sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

# Define a function to get sentiment scores
def get_sentiment(text):
    if isinstance(text, str):
        sentiment_dict = sid.polarity_scores(text)
        return sentiment_dict
    return {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}

# Apply the sentiment analysis function to the 'Comment' column
df['Sentiment'] = df['Comment'].apply(lambda x: sid.polarity_scores(x))

# Extract sentiment scores into separate columns
df = pd.concat([df.drop(['Sentiment'], axis=1), df['Sentiment'].apply(pd.Series)], axis=1)

# Save the results to a new CSV file
df.to_csv('sentiment_ratings_comments.csv', index=False)

print("Sentiment analysis completed and saved as 'sentiment_ratings_comments.csv'")



# Load the CSV file
data = pd.read_csv('sentiment_ratings_comments.csv')

# Display the first few rows of the dataframe
data.head()

# Calculate the average of the compound sentiment scores
average_compound_sentiment = data['compound'].mean()
print(average_compound_sentiment)
