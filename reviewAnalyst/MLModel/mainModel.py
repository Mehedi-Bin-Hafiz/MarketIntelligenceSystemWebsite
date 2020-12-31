import pandas as pd
from nltk.corpus import stopwords

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV

from nltk.stem.porter import PorterStemmer
import joblib


df = pd.read_excel('FinalDataSet.xlsx')

porter = PorterStemmer()

def tokenizer(text):
    return text.split()


def tokenizer_porter(text):
     return [porter.stem(word) for word in text.split()]

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(strip_accents=None,
                        lowercase=False,
                        preprocessor=None,
                        tokenizer=tokenizer_porter,
                        use_idf=True,
                        norm='l2',
                        smooth_idf=True)

x = tfidf.fit_transform(df.ManipulatedReviews)
y = df['Classification'].values

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=0)
Logistic = LogisticRegressionCV(cv=5,max_iter=300)
Logistic.fit(X_train,y_train)
model_name = 'ProductModel.sav'
joblib.dump(Logistic,model_name)