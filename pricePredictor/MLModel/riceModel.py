import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib


#database
MainDatabase = pd.read_excel(r'RiceData.xlsx')
# base on database we will set iloc
nx = MainDatabase.iloc[:, 1:5].values  #independent variables
ny = MainDatabase.iloc[ : , -2].values #dependent variables


nX_train,nX_test,ny_train,ny_test=train_test_split(nx,ny,test_size=0.3, random_state=3)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(nX_train,ny_train)

model_name = 'RiceMLModel.sav'
joblib.dump(clf,model_name)