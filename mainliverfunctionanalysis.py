# -*- coding: utf-8 -*-
"""MAINliverFunctionAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12S7jDUC4jleXPEFrFUdIUod8GP2pCWm3

**Step - 1:** Gathering Data
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from sklearn import preprocessing

"""**Step - 2:** Data Preprocessing"""

#Read the training & test data
ldata = pd.read_excel('/content/indian_liver_patient.xlsx')

ldata

ldata.shape

ldata.info()

ldata.duplicated()

lvdata = ldata.fillna("0")

#Check for any null values
lvdata.isnull().sum()

sns.countplot(data=lvdata, x = 'Dataset', label='Count')

LD, NLD = lvdata['Dataset'].value_counts()
print('Number of patients diagnosed with liver disease: ',LD)
print('Number of patients not diagnosed with liver disease: ',NLD)

lvdata.head()

lvdata.tail()

lvdata.describe()

lvdata["Gender"].value_counts()

lvdata["Albumin"].value_counts()

# See the min, max, mean values
print('The highest Albumin was of:',lvdata['Albumin'].max())
print('The lowest Albumin was of:',lvdata['Albumin'].min())
print('The average Albumin in the data:',lvdata['Albumin'].mean())

"""**Step - 3:** Data Visualization"""

import matplotlib.pyplot as plt

# Line plot
plt.plot(lvdata['Albumin'])
plt.xlabel("Albumin")
plt.ylabel("Levels")
plt.title("Line Plot")
plt.show()

g = sns.FacetGrid(lvdata, col="Dataset", row="Gender", margin_titles=True)
g.map(plt.hist, "Age", color="red")
plt.subplots_adjust(top=0.9)
g.fig.suptitle('Disease by Gender and Age');

"""**Normalization**"""

lvdata[1:5]

from sklearn import preprocessing
import pandas as pd

d = preprocessing.normalize(lvdata[['Age', 'Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase', 'Alamine_Aminotransferase', 'Aspartate_Aminotransferase', 'Total_Protiens', 'Albumin']], axis=0)
scaled_df = pd.DataFrame(d, columns=['Age', 'Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase', 'Alamine_Aminotransferase', 'Aspartate_Aminotransferase', 'Total_Protiens', 'Albumin'])
scaled_df.head()

from sklearn.model_selection import train_test_split #training and testing data split
from sklearn import metrics #accuracy measure
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, classification_report #for confusion matrix
from sklearn.linear_model import LogisticRegression,LinearRegression #logistic regression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

train, test = train_test_split(lvdata, test_size=0.3, random_state=0, stratify=lvdata['Dataset'])

train_X = train[train.columns[:-1]]
train_Y = train[train.columns[-1]]
test_X = test[test.columns[:-1]]
test_Y = test[test.columns[-1]]

X = lvdata[lvdata.columns[:-1]]
Y = lvdata['Dataset']

len(train_X), len(train_Y), len(test_X), len(test_Y)

# Create a label encoder object
le = LabelEncoder()

# Assuming 'Gender' is the column causing the issue, we transform it
train_X['Gender'] = le.fit_transform(train_X['Gender'])
test_X['Gender'] = le.transform(test_X['Gender'])

# Now you can scale your features
scaler = StandardScaler()
train_X_scaled = scaler.fit_transform(train_X)
test_X_scaled = scaler.transform(test_X)

# Train the model
model = LogisticRegression()
model.fit(train_X_scaled, train_Y.values.ravel())

# Make predictions
prediction3 = model.predict(test_X_scaled)

# Print the accuracy and classification report
print('The accuracy of the Logistic Regression is', metrics.accuracy_score(prediction3, test_Y.values.ravel()))
report = classification_report(test_Y, prediction3)
print("Classification Report:\n", report)

# Calculate confusion matrix
cm = confusion_matrix(test_Y.values.ravel(), prediction3)

# Create a heatmap
plt.figure(figsize=(10,7))
sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.title('Confusion Matrix')
plt.show()