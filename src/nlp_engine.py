```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

class NLPEngine:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))

    def process_query(self, user_query):
        tokenized = sent_tokenize(user_query)
        for i in tokenized:
            words = nltk.word_tokenize(i)
            words = [word for word in words if word.isalnum()]
            tagged = nltk.pos_tag(words)
            return tagged

    def extract_information(self, tagged_words):
        information = []
        for word in tagged_words:
            if word[1] == 'NN' or word[1] == 'NNS' or word[1] == 'NNP' or word[1] == 'NNPS':
                information.append(word[0])
        return information

    def generate_response(self, information):
        response = "I have scheduled your " + ", ".join(information) + "."
        return response
```