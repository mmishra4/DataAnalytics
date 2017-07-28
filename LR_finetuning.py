import os
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import model_selection

os.getcwd()

#read
t_train = pd.read_csv('train.csv')
t_train.info()

#EDA
#dummy for categorical columns
t_train1 = pd.get_dummies(t_train, columns=(['Sex', 'Pclass', 'Embarked']))
t_train1.info()

X_train = t_train1.drop(['PassengerId', 'Survived', 'Age', 'Name', 'Ticket',
                         'Cabin'],1)
X_train.info()
y_train = t_train['Survived']

#model building
lr_estimator = linear_model.LogisticRegression(random_state=2017)
scores = model_selection.cross_val_score(lr_estimator, X_train, y_train, cv=10)
print(scores.mean())

lr_grid = {'C':list(np.arange(0.1,1.0,0.1)), 'penalty':['l1','l2'],
           'max_iter':list(range(100,1000,200))}
lr_grid_estimator = model_selection.GridSearchCV(lr_estimator, lr_grid, cv=10, n_jobs=5)
lr_grid_estimator.fit(X_train, y_train)
lr_grid_estimator.grid_scores_
final_model = lr_grid_estimator.best_estimator_
lr_grid_estimator.best_score_
final_model.coef_
final_model.intercept_