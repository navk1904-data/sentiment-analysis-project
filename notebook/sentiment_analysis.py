import pandas as pd
from textblob import TextBlob

# Load data
df = pd.read_csv('../data/reviews.csv')

# Function to calculate sentiment
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis
df['Sentiment'] = df['review'].apply(get_sentiment)

# Display result
print(df)
