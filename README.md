# K-En Yakın Komşu (k-NN) Sınıflandırıcı Kullanımı

Bu proje, K-En Yakın Komşu (k-NN) algoritmasını kullanarak Iris veri seti üzerinde sınıflandırma yapmayı göstermektedir.

## Yapay Zeka ve Makine Öğrenimi

### Yapay Zeka (AI)

Yapay Zeka, bilgisayar sistemlerine insan benzeri düşünme yetisi kazandırmayı amaçlayan bir bilim dalıdır. Yapay Zeka, çeşitli algoritmalar ve teknikler kullanarak karmaşık problemleri çözmeye çalışır.

### Makine Öğrenimi (ML)

Makine Öğrenimi, bilgisayar sistemlerinin verilerden öğrenmesini ve deneyim kazanmasını sağlayan bir yapay zeka alt dalıdır. Makine öğrenimi algoritmaları, veri analizi ve model oluşturma süreçlerini içerir ve genellikle tahmin yapma veya desen tanıma gibi görevler için kullanılır.

## Proje Açıklaması

Bu proje, K-En Yakın Komşu (k-NN) algoritmasını kullanarak Iris veri seti üzerinde çiçek türlerini sınıflandırmayı göstermektedir. Iris veri seti, üç farklı iris çiçeği türünün (Setosa, Versicolour, Virginica) dört özellik ölçümünü içerir: sepal uzunluğu, sepal genişliği, petal uzunluğu ve petal genişliği.

Proje aşağıdaki adımları içermektedir:

1. Veri setinin yüklenmesi ve özelliklerin belirlenmesi.
2. Veri setinin eğitim ve test setlerine rastgele olarak bölünmesi.
3. K-En Yakın Komşu sınıflandırıcı modelinin oluşturulması ve eğitilmesi.
4. Yeni bir veri noktası için sınıflandırma tahmini yapılması.
5. Modelin doğruluğunun hesaplanması ve sonuçların değerlendirilmesi.

## Veri Setinin Eğitim ve Test Setlerine Bölünmesi

Veri seti, projeyi eğitmek ve test etmek için varsayılan olarak %75 eğitim ve %25 test setleri olarak rastgele bölünmüştür. Bu bölme oranları genellikle kullanılan standart bir uygulamadır. Eğitim seti, modelin öğrenmesi için kullanılan veri parçalarını içerirken, test seti modelin genel performansını değerlendirmek için ayrılmıştır.


## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- scikit-learn
- numpy

Gerekli kütüphaneleri yüklemek için terminal veya komut istemcisinde şu komutları kullanabilirsiniz:


## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için [MIT Lisansı](LICENSE) dosyasına göz atabilirsiniz.


