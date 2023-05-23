# Prediksi Harga Handphone berdasarkan Spesifikasi - Risky Novendri
## Domain Proyek
Pada era yang serba digital ini, penggunaan ponsel sudah menjadi salah satu kebutuhan utama bagi masyarakat saat ini. Saat ini pun penggunaan ponsel tidak terbatas hanya untuk menelepon atau berkirim sms saja, karena ponsel dapat digunakan sebagai alat pembayaran, m-banking, belanjan daring hingga bermain game sekalipun. Harga ponsel pun bervariarif sesuai dari spesifikasi hingga jenis brand ponsel juga mempengaruhi harga ponsel. 

Namun, pada saat ini pun banyak juga harga ponsel yang tak masuk akal bahkan tak sesuai dengan spesifikasi yang dimiliki. Sehingga banyak masyarakat yang bingung untuk membeli ponsel dengan harga yang sangat sepadan dengan barang yang dimiliki. Hal ini dapat merugikan masyarakat yang ingin membeli ponsel, terutama yang awam akan pengunaan teknologi. Sedangkan di sisi perusahaan, hal ini sangat membantu perusahaan ponsel untuk menetapkan harga jual barang ponsel untuk menghindari kerugian yang tidak diinginkan.

Oleh karena itu, saat ini dibutuhkan suatu aplikasi atau program yang mampu untuk memperhitungkan harga ponsel berdasarkan spesifikasi pada suatu ponsel. Hal ini bertujuan untuk memudahkan masyarakat untuk memutuskan pembelian ponsel yang sesuai keinginan dan sepadan dengan harga yang di dapat.

Penelitian ini sudah perlu dilakukan sebelumnya dimana, referensi yang diberikan mengkaji tentang prediksi harga smartphone menggunakan teknik machine learning [3][4][5][6][7]. Referensi ini memberikan wawasan dan pengetahuan yang relevan dalam pengembangan model prediksi harga smartphone yang efektif dan akurat.Untuk melakukan prediksi harga maka bisa menggunakan penerapan machine learning dengan model regresi. karena regresi digunakan untuk memprediksi suatu nilai berdasarkan nilai input yang dimiliki [1].

## Alasan penting yang mendasari proyek ini:
- Harga ponsel yang terlalu mahal dengan spesifikasi yang rendah dapat membuat orang-orang menyesal telah membeli produk tersebut.
- Sulit bagi masyarakat awam untuk mengetahui spesifikasi ponsel yang sesuai dengan budget dan kebutuhan.
- Proyek ini dapat membantu masyarakat untuk mencegah pembelian ponsel yang tidak sesuai kehendak.
- Membantu konsumen untuk membeli produk yang sesuai dengan harga dan spesifikasinya
- Proyek ini juga dapat membantu pengusaha yang baru mengembangkan produk ponsel untuk menentukan harga jual pasar yang layak serta sesuai dengan spesifikasi yang dimiliki.
- Selain itu juga membantu konsumen memperoleh informasi yang lebih transparan tentang faktor-faktor yang mempengaruhi harga ponsel.
- Konsumen dapat juga membuat pilihan yang lebih informatif dan sesuai dengan kebutuhan dan preferensi
- Proyek ini dapat mendorong persaingan harga yang lebih sehat antara perusahaan-perusahaan ponsel. Dengan pemahaman yang lebih baik tentang faktor-faktor yang mempengaruhi harga, perusahaan dapat menentukan harga yang lebih kompetitif dan mengoptimalkan penawaran
## Referensi Terkait
- [Prediction of Phone Prices Using Machine Learning Techniques](https://link.springer.com/chapter/10.1007/978-981-15-1097-7_65)
- [Comparison of KNN and DNN Classifiers Performance in Predicting Mobile Phone Price Ranges](https://dergipark.org.tr/en/pub/aair/issue/59650/848028)
- [Mobile Phone Specifications and Prices](https://www.kaggle.com/datasets/pratikgarai/mobile-phone-specifications-and-prices)

# Business Understanding

Dari latar belakang yang di jabarkan sebelumnya maka, banyak pihak yang memerlukan aplikasi atau program yang mampu menentukan harga ponsel berdasarkan spesifikasi yang dimiliki suatu ponsel. Hal ini juga berdampak dengan adanya proyek ini mampu membantu banyak pihak dalam penentuan keputusan untuk membeli ponsel.

## Problem Statements
Berdasarkan studi kasus maka:
- Apa hubungan antara fitur-fitur ponsel (seperti RAM, Memori Internal, dll.) dengan harga penjualan ponsel di pasar yang kompetitif?
- Seberapa besar pengaruh fitur ponsel terhadap harga ponsel?
- Bagaimana hasil dari penerapan model machine learning terhadap studi kasus?
- Model algoritma apa yang mampu memberikan tingkat error paling rendah?
- Berapa tingkat skor paling rendah pada algoritma tersebut?

## Goals
Berdasarkan problem statements maka :
- Mengetahui keterkaitan antara fitur pada ponsel terhadap harga ponsel dipasaran.
- Mengetahui besar pengaruh fitur ponsel terhadap harga ponsel.
- Mengetahui hasil dari penerapan model machine learning terhadap memprediksi harga ponsel berdasarkan fitur yang dimiliki oleh ponsel.
- Mampu membuat model yang dapat memprediksi harga ponsel untuk membantu dalam pengambilan keputusan.
- Mengetahui algoritma yang paling cocok untuk studi kasus tersebut.
- Mengetahui skor error paling rendah yang dimiliki model

## Solution Statements
Berdasarkan Goals maka:
- Mencari pengetahuan yang ada pada data dengan menerapkan proses EDA
- Untuk pemilihan model machine learning akan menggunakan algortima SVR yang ada pada [referensi](https://www.researchgate.net/publication/338471736_Prediction_of_Phone_Prices_Using_Machine_Learning_Techniques) dan menggunakan library pycaret untuk menentukan algoritma yang lain.
- evaluasi pembanding model akan menggunakan MSE atau Mean Squared Error

# Data Understanding
Dataset yang digunakan berdasal dari kaggle dengan nama [Mobile Phone Price and Specification](https://www.kaggle.com/datasets/pratikgarai/mobile-phone-specifications-and-prices) yang memiliki jumlah data 1359 baris dan 21 kolom. Dataset merupakan hasil dari scraping dari website [Gadget360](https://www.gadgets360.com/) [8].Dataset berisikan tentang spesifikasi masing-masing handphone dan harga ponsel.

## Sample Data
Ada pun sample data yang bisa dilihat seperti dibawah ini.
| Name                          | Brand  | Model                 | Battery capacity (mAh) | Screen size (inches) | Touchscreen | Resolution x | Resolution y | Processor | RAM (MB) | Internal storage (GB) | Rear camera | Front camera | Operating system | Wi-Fi | Bluetooth | GPS | Number of SIMs | 3G  | 4G/ LTE | Price |
|-------------------------------|--------|-----------------------|------------------------|----------------------|-------------|--------------|--------------|-----------|----------|-----------------------|-------------|--------------|------------------|-------|-----------|-----|----------------|-----|----------|-------|
| OnePlus 7T Pro McLaren Edition | OnePlus| 7T Pro McLaren Edition | 4085                   | 6.67                 | Yes         | 1440         | 3120         | 8         | 12000    | 256.0                 | 48.0         | 16.0         | Android          | Yes   | Yes       | Yes | 2              | Yes | Yes      | 58998 |
| Realme X2 Pro                 | Realme | X2 Pro                | 4000                   | 6.5                  | Yes         | 1080         | 2400         | 8         | 6000     | 64.0                  | 64.0         | 16.0         | Android          | Yes   | Yes       | Yes | 2              | Yes | Yes      | 27999 |
| iPhone 11 Pro Max             | Apple  | iPhone 11 Pro Max     | 3969                   | 6.5                  | Yes         | 1242         | 2688         | 6         | 4000     | 64.0                  | 12.0         | 12.0         | iOS              | Yes   | Yes       | Yes | 2              | Yes | Yes      | 106900 |
| iPhone 11                     | Apple  | iPhone 11             | 3110                   | 6.1                  | Yes         | 828          | 1792         | 6         | 4000     | 64.0                  | 12.0         | 12.0         | iOS              | Yes   | Yes       | Yes | 2              | Yes | Yes      | 62900 |

Tabel 1 : Sample Data
Untuk sample data bisa dilihat seperti pada tabel 1.

## Data Variabel
- Name : berisi nama ponsel
- Brand : merek pada ponsel
- Model : type produk ponsel
- Battery Capacity : kapasitas baterai yang dimiliki ponsel dalam satuan mAh
- screen_size : ukuran layar ponsel
- touchscreen : merupakan layar sentuh atau tidak
- Resolution X : resolusi horizontal layar
- Resolution Y : resolusi layar vertikal
- Processor : jumlah prosessor yang dimiliki pada ponsel
- Ram : Kapasitas memory ram yang dimiliki
- Internal Storage: jumlah memory penyimpanan internal ponsel
- Rear Camera : Resolusi kamera belakang ponsel
- Front Camera : Resolusi kamera depan ponsel
- Operation System : Sistem operasi yang digunakan ponsel
- Wifi : Ponsel memiliki koneksi wi-fi atau tidak
- Bluetooth : Ponsel memiliki bluetooth atau tidak
- GPS : Ponsel memiliki GPS atau tidak
- Numbers of SIMs : Banyak kartu provider (SIM) yang bisa digunakan sekaligus
- 3G : support sinyal 3G atau tidak
- 4g/LTE: support sinyal 4G atau tidak
- Price : harga ponsel

## Langkah-Langkah dalam pendalaman Data Understanding.
- Melakukan tahapan EDA seperti mendeskripsikan variabel, mencari outliers, Univariate hingga Multi-variate analysis.
- Untuk Mendeskripsikan variabel bisa menggunakan library pandas dan fungsi .describe() dan .info()
- Melakukan visualisasi data pada saat melakukan analisa data.
- Untuk menganalisa outliers bisa menggunaka boxplot dengan memanggil fungsi .plot() pada pandas
- Membersihkan data ouliers dengan IQR
- Mengecek data missing value dan membersihkan data missing value dengan membuat simple logic program
- Menggunakan histogram untuk melihat penyebaran data dengan library pandas fungsi .hist()
- Mencari Keterkaitaan antar fitur dengan correlation matrix dengan fungsi pandas dan visualisasi heatmap dengan seaborn

### Hasil Visualisasi tahapan EDA
|   #   |    Column     | Non-Null Count |  Dtype  |
|-------|--------------|----------------|---------|
|   0   |     name     |    1359        | object  |
|   1   |    brand     |    1359        | object  |
|   2   |    model     |    1359        | object  |
|   3   |   battery    |    1359        | int64   |
|   4   | screen_size  |    1359        | float64 |
|   5   | touchscreen  |    1359        | object  |
|   6   | resolution_x |    1359        | int64   |
|   7   | resolution_y |    1359        | int64   |
|   8   |  processor   |    1359        | int64   |
|   9   |     ram      |    1359        | int64   |
|   10  |   internal   |    1359        | float64 |
|   11  | rear_camera  |    1359        | float64 |
|   12  | front_camera |    1359        | float64 |
|   13  |      os      |    1359        | object  |
|   14  |     wifi     |    1359        | object  |
|   15  |  bluetooth   |    1359        | object  |
|   16  |     gps      |    1359        | object  |
|   17  |     sim      |    1359        | int64   |
|   18  |      3g      |    1359        | object  |
|   19  |      4g      |    1359        | object  |
|   20  |    price     |    1359        | int64   |

Tabel 2 : melihat kolom dan tipe data pada dataset
Pada gambar dapat dilihat pada data memiliki kolom 11 kolom numerik atau angka sedangkan sisanya non-numerik atau kategorikal

![box_price](https://user-images.githubusercontent.com/60514291/239754847-afe73a9f-58b1-4634-9792-1555a22688cc.png)
Gambar 1 : Outliers terhadap price
Pada gambar terlihat outliers nya cukup banyak dimana harga nya melebihi batas atas atau Q3 dari keseluruhan data. Sehingga data yang dimiliki perlu di bersihkan dari outliers dengan metode IQR

|    Kolom       | NaN Value Count | Total Rows |
|---------------|----------------|------------|
|    name       |       0        |   1359     |
|    brand      |       0        |   1359     |
|    model      |       0        |   1359     |
|    battery    |       0        |   1359     |
|  screen_size  |       0        |   1359     |
|  touchscreen  |       0        |   1359     |
| resolution_x  |       0        |   1359     |
| resolution_y  |       0        |   1359     |
|  processor    |       0        |   1359     |
|     ram       |       0        |   1359     |
|   internal    |       0        |   1359     |
| rear_camera   |       0        |   1359     |
| front_camera  |       0        |   1359     |
|      os       |       0        |   1359     |
|     wifi      |       0        |   1359     |
|  bluetooth    |       0        |   1359     |
|     gps       |       0        |   1359     |
|     sim       |       0        |   1359     |
|      3g       |       0        |   1359     |
|      4g       |       0        |   1359     |
|    price      |       0        |   1359     |

Tabel 3: pengecekan NaN atau pun bernilai 0 
Pada gambar diatas telah di lakukan pengecekan apakah ada missing value pada data kategorikal dan nilai null/0 pada data numerikal. Dan hasilnya tidak ada data yang missing ataupun null

![top10](https://user-images.githubusercontent.com/60514291/239754897-6b95dec0-3029-47af-a5c7-9042d6cd1699.png)
Gambar 2 : Top 10 brand phone
Pada dataset yang memiliki data ponsel paling banyak adalah Ponsel bermerk Intex dan motorola berada di urutan ke 10.

![hist](https://user-images.githubusercontent.com/60514291/239754920-9debd797-1c19-4df3-9e67-45c0942e55d6.png)
Gambar 3: Persebaran Dataset

Pada gambar diatas ada beberapa kesimpulan yaitu :
*   Pada kolom price, ponsel dengan harga mahal cenderung lebih sedikit daripada ponsel murah 
*   Histogram pada 'price' lebih miring ke kanan atau distribusi miring kanan
*   Pada pada, ponsel paling banyak berada pada harga di bawah 10000

![image](https://user-images.githubusercontent.com/60514291/239755894-c780e92e-ef5f-473c-9713-f505c76788dc.png)
Gambar 4 : Multivariate Analysis OS with Average Price

Pada gambar diatas , OS android memiliki rata-rata harga paling tinggi

![image](https://user-images.githubusercontent.com/60514291/239755998-ea9c9ca4-dbbf-425b-8974-26206fe3b62a.png)
Gambar 5 : Multivariate Analysis gps with Average Price

Harga Handphone rata-rata lebih mahal apabila memiliki GPS.

![image](https://user-images.githubusercontent.com/60514291/239756106-4606ae46-2031-452c-9650-500496067d69.png)
Gambar 6 : Multivariate Analysis 4g with Average Price
Pada gambar diatas, harga rata-rata ponsel lebih mahal apabila memiliki sinyal 4g

![pairplotall](https://user-images.githubusercontent.com/60514291/239754965-9193e343-4d0e-4fd9-8336-68c0e95e5129.png)
Gambar 7 : Korelasi antar price dengan fitur yang lain secara pairplot

Walaupun terlihat acak, namun apabila diperhatikan tiap fitur numerik memiliki korelasi positif terhadap 'price', semakin ke kanan harga pun semakin naik

![corrmat](https://user-images.githubusercontent.com/60514291/239755032-44b5c830-e116-46ae-b587-a76b54ae1565.png)
Gambar 8:Correlation Matrix
Untuk tiap fitur memiliki korelasi positif namun tidak terlalu tinggi, dimana fitur yang paling berpengaruh yaitu ram,internal dan resolusi layar.
Sedangkan pada fitur baterai, memiliki korelasi yang paling kecil diantara fitur yang lainnya

### Result EDA
Sejauh tahap yang dilakukan, seperti menghapus outliers maka tersisa data sebanyak 938 baris data yang sudah bersih dari outliers.

# Data Preparation
## Proses yang dilakukan
-   Menerapkan One Hot Encoding pada data Categorical dengan menggunakan pandas library pada fungsi pd.get_dummies()
-   Menerapkan PCA pada data yang memiliki kesamaan arti dan nilai dengan library sklearn PCA
-   Membagi data set antara training dan testing dengan library sklearn dengan fungsi train_test_split() dengan perbandingan 80:20 sehingga memiliki 750 data train dan 188 data testing
-   Menerapan Standard Scaler pada data numerikal dengan library sklearn dengan fungsi StandarScaler

## Alasan Pengunaan
- One Hot encoding digunakan untuk mengubah variabel kategorikal menjadi representasi numerik yang dapat digunakan dalam model machine learning. serta dapat meningkatan performa model dalam melakukan prediksi karena hanya menggunakan nilai biner. Hal ini sangat berguna karena algoritma machine learning umumnya membutuhkan data numerik sebagai input.
- Penggunaan PCA digunakan untuk mengurangi dimensi dari dataset yang memiliki fitur yang sangat banyak dimana data yang dimiliki mengandung informasi yang redundan atau sama antar banyak fitur yang serupa sehingga cukup dijadikan satu dimensi saja. Hal ini juga bertujuan untuk meningkatkan performa model. Karena terlalu banyak fitur dapat mengakibatkan masalah dalam pemodelan seperti overfitting atau kompleksitas yang berlebihan.Dengan menggunakan PCA, kita dapat mengurangi dimensi fitur-fitur tersebut menjadi sejumlah komponen utama yang paling mengandung informasi.
- Membagi dataset kedalam bentuk training dan testing adalah agar model dapat di evaluasi nantinya. Selain itu, pembagian ini dapat juga untuk mendeteksi apakah model mengalami overfitting jika model memiliki performa yang sangat baik pada data pelatihan tetapi performa yang buruk pada data pengujian.
- Standar Scaler digunakan untuk menormalkan atau menskalakan data numerik dalam skala yang sama. Menggunakan data dengan skala yang berbeda dapat mengganggu performa model yang menggunakan metrik jarak seperti algoritma SVM. Sehingga, model dapat menormalkan data numerik sehingga memiliki rata-rata nol dan standar deviasi satu. Ini membantu dalam menghilangkan perbedaan skala dan memastikan bahwa setiap fitur diperlakukan secara adil dan tidak mendominasi pengaruhnya terhadap hasil model.

# Modeling
Pada proyek ini akan menggunakan model SVR sesuai dengan referensi sebelumnya dan juga menggunakan algoritma Huber Regessor berdasarkan hasil dari running data menggunakan library pycaret.

|   Model   |           Algorithm            |    MAE    |       MSE       |     RMSE    |     R2     |   RMSLE   |   MAPE   | TT (Sec) |
|-----------|-------------------------------|-----------|-----------------|-------------|------------|-----------|----------|----------|
|   huber   |         Huber Regressor        | 4926.8217 | 109476114.4566  |  10220.0214 |   0.3062   |   0.5269  |  0.4096  |  0.4150  |
|    knn    |    K Neighbors Regressor       | 6014.3109 | 131721542.8240  |  11249.8804 |   0.1568   |   0.6684  |  0.6604  |  0.4230  |
|  lightgbm | Light Gradient Boosting Machine| 7512.7058 | 149481917.6927  |  12030.7421 |   0.0284   |   0.8183  |  1.0080  |  0.4430  |
|     et    |    Extra Trees Regressor       | 7575.7432 | 155341761.4113  |  12271.8095 |  -0.0116   |   0.8261  |  1.0060  |  0.5900  |
|    ada    |     AdaBoost Regressor         | 7227.6931 | 156073006.1999  |  12294.8434 |  -0.0144   |   0.7995  |  0.9053  |  0.3480  |
|  xgboost  |   Extreme Gradient Boosting     | 7580.2099 | 155719354.5086  |  12288.7833 |  -0.0148   |   0.8276  |  1.0065  |  0.4730  |
|    omp    |   Orthogonal Matching Pursuit   | 7582.6384 | 155842850.6352  |  12293.4675 |  -0.0156   |   0.8280  |  1.0070  |  0.6200  |
|    llar   |  Lasso Least Angle Regression  | 7582.6383 | 155842848.6985  |  12293.4674 |  -0.0156   |   0.8280  |  1.0070  |  0.5040  |
|    lar    |      Least Angle Regression    | 7582.6384 | 155842850.6352  |  12293.4675 |  -0.0156   |   0.8280  |  1.0070  |  0.7020  |
|    br     |         Bayesian Ridge         | 7582.6385 | 155842851.2002  |  12293.4675 |  -0.0156   |   0.8280  |  1.0070  |  0.7680  |
|    lr     |       Linear Regression        | 7582.6384 | 155842850.6352  |  12293.4675 |  -0.0156   |   0.8280  |  1.0070  |  0.5620  |
|    en     |          Elastic Net           | 7582.6377 | 155842828.1476  |  12293.4666 |  -0.0156   |   0.8280  |  1.0070  |  0.5610  |
|   ridge   |        Ridge Regression        | 7582.6384 | 155842850.5385  |  12293.4675 |  -0.0156   |   0.8280  |  1.0070  |  0.3050  |
|   lasso   |        Lasso Regression        | 7582.6384 | 155842848.8967  |  12293.4674 |  -0.0156   |   0.8280  |  1.0070  |  0.3680  |
|   dummy   |        Dummy Regressor         | 7582.6384 | 155842850.6352  |  12293.4675 |  -0.0156   |   0.8280  |  1.0070  |  0.3110  |
|    rf     |   Random Forest Regressor      | 7614.6345 | 156392402.3966  |  12313.1076 |  -0.0184   |   0.8302  |  1.0131  |  0.3910  |
|    gbr    |  Gradient Boosting Regressor   | 7609.6841 | 156583555.8053  |  12318.9634 |  -0.0191   |   0.8294  |  1.0118  |  0.4490  |
|    dt     |   Decision Tree Regressor     | 7656.8606 | 158612810.0040  |  12391.4475 |  -0.0305   |   0.8327  |  1.0205  |  0.3230  |
|    par    | Passive Aggressive Regressor   | 7442.2487 | 156193958.7692  |  12125.3283 |  -0.0439   |   1.1905  |  0.7329  |  0.3170  |

Tabel 5 : Algorithm Reference

Pada saat menjalankan library yang ada di pycaret, huber regressor memiliki skor mse paling rendah daripada algoritma lain.

## Tahapan yang dilakukan
- Melatih Model dengan data training dengan menggunakan algoritma Huber regressor dan SVR
- Pada tahap training ini akan dilakukan pengujian model dengan parameter default yang ada pada library
- Melakukan pengujian dengan data training
- Kemudian, lanjut pengujian dengan data testing
- Pengukuran menggunakan metriks MSE,MAE,RMSE dan R2 dengan menggunakan lirary sklearn.
- Melihat hasil performa model antara hasil training dan testing
- Kemudian tingkatkan performa model dengan menerapkan grid search atau hyper parameter pada model.
- Untuk hyper param yang digunakan pada Huber Regressor adalah param_grid = { 'epsilon': [1.0, 1.5, 2.0],'alpha': [0.0001, 0.001, 0.01],
    'max_iter': [100, 200, 300]}
- Pada SVR param_grid = {'kernel': ['linear', 'rbf'],'C': [0.1, 1, 10],'epsilon': [0.1, 0.2, 0.3]}
- Dari pengujian hyperparam , mendapatkan param yang terbaik yaitu {'alpha': 0.01, 'epsilon': 2.0, 'max_iter': 200} pada model huber
- Sedangkan SVR {'C': 10, 'epsilon': 0.1, 'kernel': 'linear'}

### Hasil Running Model
|       | Huber_MAE |  SVR_MAE  |    Huber_MSE    |    SVR_MSE     |   Huber_RMSE   |   SVR_RMSE    |   Huber_R2   |   SVR_R2   |
|-------|-----------|-----------|-----------------|----------------|----------------|---------------|--------------|------------|
| train | 1905.190  | 2584.369  | 7774691.441     | 13188739.278   | 2788.313       | 3631.630      | 0.391        | -0.034     |
| test  | 2189.424  | 2907.168  | 11186580.685    | 17854936.225   | 3344.635       | 4225.510      | 0.325        | -0.078     |
Table 6 : Hasil training dan testing tanpa param
Dari tabel diatas dapat dijelaskan bahwa:
* Huber_MAE: Rata-rata absolut dari selisih antara nilai prediksi dan nilai aktual pada data train adalah sekitar 1905.190, sedangkan pada data test sekitar 2189.424. Ini menunjukkan bahwa model memiliki tingkat kesalahan yang sedikit lebih tinggi pada data test dibandingkan dengan data train.

* SVR_MAE: Rata-rata absolut dari selisih antara nilai prediksi dan nilai aktual pada data train adalah sekitar 2584.369, sedangkan pada data test sekitar 2907.168. Hal ini menunjukkan bahwa model memiliki tingkat kesalahan yang sedikit lebih tinggi pada data test dibandingkan dengan data train.

* Huber_MSE: Rata-rata dari kuadrat selisih antara nilai prediksi dan nilai aktual pada data train adalah sekitar 7,774,691.441, sedangkan pada data test sekitar 11,186,580.685. Ini menunjukkan bahwa model memiliki tingkat kesalahan yang sedikit lebih tinggi pada data test dibandingkan dengan data train.

* SVR_MSE: Rata-rata dari kuadrat selisih antara nilai prediksi dan nilai aktual pada data train adalah sekitar 13,188,739.278, sedangkan pada data test sekitar 17,854,936.225. Hal ini menunjukkan bahwa model memiliki tingkat kesalahan yang sedikit lebih tinggi pada data test dibandingkan dengan data train.

* Huber_RMSE: Akar kuadrat dari Huber_MSE pada data train adalah sekitar 2,788.313, sedangkan pada data test sekitar 3,344.635. Ini menunjukkan bahwa prediksi model memiliki tingkat kesalahan yang sedikit lebih tinggi pada data test dibandingkan dengan data train.

* SVR_RMSE: Akar kuadrat dari SVR_MSE pada data train adalah sekitar 3,631.630, sedangkan pada data test sekitar 4,225.510. Hal ini menunjukkan bahwa prediksi model memiliki tingkat kesalahan yang sedikit lebih tinggi pada data test dibandingkan dengan data train.

* Huber_R2: Koefisien determinasi (R-squared) pada data train adalah sekitar 0.391, sedangkan pada data test sekitar 0.325. Ini menunjukkan bahwa model memiliki kemampuan yang lebih baik dalam menjelaskan variasi data pada data train dibandingkan dengan data test.

* SVR_R2: Koefisien determinasi (R-squared) pada data train adalah sekitar -0.034, sedangkan pada data test sekitar -0.078. Hal ini menunjukkan bahwa model memiliki kinerja yang buruk dalam menjelaskan variasi data baik pada data train maupun data test.

Kesimpulannya, terdapat perbedaan kinerja model antara data train dan data test. Model cenderung memiliki tingkat kesalahan yang sedikit lebih tinggi pada data test, menunjukkan adanya overfitting pada data train. Selain itu, koefisien determinasi (R-squared) juga menunjukkan bahwa model memiliki kemampuan yang lebih baik dalam menjelaskan variasi data pada data train dibandingkan dengan data test. Sehingga, perlu adanya penerapan Hyperparam setelah model masuk ke evaluasi

## Kelebihan dan kekurangan masing-masing algoritma
- Dari hasil pengujian, Algoritma Huber lebih unggul daripada SVR terhadap data yang dimiliki.
- Pada Huber memiliki keunggulan yaitu Lebih toleran terhadap outliers dan cenderung memberikan estimasi parameter yang lebih stabil
- Pada SVR memiliki keunggulan yaitu mampu menangani data yang memiliki hubungan non-linear, kemampuan menangani outliers serta memiliki berbagai macam kernel sesuai dengan yang dibutuhkan.
- Namun, Huber memiliki kelemahan yaitu kurang fleksibel menangani data non-linear dan membutuhkan penyetelan param yang tepat untuk menghasilkan model terbaik
- Sedangkan SVR memiliki kelemahan yaitu apabila model semakin kompleks akan berdampak kepada performa processing yang lebih lama dan sangat sensitif terhadap param yang digunakan

# Evaluasi

### MSE
Untuk metode evaluasi menggunakan metriks MSE atau Mean Squared Error terhadap model machine learning yang di kembangkan.Cara kerja metriks ini sendiri cukup simpel yaitu semakin kecil angka yang keluar maka model yang dihasilkan semakin baik. MSE memberikan bobot yang lebih besar pada perbedaan yang besar dan juga menghasilkan nilai non-negatif karena nilai dikuadratkan [2]. MSE dihitung dengan cara mengambil perbedaan antara nilai prediksi (ŷ) dan nilai sebenarnya (y) untuk setiap data poin, mengkuadratkannya, dan kemudian mengambil rata-rata dari seluruh perbedaan kuadrat tersebut.

Untuk rumusnya yaitu : MSE = $$\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

* Dimana n adalah jumlah data poin dalam dataset 
* y adalah nilai sebenarnya dari target atau variabel yang diprediksi 
* ŷ adalah nilai prediksi dari target atau variabel yang diprediksi.

### MAE
MAE merupakan metrik evaluasi yang mengukur rata-rata selisih absolut antara nilai prediksi dan nilai sebenarnya [2]. Dimana, semakin kecil angka maka performa semakin baik. MAE juga memberikan gambaran tentang seberapa besar kesalahan prediksi dalam satuan yang sama dengan variabel target.

Rumus : MAE = $$\frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
### RMSE 
RMSE merupakan akar kuadrat dari MSE dan digunakan untuk mengukur akurasi rata-rata prediksi [2].memberikan gambaran tentang seberapa besar kesalahan prediksi dalam satuan yang sama dengan variabel target.

Rumus : RMSE = $$\sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

### R-Squared (R2)
R-squared (R2) merupakan metrik evaluasi yang mengukur seberapa baik model regresi dapat menjelaskan variasi data [2]. Metriks ini memiliki rentang nilai antara 0 hingga 1, dimana nilai 1 menunjukkan bahwa model dapat menjelaskan seluruh variasi data dengan sempurna.

RUMUS = R2 = $$1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$

|     Index    | Huber_MAE | SVR_MAE |  Huber_MSE  |   SVR_MSE    | Huber_RMSE |  SVR_RMSE   |  Huber_R2   |  SVR_R2   |
|:------------:|:---------:|:-------:|:-----------:|:------------:|:----------:|:-----------:|:-----------:|:---------:|
|    train     | 1905.190  | 2584.369| 7774691.441 | 13188739.278 | 2788.313   | 3631.630    | 0.390       | -0.034    |
|     test     | 2189.424  | 2907.168| 11186580.685| 17854936.225 | 3344.635   | 4225.510    | 0.325       | -0.078    |
| eval_train   | 1916.916  | 1894.411| 7575414.075 | 8072194.776  | 2752.347   | 2841.161    | 0.406       | 0.367     |
| eval_test    | 2232.534  | 2181.098| 11010488.333| 11648441.539 | 3318.206   | 3412.981    | 0.335       | 0.297     |

Tabel 7 : Hasil Evaluasi Model 
Berdasarkan data yang diberikan,dapat diambil kesimpulan bahwa model terbaik adalah model Huber Regression.Hal ini berdasarkan hasil dari setelah model masuk ketahap evaluasi dengan menerapkan hyperparam. Dimana, model menunjukkan nilai skor yang lebih baik secara keseluruhan matriks yang ada. Model huber memiliki tingkat kesalahan yang lebih rendah pada data pelatihan dan evaluasi, serta memiliki kemampuan yang lebih baik dalam menjelaskan variasi dalam data.

## Kesimpulan
Dari proyek ini dapat disimpulkan Bahwa:
- Spesifikasi ponsel memiliki keterkaitan terhadap harga ponsel yang dijual, dimana semakin bagus spesifikasi maka semakin mahal pula harganya.
- Sangat memungkinkan untuk mengimplementasikan model machine learning yang mampu memprediksi harga ponsel berdasarkan spesifikasi yang dimiliki.
- Fitur yang cukup mempengaruhi harga yaitu Memory Internal, RAM, Resolusi layar dan ukuran layar
- Sedangkan Baterai tidak terlalu mempengaruhi harga ponsel
- Huber Memiliki skor MAE 2232.534, MSE 11010488.333 , RMSE 3318.206 dan R2 0.335
- Sedangkan SVR Memiliki skor MAE 2181.098, MSE 11648441.539 , RMSE 3412.981 dan R2 0.297
- Dari hasil pengujian Training dan Testing, maka algoritma yang cocok untuk studi kasus ini adalah Huber Regessor yang memiliki nilai evaluasi yang paling bagus.
- Huber memiliki kemampuan memprediksi kesalahan lebih rendah dan mampu menjelaskan lebih baik variasi dalam data berdasarkan metriks evaluasi.

Dalam proyek ini juga memiliki beberapa kekurangan yaitu :
* Data testing yang kurang banyak dimana hanya memilki 1359 baris data yang setelah masuk processing menjadi 938. Hal ini dapat membuat model belajar dari sedikit data. Dimana semakin banyak data maka model akan semakin baik dalam mempelajari data yang ada.
* Perlu adanya pembanding algoritma yang lain seperti Penggunaan algoritma Random Forest, Lasso regression , AdaBoost Regressor dan masih banyak algoritma regresi lainnya.

### Referensi
[1]. T. Hastie, R. Tibshirani, and J. Friedman, "The Elements of Statistical Learning: Data Mining, Inference, and Prediction," Springer, 2009. [Online]. Available: [https://www.statlearning.com/](https://www.statlearning.com/)

[2]. G. James, D. Witten, T. Hastie, and R. Tibshirani, "An Introduction to Statistical Learning: with Applications in R," Springer, 2013. [Online]. Available: [https://www.statlearning.com/](https://www.statlearning.com/)

[3]. R. Patel and A. Sharma, "Predictive Analysis of Smartphone Prices Using Machine Learning Techniques," in *Proceedings of the 3rd International Conference on Computing Methodologies and Communication*, 2021, pp. 471-479.

[4]. C. T. Chou, Y. H. Ho, W. J. Chen, and C. W. Tsai, "A Machine Learning-Based Framework for Smartphone Price Prediction," *Information Systems Frontiers*, vol. 22, no. 6, pp. 1749-1763, 2020. [Online]. Available: [https://doi.org/10.1007/s10796-020-10068-0](https://doi.org/10.1007/s10796-020-10068-0)

[5]. K. M. Reddy, K. V. Kumar, and K. R. Reddy, "Prediction of Smartphone Prices Using Machine Learning Algorithms," *International Journal of Advanced Science and Technology*, vol. 28, no. 19, pp. 2060-2072, 2019.

[6]. S. Subhiksha, S. Thota, and J. Sangeetha, "Prediction of Phone Prices Using Machine Learning Techniques," in *Data Engineering and Communication Technology*, K. Raju, R. Senkerik, S. Lanka, and V. Rajagopal (eds), Advances in Intelligent Systems and Computing, vol. 1079, Springer, Singapore, 2020. [Online]. Available: [https://doi.org/10.1007/978-981-15-1097-7_65](https://doi.org/10.1007/978-981-15-1097-7_65)
[7]. E. Güvenç, G. Çetin, and H. Koçak, "Comparison of KNN and DNN Classifiers Performance in Predicting Mobile Phone Price Ranges," *Advances in Artificial Intelligence Research*, vol. 1, no. 1, pp. 19-28, Jan. 2021.
[8]. Garai, P. (2021). Mobile Phone Specifications and Prices. Kaggle. [Online]. Available: https://www.kaggle.com/datasets/pratikgarai/mobile-phone-specifications-and-prices. [Accessed: 22-05-2023].


