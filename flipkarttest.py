import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk


# Ensure the VADER lexicon is downloaded
#nltk.download('vader_lexicon')

# User-Agent and Accept-Language headers
headers = {
    'User-Agent': 'Your User Agent',  # Replace with your actual user agent
    'Accept-Language': 'en-us,en;q=0.5'
}

ratings = []
comments = []

# Loop through multiple pages (1 to 44 in this case)
for i in range(1, 15):
    # Construct the URL for the current page
    url =f"https://www.flipkart.com/cmf-nothing-phone-1-black-128-gb/product-reviews/itmeef68c7ce70bf?pid=MOBHYBQTSE9EKVBT&lid=LSTMOBHYBQTSE9EKVBT5UGTRK&marketplace=FLIPKART&page={i}"

    # Send a GET request to the page
    page = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract ratings
    rat = soup.find_all('div', class_='XQDdHH Ga3i8K')
    for r in rat:
        rating = r.get_text()
        if rating:
            ratings.append(rating)
        else:
            ratings.append('0')  # Replace null ratings with 0

    # Extract comments
    cmt = soup.find_all('div', class_='ZmyHeo')
    for c in cmt:
        comment_text = c.div.div.get_text(strip=True)
        comments.append(comment_text)

    print(f"Scraped page {i}")

# Ensure all lists have the same length
min_length = min(len(ratings), len(comments))
ratings = ratings[:min_length]
comments = comments[:min_length]

# Create a DataFrame from the collected data
data = {
    'Rating': ratings,
    'Comment': comments
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('flip.csv', index=False)

# Define a function to clean special characters and emojis
def clean_text(text):
    if isinstance(text, str):
        # Use regular expression to remove special characters and emojis
        cleaned_text = re.sub(r'[^A-Za-z0-9\s,.]', '', text)
        return cleaned_text
    return text

# Load the CSV file
df = pd.read_csv('flip.csv')

# Apply the cleaning function to the 'Comment' column
df['Comment'] = df['Comment'].apply(clean_text)

# Save the cleaned data to a new CSV file
df.to_csv('cleanflip.csv', index=False)

print("CSV file cleaned and saved as 'cleanflip.csv'")
