#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read the dataset
dataset=pd.read_csv("data2.csv",error_bad_lines=False)
x=dataset.iloc[:,:4].values
y=dataset.iloc[:,4].values

#encode the months column
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
x[:, 0] = labelencoder.fit_transform(x[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
x = onehotencoder.fit_transform(x).toarray()

#divide into training and testing set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)


#make your model
from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier()
clf.fit(x_train,y_train)

#predict y
y_pred=clf.predict(x_test)
y_pred1=clf.predict_proba(x_test)[:,1]

#make confusion matrix
from sklearn.metrics import confusion_matrix
cm4=confusion_matrix(y_test, y_pred)

print(cm4)