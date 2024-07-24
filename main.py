# Gerekli kütüphaneleri yüklüyoruz
from sklearn.datasets import load_iris  # scikit-learn kütüphanesinden iris veri setini yükler
from sklearn.model_selection import train_test_split  # Veri setini eğitim ve test setlerine ayırmak için kullanılır.Bir fonksiyon
from sklearn.neighbors import KNeighborsClassifier  # Algortimamızın modelini içeren sınıf
import numpy as np  # Sayısal hesaplamalar ve veri işlemleri için kullanılır

# K-En Yakın Komşu sınıflandırıcı modelini oluşturuyoruz
knn = KNeighborsClassifier(n_neighbors=1)  # K=1 olan K-En Yakın Komşu modeli oluşturulur

# Iris veri setini yüklüyoruz
iris_veri_seti = load_iris()  # Iris veri setini yükler

# Veri setini eğitim ve test setlerine ayırıyoruz
ozellikler_egitim, ozellikler_test, hedef_egitim, hedef_test = train_test_split(iris_veri_seti['data'], iris_veri_seti['target'])
# iris veri setini özellikler ve hedef değişken olarak ayırır
# train_test_split() fonksiyonu veriyi rastgele eğitim (%75) ve test (%25) setlerine böler

# Modeli eğitiyoruz
knn.fit(ozellikler_egitim, hedef_egitim)
# K-En Yakın Komşu modelini eğitir
# fit() metodu eğitim veri seti üzerinde modeli öğretir

# Yeni bir veri noktası için tahmin yapıyoruz
yeni_veri_noktasi = [[3.5, 2.1, 3.4, 1.2]]
tahmin = knn.predict(yeni_veri_noktasi)
# Yeni bir veri noktası üzerinde tahmin yapar
# predict() metodu ile yeni_veri_noktasi için tahmin edilen hedef değişken değerini döndürür

# Test seti üzerinde tahminler yapıyoruz
dogruluk = np.mean(knn.predict(ozellikler_test) == hedef_test) * 100
# Test seti üzerinde modelin doğruluğunu hesaplar ve yüzde cinsinden ifade eder
# np.mean() fonksiyonu doğru tahminlerin yüzdesini hesaplar

# Sonucu ekrana yazdırıyoruz
print("Doğruluk:", dogruluk)
# Elde edilen doğruluk değerini ekrana yazdırır
