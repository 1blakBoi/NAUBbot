import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class UniversityChatbot:
    def __init__(self, path='chatbot/dataset/chatbot2.csv'):
        
        self.data = pd.read_csv(path)
        self.questions = self.data['question']
        self.answers = self.data['answer']

        self.vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        self.tfidf_matrix = self.vectorizer.fit_transform(self.questions)


    def get_response(self, user_input):

        user_vector = self.vectorizer.transform([user_input])
        similarity = cosine_similarity(user_vector, self.tfidf_matrix)
        best_match = np.argmax(similarity)

        return self.answers.iloc[best_match]