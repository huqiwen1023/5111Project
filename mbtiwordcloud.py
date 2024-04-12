import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

data=pd.read_csv('./static/mbti_1.csv')

i_comments = data[data['type'].str.startswith('I', na=False)]['posts']
e_comments = data[data['type'].str.startswith('E', na=False)]['posts']

custom_stopwords = set(['people', 'think', 'one', 'know', 'thing', 'really', 'feel', 'want'])
stopwords = set(STOPWORDS).union(custom_stopwords)

i_text = ' '.join(i_comments)
wordcloud1 = WordCloud(width=600, 
                      height=400,
                      background_color='white',
                      stopwords=stopwords,
                      colormap='Greens_r'
                      ).generate(i_text)

image1='./static/image/ciyun1.jpg'
wordcloud1.to_file(image1)

e_text = ' '.join(e_comments)
wordcloud2 = WordCloud(width=600, 
                      height=400,
                      background_color='white',
                      stopwords=stopwords,
                      colormap='Oranges_r'
                      ).generate(e_text)

image2='./static/image/ciyun2.jpg'
wordcloud2.to_file(image2)

