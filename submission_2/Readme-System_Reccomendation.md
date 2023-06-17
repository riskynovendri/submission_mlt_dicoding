# Project Overview
## Project Overview

Dalam era digital yang kian berkembang, jumlah informasi dan konten yang tersedia secara *online* semakin melimpah. Hal ini menciptakan tantangan bagi pengguna untuk menavigasi dan menemukan konten yang relevan dengan minat dan preferensi mereka. Di tengah kemajuan teknologi dan transformasi digital, sistem rekomendasi telah menjadi penting dalam memberikan pengalaman pengguna yang personal dan membantu mereka menemukan konten yang paling sesuai dengan kebutuhan mereka.

Sistem rekomendasi memiliki peran krusial dalam berbagai *platform online*, seperti *E-commerce*, *Media Streaming*, dan *Sosial Media*. Seperti pada industri *E*, sistem rekomendasi dapat membantu pengguna menemukan produk yang relevan dengan preferensi mereka, meningkatkan kemungkinan pembelian oleh pengguna. Pada *Media Streaming*, sistem rekomendasi dapat membantu pengguna menemukan film, musik, atau buku baru yang sesuai dengan selera mereka, meningkatkan pengalaman hiburan mereka. Selain itu pada *Sosial media* juga sering dijumpai konten yang mungkin disukai oleh pengguna lain sehingga dapat membantu *Content Creator* untuk mendapatkan *Audiens* yang tepat.

Pendekatan tradisional dalam membangun sistem rekomendasi melibatkan metode *Collaborative Filtering* (CF) dan *Content-Based Filtering* (CBF) [2][3][4]. Serta dengan kemajuan dalam bidang *deep learning* dalam sistem rekomendasi telah menghasilkan peningkatan signifikan dalam kualitas dan akurasi rekomendasi. Model *deep learning* dapat mengekstraksi pola yang kompleks dan mampu mengatasi masalah skala besar dalam data rekomendasi [5][6].

Oleh karena itu proyek ini akan membuat System rekomendasi dengan pendekatan *Collaborative Filtering* (CF) dan *Content-Based Filtering* (CBF). Proyek ini juga berdasarkan dari beberapa referensi terkait yang menggunakan metode yang sama [2][3]. Pada penelitian ini juga akan menerapkan *Collaborative filtering* dengan menambahkan teknik deep learning.

# Business Understanding
## Problem Statement
Berdasarkan latar belakang sebelumnya maka ada beberapa yang dapat di pertanyakan yaitu:
* Apa dampak yang dapat diberikan kepada pengguna dalam penerapan Sistem rekomendasi dengan metode *Collaborative Filtering* (CF) dan *Content-Based Filtering* (CBF) ?
* Bagaimana metode *Content Based Filtering dan Collaborative Filtering* dapat memberikan rekomendasi buku terhadap pengguna?
* Apa keunggulan dan kekurangan dari metode *Collaborative Filtering* (CF) dan *Content-Based Filtering* (CBF) dalam sistem rekomendasi?
* Bagaimana hasil dari metode *Collaborative Filtering* (CF) dan *Content-Based Filtering* (CBF)?

## Goals
Berdasarkan problem statement yang dijabarkan sebelumnya maka tujuan dari proyek ini adalah :

* Mampu menjelaskan dampak yang dapat diberikan kepada pengguna dalam penerapan Sistem rekomendasi dengan metode *Collaborative Filtering* (CF) dan *Content-Based Filtering* (CBF) 
* Dapat menerapkan metode *Content Based Filtering dan Collaborative Filtering* dapat memberikan rekomendasi buku terhadap pengguna
* Mebandingkan keunggulan dan kekurangan dari metode *Collaborative Filtering* (CF) dan *Content-Based Filtering* (CBF) dalam sistem rekomendasi
* Analisa hasil dari metode *Collaborative Filtering* (CF) dan *Content-Based Filtering* (CBF)

## Solution Statement
Berdasarkan goal yang dimiliki maka ada beberapa solusi yang dapat diberikan yaitu:
* Menerapkan metode Content Based Filtering dengan menghitung Cosine Simmiliarity
* Menerapkan Collaborative filtering yang di kombinasikan dengan deep learning yaitu Singular Value Decomposition (SVD)
* Melakukan Evaluasi dan membandingkan kinerja pada metode CBF and CF
* Pada CBF akan menghitung *Precision ,Recall dan Accuracy* pada sistem
* Sedangakn pada CF akan dievaluasi menggunakan *Root Mean Squared Error*

# Data Understanding
Adapun dataset yang digunakan adalah [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) dimana data tersebut ada di website kaggle. Pada dataset memiliki 3 File yang terdiri dari Users.csv yang memiliki 278858 baris dan 3 kolom, Rating.csv 1149780 baris dan 3 kolom dan terakhir adalah Books.csv yang memiliki 271360 baris dan 8 kolom.

## Sample dataset
### Users Dataset

Tabel 1 : Dataset Users

| User-ID | Location                         | Age |
|---------|----------------------------------|-----|
| 1       | nyc, new york, usa               | NaN |
| 2       | stockton, california, usa        | 18  |
| 3       | moscow, yukon territory, russia | NaN |
| 4       | porto, v.n.gaia, portugal        | 17  |
| 5       | farnborough, hants, united kingdom | NaN |


Pada dataset users memiliki 3 Kolom yang terdiri dari User-ID, Location dan Age. Dataset ini merupakan dataset tentang profil pengguna yang dapat dilihat pada tabel 1.


### Rating Dataset

Tabel 2 : Rating dataset

| User-ID |     ISBN    | Book-Rating |
|---------|-------------|-------------|
| 276725  | 034545104X  |     0       |
| 276726  | 0155061224  |     5       |
| 276727  | 0446520802  |     0       |
| 276729  | 052165615X  |     3       |
| 276729  | 0521795028  |     6       |

Pada dataset rating memiliki 3 kolom yang terdiri dari User-ID, ISBN dan book rating. Dataset ini berisi tentang buku yang telah dirating oleh pengguna yang dapat dilihat pada tabel 2.

### Books Dataset

Tabel 3 : Books Dataset

|     ISBN    |               Book-Title              |     Book-Author     | Year-Of-Publication |        Publisher       |             Image-URL-S           |             Image-URL-M           |             Image-URL-L           |
|-------------|--------------------------------------|---------------------|---------------------|------------------------|----------------------------------|----------------------------------|----------------------------------|
| 0195153448  |        Classical Mythology            | Mark P. O. Morford  |        2002         | Oxford University Press | http://images.amazon.com/images/P/0195153448.0... | http://images.amazon.com/images/P/0195153448.0... | http://images.amazon.com/images/P/0195153448.0... |
| 0002005018  |           Clara Callan                | Richard Bruce Wright |        2001         | HarperFlamingo Canada   | http://images.amazon.com/images/P/0002005018.0... | http://images.amazon.com/images/P/0002005018.0... | http://images.amazon.com/images/P/0002005018.0... |
| 0060973129  |         Decision in Normandy           |     Carlo D'Este    |        1991         |    HarperPerennial      | http://images.amazon.com/images/P/0060973129.0... | http://images.amazon.com/images/P/0060973129.0... | http://images.amazon.com/images/P/0060973129.0... |
| 0374157065  | Flu: The Story of the Great Influenza Pandemic... |  Gina Bari Kolata   |        1999         |   Farrar Straus Giroux  | http://images.amazon.com/images/P/0374157065.0... | http://images.amazon.com/images/P/0374157065.0... | http://images.amazon.com/images/P/0374157065.0... |
| 0393045218  |        The Mummies of Urumchi          |    E. J. W. Barber  |        1999         | W. W. Norton & Company | http://images.amazon.com/images/P/0393045218.0... | http://images.amazon.com/images/P/0393045218.0... | http://images.amazon.com/images/P/0393045218.0... |

Pada Books dataset memiliki detail mengenai buku yang ada pada data seperti pada tabel 3 yang memiliki 8 kolom yang dapat dilihat pada tabel 3.

## Data Variabel
### Users dataset
* User-ID : Id pengguna
* Location : tempat tinggal pengguna
* Age : Umur pengguna

### Rating Dataset
* Users-ID : id pengguna
* ISBN : merupakan kode unique pengenal pada buku
* book-rating : merupakan rating yang diberikan oleh pengguna pada buku tersebut

### Books Dataset
* ISBN : id pengenal buku
* book-title : judul buku
* book-author : penulis buku
* Year-of-publication : Tanggal publikasi buku
* Publisher : Penerbit buku
* Image-URL-S : link sampul buku versi kecil
* Image-URL-M : link sampul buku versi sedang
* Image-URL-L : link sampul buku versi besar

## Langkah-Langkah Data Understanding
* Melakukan load dataset menggunakan Pandas
* Mengecek Jumlah kolom dan baris pada dataset dengan pandas
* Rename kolom yang diperlukan untuk memudahkan memanggil kolom
* Mengecek Tipe data pada dataset dengan fungsi .info()
* Mengecek nilai unique pada dataset terhadap kolom yang akan digunakan
* Cek distribusi dataset rating dengan fungsi .hist() pada pandas
* Mengambil dataset sample karena keterbatasan resource perangkat google colab

### Hasil EDA dan Visualisasi

Tabel 4 : Table Info Dataset Users

|  Column   | Non-Null Count | Dtype     |
|---------- | -------------- | --------- |
| User-ID   | 278858         | int64     |
| Location  | 278858         | object    |
| Age       | 168096         | float64   |

Pada dataset user, memiliki tipe data integer,object dan float dimana data age memiliki nilai null yang berarti ada user yang tidak memiliki data umur pada dataset. Hal ini dapat disebabkan oleh pengguna tidak melengkapi data profil yang diperlukan. Karena data tidak digunakan maka hal ini dibiarkan saja. Tapi apabila diperlukan maka data null dapat diisi dengan nilai rata-rata atau pun diisi dengan nilai 0.

Tabel 5 : Table Info Dataset Books

|   Column              | Non-Null Count | Dtype   |
|----------------------|----------------|---------|
| ISBN                 | 271360         | object  |
| Book-Title           | 271360         | object  |
| Book-Author          | 271359         | object  |
| Year-Of-Publication  | 271360         | object  |
| Publisher            | 271358         | object  |
| Image-URL-S          | 271360         | object  |
| Image-URL-M          | 271360         | object  |
| Image-URL-L          | 271357         | object  |

Keseluruhan tipe data pada dataset books adalah object dan tidak ada numerik selain itu, pada kolom book-author,publisher dan Image-URL-L memiiki nilai null. 

Tabel 6 : Info dataset Ratings

|   Column      | Non-Null Count | Dtype   |
|--------------|----------------|---------|
| User-ID      | 1149780        | int64   |
| ISBN         | 1149780        | object  |
| Book-Rating  | 1149780        | int64   |


Pada tabel dataset Rating memiliki dua kolom numerik integer dan satu tipe data object dan juga tidak ada indikasi nilai null.

![image](https://user-images.githubusercontent.com/60514291/244953579-0ca03922-311c-4b3b-aebc-a0a12236d7a4.png)

Gambar 1 : Persebaran data book_rating
Pada gambar 1 dapat dilihat bahwa persebaran data sekitar 700.000 data memiliki nilai rating 0. Hal ini dapat di asumsikan bahwa pengguna belum memberikan rating pada buku tersebut. Oleh karena itu data dengan rating 0 akan di drop.

![image](https://user-images.githubusercontent.com/60514291/244954437-70a03f91-9933-463d-be32-bf42cbdb7f34.png)

Gambar 2 : Hasil drop book_rating 0
Setelah rating 0 di drop dapat dilihat bahwa data memiliki persebaran data condong ke kiri yang mendadakan user lebih banyak memberikan rating bagus dari pada rating jelek

Tabel 7 : Statistik Rating

|         | book_rating |
|---------|-------------|
| count   | 431901.000  |
| mean    | 7.628       |
| std     | 1.798       |
| min     | 1.000       |
| 25%     | 7.000       |
| 50%     | 8.000       |
| 75%     | 9.000       |
| max     | 10.000      |

Pada kolom book rating memiliki jumlah 431.901 setelah di clean yang memiliki rata-rata rating 7.6, dengan nilai minimal 1 dan maximal rating 10.

# Data Preparation

## Content Based Filtering
### Data Processing
* Karena berbasis konten maka mengambil dataset books untuk masuk ke tahap processing
* Melakukan perubahan nama kolom menggunakan fungsi rename() pada pandas
* Membersihkan data dari nilai null dengan menggunakan fungsi dropna()
* Membersihkan data dari duplikasi menggunakan fungsi drop_duplicates()
* Memperbaiki kolom book author yang tidak konsisten penamaannya dengan fungsi replace()
* Kemudian mengambil sample 20000 dataset  

### Alasan Penggunaan
* Mengambil dataset books karena CBF membutuhkan atribut konten yang dimiliki oleh dataset books
* Rename kolom untuk memudahkan pemanggilan kolom
* Membersihkan data dari nilai null dan duplicates untuk menghindari bias dan kesalahan analisa pada model
* Menjaga konsistensi data juga untuk mengurangi bias pada model dan juga kesalahan analisa serta meningkatkan efisiensi kinerja model
* Pengambilan sample dataset untuk tahap modelling dikarenakan keterbatasan resource google colab yang tidak mampu memproses data karena data yang terlalu besar dan sering mengalami crash.

## Collaborative FIltering
### Data Processing
* Menggunakan Dataset Rating untuk modelling
* Melakukan Encode User-ID dan ISBN menggunakan fungsi enumerate pada python
* Mapping Hasil encode ke dataframe menggunakan fungsi map()
* Mengambil Sample dataset sebesar 20000
* Membagikan dataset menjadi data training dan data testing menggunakan fungsi train_test_split pada library sklearn dengan perbandingan 80:20

### Alasan Penggunaan
* Menggunakan dataset Rating dikarenakan model akan berdasarkan rating yang diberikan user
* Proses encoding dilakukan agar model nantinya mudah dipahami dan di proses oleh algoritma. serta untuk mengubah data kategorikal menjadi data numerikal dan serta mengurangi dimensi pada data
* Mengambil sample sebesar 20000 karena keterbatasan resource google colab yang tidak mampu mengolah data yang besar dan sering mengalami crash
* Membagi dataset bertujuan agar model dapat di evaluasi setelah melakukan training


# Modeling
## Modeling Content Based Filtering
### Proses yang Dilakukan
* Melakukan perhitungan tf-idf dengan Tfidfvectorizer pada library sklearn
* Perhitungan dilakukan dengan fungsi .fit() agar perhitungan dapat dilakukan
* Kemudian mentransformasikan hasil perhitungan kedalam bentuk skor pada data dengan fungsi fit_transform()
* Fitur yang ditransformasikan adalah pengarang buku
* Setelah itu maka dilakukan perhitungan derajat kesamaan dengan consine_similiarity pada library sklearn
* Hasil dari perhitungan di masukkan kedalam dataframe 
* Membuat fungsi rekomendasi buku untuk melakukan perhitungan dan menampilkan rekomendasi buku berdasarkan judul buku
* Input paramater pada fungsi adalah judul_buku, similiarity_data,index,k dimana judul_buku yang merupakan input judul buku yang akan diperhitungkan, similiarity data merupakan dataframe hasil perhitungan consine_similiarity, index yang merupakan list judul buku dan nama pengarang buku dan k merupakan kelipatan yang akan ditampilkan sebanyak k.
* Untuk proses pada fungsi tersebut, judul_sebagai input akan masuk kedalam pencarian pada df hasil cosine_similiarity dengan menggunakan argpartition dan juga merubah dataframe menjadi numpy dengan rentang -1,-k,-1
* Kemudian mengambil similiarity terbesar dari index yang ada
* Selanjutnya hasil akan disimpan dan drop judul buku yang sebagai input
* Dan terakhir hasil disimpan kedalam dataframe dengan menampilkan top k

 ### Input data untuk Evaluasi
 
 Tabel 9 : Data Input Testing Untuk Evaluasi
 
| user_id | book_rating | book_author   | book_title |
|---------|-------------|---------------|------------|
|   39    |      8      | Dean R. Koontz | Icebound   |


Pada data input user adalah 39 dimana memberikan rating 8 pada judul buku Icebound dengan autho Dean R. Koontz.

### Output Data 

Tabel 10 : Hasil Prediksi System Rekomendasi CBF

| book_title                     | book_author   |
|-------------------------------|---------------|
| The Funhouse                   | Dean R. Koontz |
| Morgengrauen. Sonderausgabe.  | Dean R. Koontz |
| The Mask                       | Dean R. Koontz |
| Mask                          | Dean R. Koontz |
| Unico Superviviente           | Dean R. Koontz |

Pada tabel 10 dapat dilihat bahwa sistem rekomendasi berhasil melakukan prediksi dengan book author yang sama secara keseluruhan

## Modeling Collaborative FIltering
### Proses yang dilakukan
* Setelah data masuk tahap pre-processing kemudian akan menghitung matrix faktorisasi dengan fungsi pivot pada pandas dengan parameter (index='user_id', columns='ISBN', values='book_rating')
* Hasil matrix disimpan kedalam dafarame
* Setelah itu dataframe akan di implementasikan fungsi fillna pada pandas untuk menghindari nilai null dan diganti dengan 0
* Kemudian dataframe di convert kedalam bentuk numpy
* Kemudian dataframe akan di aplikasikan Singular Decomposition Value (SVD) untuk mengurangi dimensi matriks rating pengguna-item yang besar
* SVD bekerja dengan membagi matriks rating pengguna-item menjadi tiga matriks U, Sigma dan Vt
* Dimana U merupakan User, Sigma (s) merupakan rating dan Vt adalah item atau buku
* Penerapan SVD menggunakan fungsi svds pada library scipy
* Kemudian konversikan S kedalam bentuk diagonal matrix untuk mempertahankan informasi yang paling signifikan dalam matriks rating asli.
* Kemudian data matrix akan dihitung dot product nya dengan fungsi dot() pada numpy
* Setelah itu tahap selanjutnya adalah pemodelan ann dengan library tensorflow dan keras
* Dalam pemodelan terdapat beberapa lapisan layer
* Pertama input layers dengan paramater input (shape=(2,), name='input')
* Kedua Layer embedding dengan param input faktorisasi matriks, kemudian Inisialisasi nilai awal untuk embedding. Dalam kasus ini, 'he_normal' digunakan, yang merupakan metode inisialisasi yang biasa digunakan dalam deep learning dan juga Regularisasi yang diterapkan pada embedding. Dalam kasus ini, regularisasi L2 dengan parameter 1e-6 untuk membantu mengurangi kompleksitas model dan menghindari overfitting.
* Ketiga ada layer flatten digunakan untuk mengubah representasi embedding yang memiliki dimensi lebih tinggi menjadi representasi datar yang diperlukan untuk menghubungkan layer Embedding ke layer selanjutnya dalam model
* Keempat adalah Dense layer dengan activation relu dan juga layer dropout dimana param neuron yang digunakan bervariasi dari 32,64,256 dan 128 untuk membuat kompleksitas model sedangkan dropout yang digunakan sebesar 0.3 dan 0.4 untuk mengurangi overfitting
* Dan terakhir adalah output layer dengan activation linear untuk memecahkan masalah regresi
* Kemudian model di compile dengan parameter loss huber yang ada di library tensorflow,optimizer adam pada tensorflow dengan learning rate 0.00001 dan menggunakan matrices RootMeanSquaredError pada library tensorflow
* Selanjutnya juga membuat callback dengan Modelchekcpoint pada library tensorflow bertujuan untuk menyimpan model terbaik dari keseluruhan proses training (epoch) yang telah di jalankan.
* Kemudian model masuk ke tahapan training dengan fungsi .fit() menggunakan epoch 100 dan batch_size 32
### Hasil Compile Model

Tabel 8 : Summary Model

| Layer (type)        | Output Shape   | Param #     |
| ------------------  | -------------- | ---------- |
| input (InputLayer)  | (None, 2)      | 0          |
| embedding (Embedding)| (None, 2, 100) | 2692800    |
| flatten (Flatten)   | (None, 200)    | 0          |
| dense (Dense)       | (None, 64)     | 12864      |
| dense_1 (Dense)     | (None, 32)     | 2080       |
| dropout (Dropout)   | (None, 32)     | 0          |
| dense_2 (Dense)     | (None, 256)    | 8448       |
| dropout_1 (Dropout) | (None, 256)    | 0          |
| dense_3 (Dense)     | (None, 128)    | 32896      |
| dense_4 (Dense)     | (None, 32)     | 4128       |
| dense_5 (Dense)     | (None, 1)      | 33         |

Pada tabel di atas merupakan hasil dari compile model yang telah dibuat dengan total Trainable params: 2,753,249

### Hasil Testing System Rekomendasi Menggunakan CF

Untuk data input adalah user-id 98391 dimana rating tertinggi yang diberikan adalah pada judul dibawah ini 

Tabel 11 : Top 5 High Rating User book

| Book with high ratings from user                                  |
|------------------------------------------------------------------|
| 1. The Madman's Tale (Katzenbach, John) By JOHN KATZENBACH       |
| 2. Bury the Lead (Today Show Book Club #24) By David Rosenfelt    |
| 3. In the Company of Soldiers : A Chronicle of Combat By Rick Atkinson |
| 4. Unleashed (Futuristic Romance) By C. J. Barry                |
| 5. Facade By Patricia A. Rasey                                   |


Tabel diatas merupakan buku dengan rating terbaik yang diberikan oleh user 98391 yang dapat dilihat pada tabel diatas. Sehingga berdasarkan hal tersebut, maka sistem merekomendasikan 10 buku yang mungkin relate oleh user seperti pada tabel 12.

Tabel 12 : Hasil Prediksi Rekomendasi Buku menggunakan CF

| Top 10 book recommendations                                      |
|------------------------------------------------------------------|
| 1. Pay It Forward: A Novel By Catherine Ryan Hyde                |
| 2. Last Honest Woman By Nora Roberts                              |
| 3. Stuart Little By E.B. White                                    |
| 4. King Lear (Shakespeare Made Easy Series) By Alan Durband       |
| 5. The Chronicles of Chrestomanci, Volume 1: Charmed Life / The Lives of Christopher Chant By Diana Wynne Jones |
| 6. Once upon a Dream By Nora Roberts                              |
| 7. Pennsylvania Dutch Cooking : A Mennonite Community Cookbook By MARY E. SHOWALTER |
| 8. Tempting Fate #13 (Language of Love, No. 13) By Nora Roberts   |
| 9. The Woman Who Wouldn't Talk By Susan McDougal                 |
| 10. Who's That Stepping on Plymouth Rock By Jean Fritz           |


## Perbandingan Kelebihan dan Kekurangan pada metode CBF dan CF
### Content Based Filtering 
Keunggulan

* Personalisasi: CBF memperhitungkan preferensi pengguna secara individual berdasarkan konten atau karakteristik item. Hal ini memungkinkan sistem rekomendasi untuk memberikan rekomendasi yang lebih relevan dan sesuai dengan preferensi pengguna.
* Pemahaman Konten: CBF memanfaatkan informasi konten dari item yang direkomendasikan. Hal ini memungkinkan sistem rekomendasi untuk lebih memahami konten dan menghubungkannya dengan preferensi pengguna.
* Ketahanan terhadap "Cold Start": CBF dapat memberikan rekomendasi bahkan ketika terdapat sedikit atau tidak ada informasi pengguna. Dalam kasus "Cold Start", di mana data pengguna terbatas, CBF tetap dapat memberikan rekomendasi berdasarkan informasi konten item.

Kekurangan 

* Keterbatasan pada Informasi Konten: CBF hanya menggunakan informasi konten dari item yang direkomendasikan. Jika informasi konten item tidak mencakup preferensi pengguna secara lengkap, rekomendasi yang dihasilkan mungkin kurang diversifikasi atau kurang akurat.
* Ketergantungan pada Representasi Konten: CBF sangat tergantung pada kualitas representasi konten yang digunakan. Jika representasi konten tidak mewakili dengan baik karakteristik item, kualitas rekomendasi dapat menurun.
* Kurangnya Penemuan Baru: CBF cenderung memberikan rekomendasi yang serupa dengan item yang sudah diketahui oleh pengguna. Ini dapat mengurangi kemungkinan penemuan item baru yang mungkin menarik bagi pengguna.
    
### Collaborative Filtering 

Keunggulan:

* Penemuan Baru: CF dapat memberikan rekomendasi yang baru dan tidak terduga dengan memanfaatkan informasi dari pengguna lain dengan preferensi serupa. Ini memungkinkan pengguna untuk menemukan item yang tidak diketahui sebelumnya.
* Tidak Memerlukan Informasi Konten: CF tidak memerlukan informasi konten dari item yang direkomendasikan. Hal ini memungkinkan CF untuk digunakan pada data yang hanya memiliki informasi preferensi pengguna tanpa informasi detail item.

Kekurangan:

* Data Sparse: CF dapat menghadapi masalah ketika data preferensi pengguna sangat sparse. Jika hanya sedikit data preferensi yang tersedia, akurasi rekomendasi dapat menurun.
* Efek "Cold Start": CF mungkin mengalami kesulitan dalam memberikan rekomendasi saat terdapat pengguna baru atau item baru yang belum memiliki preferensi yang cukup untuk dijadikan acuan.
* Efek "Popularitas": CF cenderung menghasilkan rekomendasi yang cenderung populer berdasarkan perilaku pengguna secara keseluruhan. Hal ini dapat mengabaikan preferensi individu yang mungkin berbeda.

# Evaluation
## Content Based Filtering
* Untuk Metriks yang di gunakan pada content based filtering adalah menggunakan precision, recall dan accuracy yang dapat dihitung dengan menggunakan rumus seperti dibawah ini 

$$ \text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}} $$

$$ \text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}} $$

$$ \text{Accuracy} = \frac{\text{True Positives} + \text{True Negatives}}{\text{True Positives} + \text{True Negatives} + \text{False Positives} + \text{False Negatives}} $$

Dimana 

True Positives (TP) = jumlah prediksi yang benar positif 
False Positives (FP) = jumlah prediksi yang salah positif
False Negatives (FN) = jumlah prediksi yang salah negatif
True Negatives (TN) = jumlah prediksi yang benar negatif

* Recall mengukur sejauh mana model atau sistem mampu mengidentifikasi keseluruhan jumlah data positif yang sebenarnya. Tujuan dari recall adalah untuk meminimalkan jumlah false negatives (data positif yang salah diklasifikasikan sebagai negatif).
* Precision mengukur sejauh mana prediksi positif yang dibuat oleh model atau sistem adalah benar. Tujuan dari precision adalah untuk meminimalkan jumlah false positives (data negatif yang salah diklasifikasikan sebagai positif).
* Accuracy mengukur sejauh mana model atau sistem mampu memberikan prediksi yang benar secara keseluruhan. Tujuan dari accuracy adalah untuk memberikan gambaran umum tentang seberapa baik model atau sistem dalam melakukan klasifikasi secara keseluruhan.
* Hasil pada model adalah berhasil memprediksikan seluruhnya dengan benar dimana book author yang Dean R. Koontz dimana hasilnya sama dengan book author yang ada pada input sebelumnya.

Sehingga apabila kita implementasikan pada rumus maka :

Precision (Presisi):

$$  \text{{Precision}} = \frac{{\text{{5}}}}{{\text{{5}} + \text{{0}}}} = \text{{1}} $$

Recall (Recall):

$$  \text{{Recall}} = \frac{{\text{{5}}}}{{\text{{5}} + \text{{0}}}} = \text{{1}}  $$

Accuracy (Akurasi):

$$  \text{{Accuracy}} = \frac{{\text{{5}} + \text{{0}}}}{{\text{{5}} + \text{{0}} + \text{{0}} + \text{{0}}}} = \text{{1}}  $$

* Sehingga dari hasil evaluasi model mendapatkan hasil dengan akurasi, precision dan recall sebesar 100% yang mana system bekerja sangat baik dalam memberikan rekomendasi buku


## Collaborative Filtering
* Untuk Collaborative Filtering menggunakan evaluasi RMSE atau Root Mean Squared Error dimana metrik yang umum digunakan dalam masalah regresi atau prediksi kontinu
* Hasil RMSE berdasarkan semakin kecil nilai yang di hasilkan maka model memberikan performa yang lebih baik
* Rumus RMSE adalah sebagai Berikut :

RMSE = $$\sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

* Untuk hasil performa learning pada model dapat dilihat pada gambar berikut
![image](https://user-images.githubusercontent.com/60514291/246415966-0bb23c30-f313-42b7-a01d-36a1c0b123b2.png)

Gambar 3 : Hasil Performa Training Model

Pada model dapat dilihat bahwa proses training berjalan dengan cukup bagus dimana RMSE yang dihasilkan semakin kecil dengan indikasi model semakin membaik dalam melakukan perhitungan prediksi. Selain itu, model dapat dikatakan cukup baik dikarenakan jarak antara skor RMSE training dan Testing tidak jauh dengan signifikan dimana hasil akhir root_mean_squared_error 0.4874 dan val_root_mean_squared_error 1.9641 namun terdapat indikasi model memgalami overfitting. Hal ini dapat terjadi karena banyak hal seperti kurangnya data yang dimiliki hingga model yang di buat terlalu kompleks.

# Kesimpulan
* Proyek System rekomendasi buku dapat menggunakan metode Content Based Filtering maupun Collaborative Filtering
* Untuk masing-masing sistem memiliki keunggulan dan kekurangan masing-masing
* Pada Sistem Content Based Filtering mampu memberikan system rekomendasi dengan tingkat evaluasi akurasi, presisi dan recall sebesar 100% dimana sistem memberikan rekomendasi dengan sangat baik
* Sedangkan pada Collaborative Filtering Memberikan hasil nilai evaluasi RMSE sebesar 0.4874 dan Validasi RMSE 1.9641 dimana model mengalami overfitting
* Apabila ingin membuat sistem dengan berdasarkan Content atau atribut pada item, maka CBF dapat menjadi solusi
* Dan jika ingin membuat sistem rekomendasi berdasarkan rating yang diberikan pengguna maka metode CF dapat menjadi solusi
 
Dalam proyek ini terdapat beberapa kekurangan yaitu :

* Dataset yang digunakan tidak dapat digunakan semuanya hal ini dikarenakan keterbatasan resource pada google colab yang tidak mampu proses data yang lebih banyak.
* Untuk sistem CBF saat ini bisa di eksplor dengan based lain seperti User based yang mungkin bisa memberikan preferensi rekomendasi yang lebih baik
* Sedangkan untuk metode CF bisa disarankan untuk mencoba dengan metode Memory Based untuk dapat membandingkan performa sistem yang lebih baik
* Selain itu juga dapat menggabungkan kedua metode dengan *Hybrid Reccomendation System* [2]. Metode ini juga dapat menghasilkan rekomendasi yang lebih baik dikarenakan penggabungan dari dua metode sistem rekomendasi.
* Perlu adanya penelitian lebih lanjut dalam penerapan model *Collaborative Filtering* dengan Teknik *Deep Learning*

Berdasarkan dari project yang telah dikerjakan maka 

#References

* [1] A. Arash, "Book Recommendation Dataset," Kaggle, 2021. [Online]. Available: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset. [Accessed: Month Day, Year].
* [2] Zhang, J., He, X., & Chen, Z. (2019). A survey of collaborative filtering, content-based filtering and hybrid recommendation system. ACM Transactions on Knowledge Discovery from Data (TKDD), 13(6), 1-35.
* [3] Wang, J., Wang, Y., & Zhang, L. (2018). Comparison of content based and collaborative filtering in recommendation systems. IEEE Access, 6, 28327-28336.
* [4] Forsati, R. (2017). A brief analysis of collaborative and content based filtering algorithms used in recommender systems. IOP Conference Series: Materials Science and Engineering, 263(1), 012015.
* [5] He, Xiangnan, Lizi Liao, Hao Sun, and Julian McAuley. "Neural collaborative filtering." In Proceedings of the 26th ACM SIGKDD international conference on knowledge discovery and data mining, pp. 815-824. ACM, 2017.
* [6] Guo, Huifeng, Ruiming Tang, Yunming Ye, Zhenguo Li, and Xiuqiang He. "DeepFM: A factorization-machine based neural network for personalized recommendations." In Proceedings of the 26th AAAI conference on artificial intelligence, pp. 2782-2788. AAAI Press, 2017.
* [7] Guo, Huifeng, Ruiming Tang, Yunming Ye, Zhenguo Li, and Xiuqiang He. "Deep learning for recommender systems." In Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery and data mining, pp. 2074-2082. ACM, 2016.

