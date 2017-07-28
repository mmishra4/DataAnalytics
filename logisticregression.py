import os
import pandas as pd
from sklearn import linear_model
from sklearn import model_selection

os.getcwd()
os.chdir('D:\\MM\Py Prac')
#read
titanic_train = pd.read_csv('train.csv')
titanic_train.info()

#EDA
titanic_train1 = pd.get_dummies(titanic_train, 
                                columns=['Pclass', 'Sex', 'Embarked'])
titanic_train1.info()
titanic_train1.head(6)
X_train = titanic_train1.drop(['PassengerId', 'Survived', 'Name', 'Ticket',
                               'Cabin', 'Age'],1)
X_train.info()
y_train = titanic_train['Survived']

lr_estimator = linear_model.LogisticRegression(random_state=2017)
scores = model_selection.cross_val_score(lr_estimator, X_train, y_train, cv=10)
print(scores.mean())
lr_estimator.fit(X_train, y_train)
lr_estimator.coef_
lr_estimator.intercept_