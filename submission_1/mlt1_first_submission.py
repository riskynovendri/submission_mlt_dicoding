# -*- coding: utf-8 -*-
"""MLT1  First Submission

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19BylXWxpeWOuTvHnNsdwQTTjNi5WsfQq
"""

import pandas as pd
import numpy as np

pip install pycaret #Install Pycaret For references using models

import pycaret

# from pycaret.datasets import get_data
# data = get_data('diabetes')

# from pycaret.classification import *
# setup =  setup(data,target='Class variable')

# best = compare_models()

data = pd.read_csv('/content/drive/MyDrive/MLT Submission 1 dataset/phone_price_with_specs.csv')

data.drop(columns='Unnamed: 0',inplace=True)

data

"""Data yang dimiliki ada 1359 baris dan 21 kolom data"""

data.columns

#rename kolom agar memudahkan pemanggilan kolom
cols = ['name', 'brand', 'model', 'battery',
       'screen_size', 'touchscreen', 'resolution_x', 'resolution_y',
       'processor', 'ram', 'internal', 'rear_camera',
       'front_camera', 'os', 'wifi', 'bluetooth', 'gps',
       'sim', '3g', '4g', 'price']
data.columns = cols

data.head(5)

from pycaret.regression import * #Setup Models
setup = setup(data, target = 'price', session_id = 123)

best = compare_models() #Run models for references

"""Melihat seluruh algoritma regresi yang ada dan mencari algoritma yang menghasilkan performa yang bagus sesuai dengan data yang dimiliki. Berdasarkan hasil tersebut maka proyek ini akan menggunakan algoritma Huber regressor, sebagai pembanding akan meggunakan SVM sesuai dengan referensi jurnal sebelumnya.

## EDA
"""

data.info()

data

data.describe()

for col in data.columns: #Hitung missing value setiap kolom
  print("kolom : {} memiliki NaN value sebanyak \
  {} dari {} row".format(col, 
                         str(data[col].isna().sum()), 
                         str(len(data.index))))

for col in data.columns: #Cek yang bernilai 0
  print("kolom : {} memiliki NaN value sebanyak \
  {} dari {} row".format(col, 
                         str((data[col]==0).sum()), 
                         str(len(data.index))))

"""Data tidak ada yang NaN maupun value 0"""

# Commented out IPython magic to ensure Python compatibility.
 import seaborn as sns
 import matplotlib.pyplot as plt 
#  %matplotlib inline

data['price'].plot(kind='box')

data['battery'].plot(kind='box')

data['sim'].plot(kind='box')

"""Data terdapat outliers terutama pada kolom price"""

#Hapus Outliers yang ada menggunakan IQR Method
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR=Q3-Q1
data=data[~((data<(Q1-1.5*IQR))|(data>(Q3+1.5*IQR))).any(axis=1)]

data

data['brand'].value_counts().head(10).plot(kind='bar',title='Top 10 Brands')

"""Pada kolom brand, product brands Intex memiliki jenis ponsel paling banyak"""

data.hist(bins=50, figsize=(20,15))
plt.show()

"""

*   Pada kolom price, ponsel dengan harga mahal cenderung lebih sedikit daripada ponsel murah 
*   Histogram pada price lebih miring ke kanan atau distribusi miring kanan
*   Pada pada, ponsel paling banyak berada pada harga di bawah 10000

"""

#Melihat rata-rata harga terhadap masing-masing kategorikal data
cat_features = data.select_dtypes(include='object').columns.to_list()
    
for col in cat_features:
    sns.catplot(x=col, y="price", kind="bar", dodge=False, height = 4, aspect = 3,  data=data, palette="Set3")
    plt.title("Rata-rata 'price' Relatif terhadap - {}".format(col))

# Mengamati hubungan antar fitur numerik dengan fungsi pairplot()
sns.pairplot(data, diag_kind = 'kde')

"""Walaupun terlihat acak, namun apabila diperhatikan tiap fitur memiliki korelasi positif, semakin ke kanan harga pun semakin naik"""

plt.figure(figsize=(10, 8))
    correlation_matrix = data.corr().round(2)
     
    # Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
    sns.heatmap(data=correlation_matrix, annot=True, cmap='PiYG' )
    plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""Untuk tiap fitur memiliki korelasi yang tidak terlalu tinggi

## Data Preparation
"""

#One Hot Encoding
data_cat =  pd.get_dummies(data[['touchscreen', 'os', 'wifi', 'bluetooth', 'gps',
        '3g', '4g']])

data_cat

#Concenate Dataframe
data = pd.concat([data,data_cat],axis=1)

data.drop(columns=['name', 'brand', 'model', 'touchscreen', 'os', 'wifi', 'bluetooth', 'gps',
        '3g', '4g'],inplace=True)

from sklearn.decomposition import PCA

sns.pairplot(data[['screen_size','resolution_x','resolution_y']], plot_kws={"s": 3});

sns.pairplot(data[['rear_camera','front_camera']], plot_kws={"s": 2});

pca_screen = PCA(n_components=3, random_state=199)
pca_screen.fit(data[['screen_size','resolution_x','resolution_y']])
princ_comp_screen = pca_screen.transform(data[['screen_size','resolution_x','resolution_y']])

pca_cam = PCA(n_components=2, random_state=98)
pca_cam.fit(data[['rear_camera','front_camera']])
princ_comp_cam = pca_cam.transform(data[['rear_camera','front_camera']])

pca_screen.explained_variance_ratio_.round(3)

"""96.5% pada data 'screen_size','resolution_x','resolution_y' ada pada PCA Pertama, Kemudian 3.5% sisanya di PCA 2 sedangkan PCA 3 tidak ada sama sekali


"""

pca_cam.explained_variance_ratio_.round(3)

"""83.7% pada data 'rear_camera','front_camera' ada pada PCA Pertama, Kemudian 16.3% sisanya di PCA 2"""

#PCA for Screen
pca_screen_1 = PCA(n_components=1, random_state=199)
pca_screen_1.fit(data[['screen_size','resolution_x','resolution_y']])
data['screen'] = pca_screen_1.transform(data.loc[:, ('screen_size','resolution_x','resolution_y')]).flatten()
data.drop(['screen_size','resolution_x','resolution_y'], axis=1, inplace=True)

#PCA form camera
pca_cam_1 = PCA(n_components=1, random_state=98)
pca_cam_1.fit(data[['rear_camera','front_camera']])
data['camera'] = pca_cam_1.transform(data.loc[:, ('rear_camera','front_camera')]).flatten()
data.drop(['rear_camera','front_camera'], axis=1, inplace=True)

#Split Dataset
from sklearn.model_selection import train_test_split
    
X = data.drop(['price'],axis =1)
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

print(f'Total # of sample in whole dataset: {len(y)}')
print(f'Total # of sample in train dataset: {len(y_train)}')
print(f'Total # of sample in test dataset: {len(y_test)}')

#Scaling menggunakan standard scaler
from sklearn.preprocessing import StandardScaler
    
num_cols = ['battery','processor', 'ram', 'internal','sim']
scaler = StandardScaler()
scaler.fit(X_train[num_cols])
X_train[num_cols] = scaler.transform(X_train.loc[:, num_cols])
X_train[num_cols].head()

X_train[num_cols].describe().round(1)

"""## Model Development"""

#dataframe untuk menyimpan hasil
result = pd.DataFrame(index=['train_mse', 'test_mse','eval_train','eval_test'], 
                      columns=['Huber', 'SVR'])

from sklearn.linear_model import HuberRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

#Train Model Huber
hr = HuberRegressor()
hr.fit(X_train, y_train)
 
result.loc['train_mse','Huber'] = mean_squared_error(y_pred = hr.predict(X_train), y_true=y_train)

#Train Model SVR
svr = SVR()
svr.fit(X_train, y_train)
 
result.loc['train_mse','SVR'] = mean_squared_error(y_pred = svr.predict(X_train), y_true=y_train)

# Scaling data testing
X_test.loc[:, num_cols] = scaler.transform(X_test[num_cols])

#Prediksi data testing dan simpan hasil ke dataframe
result.loc['test_mse','Huber'] = mean_squared_error(y_pred = hr.predict(X_test), y_true=y_test)
result.loc['test_mse','SVR'] = mean_squared_error(y_pred = svr.predict(X_test), y_true=y_test)

result

"""## Evaluasi Model"""

result.plot(kind='bar')

"""Pada hasil running data testing dan data training pada model Maka: 
* Pada Model Huber memiliki performa yang baik pada data training dan error yang dihasilkan pada saat testing cukup berbeda jauh.
* SVR menghasilkan cukup lumayan walaupun performa training nya tidak terlalu bagus dibandingkan dengan Huber. Tapi, Hasil data testingnya tidak begitu jauh dengan data training
* Performa model dirasa masih dapat ditingkatkan dengan hyperparameter
"""

from sklearn.model_selection import GridSearchCV

#Hyperparams Menggunakan Grid Search pada Huber
hr_eval = HuberRegressor()
param_grid = { #Setup Params
    'epsilon': [1.0, 1.5, 2.0],
    'alpha': [0.0001, 0.001, 0.01],
    'max_iter': [100, 200, 300]
}

grid_search_huber = GridSearchCV(hr_eval, param_grid, scoring='neg_mean_squared_error', cv=5)

#Train Model dengan hyperparam
grid_search_huber.fit(X_train, y_train)

print("Best hyperparameters:", grid_search_huber.best_params_)
print("Best Score:", grid_search_huber.best_score_)

#Data Testing
result.loc['eval_train','Huber'] = mean_squared_error(y_pred = grid_search_huber.predict(X_train), y_true=y_train)
result.loc['eval_test','Huber'] = mean_squared_error(y_pred = grid_search_huber.predict(X_test), y_true=y_test)

#Hyperparams Menggunakan Grid Search pada SVR
svr_eval = SVR()
param_grid_svr = { #Setup Params
    'kernel': ['linear', 'rbf'],
    'C': [0.1, 1, 10],
    'epsilon': [0.1, 0.2, 0.3]
}
#Train models menggunakan hyperparams
grid_search_svr = GridSearchCV(svr_eval, param_grid_svr, scoring='neg_mean_squared_error', cv=5)
grid_search_svr.fit(X_train, y_train)

print("Best hyperparameters:", grid_search_svr.best_params_)
print("Best Score:", grid_search_svr.best_score_)

#Data Testing
result.loc['eval_train','SVR'] = mean_squared_error(y_pred = grid_search_svr.predict(X_train), y_true=y_train)
result.loc['eval_test','SVR'] = mean_squared_error(y_pred = grid_search_svr.predict(X_test), y_true=y_test)

result

result.plot(kind='bar')

"""Dari Hasil Evaluasi dapat disimpulkan bahwa :
* Setelah masuk tahapan evaluasi, performa model jauh lebih baik daripada sebelumnya pada saat data testing terutama pada algoritma Huber Regressor.
* Pada algoritma SVR performa testing juga tetap signifikan namun tetap tidak bisa mengalahkan performa Huber Regressor
"""