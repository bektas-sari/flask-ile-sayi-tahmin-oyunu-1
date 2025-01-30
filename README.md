# Python/Flask ile Web Uygulama - Sayı Tahmin Oyunu

Bu proje, Flask tabanlı bir web uygulaması olup kullanıcının 1 ile 100 arasında rastgele tutulan bir sayıyı tahmin etmesini amaçlamaktadır. Kullanıcının girdisine bağlı olarak ipuçları verilir ve doğru tahminde oyun tamamlanır. Yeni oyun başlatma seçeneği mevcuttur.

## Özellikler
- Flask framework'ü kullanarak geliştirilmiş sunucu tarafı kodu
- HTML, CSS ve JavaScript kullanılarak tasarlanmış modern ve responsive arayüz
- Kullanıcının girdisine bağlı olarak dinamik geribildirim sistemi
- Yeni oyun başlatma seçeneği

## Kurulum

### Gereksinimler
- Python 3.x
- Flask framework

### Adımlar
1. Bu depoyu bilgisayarınıza klonlayın:
    ```sh
    git clone https://github.com/bektas-sari/flask-ile-sayi-tahmin-oyunu-1.git
    cd sayi-tahmin-oyunu
    ```
2. Gerekli Python paketlerini yükleyin:
    ```sh
    pip install flask
    ```
3. Flask uygulamasını başlatın:
    ```sh
    python app.py
    ```
4. Tarayıcınızda **http://127.0.0.1:5000/** adresine giderek oyunu oynayabilirsiniz.

## Kullanım
1. Sayfaya girdikten sonra "1 ile 100 arasında bir sayı tuttum. Tahmin et!" mesajını göreceksiniz.
2. Sayınızı girerek **Tahmin Et** butonuna basın.
3. Sistem, sayının daha büyük veya küçük olduğunu belirterek size ipucu verecektir.
4. Doğru tahmin ettiğinizde, toplam tahmin sayınız ile bir tebrik mesajı alacaksınız.
5. "Yeni Oyun Başlat" butonunu kullanarak yeni bir oyun başlatabilirsiniz.

## Proje Yapısı
```
|-- static/
|   |-- style.css  # CSS dosyası
|   |-- script.js  # JavaScript dosyası
|
|-- templates/
|   |-- index.html  # Ana HTML sayfası
|
|-- app.py  # Flask sunucu uygulaması
|-- README.md  # Proje hakkında detaylı bilgi
```

## Katkıda Bulunma
Projeye katkıda bulunmak isterseniz:
1. Depoyu forklayın
2. Yeni bir dal oluşturun: `git checkout -b yeni-ozellik`
3. Değişikliklerinizi yapın ve commitleyin: `git commit -m 'Yeni bir özellik ekledim'`
4. Güncellemelerinizi gönderin: `git push origin yeni-ozellik`
5. Bir pull request açın

## Lisans
Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.
