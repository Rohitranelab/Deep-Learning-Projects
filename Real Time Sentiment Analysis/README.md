
# Real-Time Sentiment Analysis

A simple Python project that performs real-time sentiment analysis on user-entered text using NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer.

## Overview

This project takes a text review as input from the user and classifies it as **Positive**, **Negative**, or **Neutral** based on VADER's compound sentiment score.

## Features

- Real-time sentiment classification from user input
- Uses VADER, a lexicon and rule-based sentiment analysis tool well-suited for social media text and short reviews
- Simple, lightweight implementation with minimal dependencies

## Requirements

- Python 3.13.5 (or compatible Python 3 version)
- `nltk` library

Install dependencies with:

```bash
pip install nltk
```

## NLTK Data

The following NLTK datasets are required and downloaded automatically the first time the notebook runs:

```python
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
```

## How It Works

1. Import NLTK's `SentimentIntensityAnalyzer` from `nltk.sentiment.vader`.
2. Download required NLTK data (`punkt`, `vader_lexicon`).
3. Initialize the analyzer:
   ```python
   sid = SentimentIntensityAnalyzer()
   ```
4. Prompt the user for a review/text input.
5. Compute polarity scores using `sid.polarity_scores(input_data)`.
6. Classify sentiment based on the **compound** score:

   | Compound Score        | Sentiment |
   |------------------------|-----------|
   | >= 0.05                | Positive  |
   | <= -0.05                | Negative  |
   | Between -0.05 and 0.05 | Neutral   |

## Usage

Run the notebook cells in order, then enter a review when prompted:

```
Enter the review: i am really happy
Positive
```

## Example

```python
input_data = input('Enter the review: ')
score = sid.polarity_scores(input_data)

if score["compound"] >= 0.05:
    print('Positive')
elif score["compound"] <= -0.05:
    print("Negative")
else:
    print('Neutral')
```

## Future Improvements

- Extend to analyze streaming/live data (e.g., social media feeds, chat messages) instead of manual input
- Add a simple UI (web app or dashboard) for real-time visualization
- Support batch processing of multiple reviews from a file or API
- Compare VADER results with other models (e.g., TextBlob, transformer-based models)
