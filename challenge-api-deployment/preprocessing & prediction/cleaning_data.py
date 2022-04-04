
#Preprocessing

##### Importing Libraries

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler, OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
import pickle
import joblib

# #### Reading CSV

df = pd.read_csv("https://raw.githubusercontent.com/UmrahJaved/challenge-data-analysis/main/clean_data.csv",index_col=0)
df = df.loc[:, ~df.columns.str.contains('^Unnamed: 0')]

# Finding Null value in dataframe
df.isna().sum()

# Split locality Column
df[['Pin Code', 'Address']] = df['locality'].str.split(' ',n=1, expand=True)

# dropping columns unnecessary columns
df = df.drop(columns=['locality','Pin Code'])

### Fit data

# Splitting dataset to test and train
X_train,X_test,y_train,y_test = train_test_split(df.drop(columns=['price']),
                                                 df['price'],
                                                 test_size=0.2,
                                                random_state=42)


# listing numerical data
num_cols = [col for col in X_train.columns if X_train[col].dtypes!='O']
num_cols

# listing categorical data
cat_cols = [col for col in X_train.columns if X_train[col].dtypes=='O']
cat_cols

# Applying column transform
ct = ColumnTransformer([
    ('step1', RobustScaler(), num_cols),
    ('step2', OneHotEncoder(sparse=False, handle_unknown='ignore'),cat_cols)

], remainder='drop')

# Creating Pipeline
pipeline = Pipeline([
    ('column_transform_step', ct),
    ('model', LinearRegression())
])


# Fit data in train set
pipeline.fit(X_train, y_train)


##### Exporting Pipeline

# export model, columns

pickle.dump(pipeline,open('model/pipe.pkl','wb'))

#Export  column information to a file 
import json

X = df.drop(columns=['price'])
columns = {
    'data_columns' : [col.lower() for col in X.columns]
}
with open("columns.json","w") as f:
    f.write(json.dumps(columns))