import csv
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

# Set the file path and the column containing the text data
file_path = 'wordcloud.csv'
text_column = 'desc'


# Define a function to extract unique words from a column of text data
def get_top_words(file_path, text_column, n=25):
    # Download the stopwords if necessary
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    word_count = {}
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            words = row[text_column].lower().split()
            for word in words:
                if word not in stop_words and word.isalpha():
                    if word not in word_count:
                        word_count[word] = 1
                    else:
                        word_count[word] += 1

    # Sort the dictionary by word count and get the top n words
    top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:n]
    return top_words


# Call the function to get the top words
top_words = get_top_words(file_path, text_column)

# Plot a bar chart of the top words
plt.bar(range(len(top_words)), [x[1] for x in top_words], color='grey')
plt.xticks(range(len(top_words)), [x[0] for x in top_words], rotation=45, size=6)
plt.xlabel('Top Words')
plt.ylabel('Frequency')
plt.title('Bar Chart of Top Words')
plt.show()
