
# coding: utf-8

# In[ ]:

import json

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import Imputer
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
import numpy as np


def parse_item(item):
    item = json.loads(item) if isinstance(item, str) else item
    return [item.get("English", np.nan), item.get("Physics", np.nan), item.get("Chemistry", np.nan),
            item.get("ComputerScience", np.nan), item.get("Biology", np.nan),
            item.get("PhysicalEducation", np.nan), item.get("Economics", np.nan), item.get("Accountancy", np.nan),
            item.get("BusinessStudies", np.nan)]


def train_data():
    with open("training.json", "r+") as f:
        m = int(f.readline())
        items = [json.loads(f.readline()) for _ in xrange(m)]
        
        x_train = [parse_item(item) for item in items]
        imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
        x_train = imp.fit_transform(x_train)
        y_train = [item["Mathematics"] for item in items]
        clf = RandomForestClassifier(max_depth=8, n_estimators=50)
        clf.fit(x_train, y_train)
        # print clf.get_params()
        # print "classes: {}, n_classes: {}, n_features: {}".format(clf.classes_, clf.n_classes_, clf.n_features_)
        
        
        return clf

import math
clf = train_data()
m = int(input())
X = [parse_item(raw_input()) for _ in range(m)]
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
X = imp.fit_transform(X)
for y in clf.predict(X):
    print int(y)

