# Sahibindencom-Scraper
Bu script, Selenium ve BeautifulSoup kullanarak belirtilen bir web sitesinden ilanları taramak için kullanılır. Başlık, fiyat ve konum gibi temel bilgileri çıkarır.

## Özellikler
- Kullanıcıdan bir ilan bağlantısı alır.
- Aşağıdaki bilgileri çıkarır ve görüntüler:
  - İlan başlığı
  - İlan fiyatı
  - İlan konumu
- Basit ve kullanıcı dostu bir arayüz.

## Gereksinimler
- Python 3.x
- Selenium
- BeautifulSoup
- Chrome WebDriver

## Kurulum
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/ibrahim12651/Sahibindencom-Scraper.git
   cd Sahibindencom-Scraper
   ```


2. Gerekli kütüphaneleri yükleyin:
   ```bash
    pip install -r requirements.txt
    ```

3. Chrome WebDriver'ı indirin ve PATH'e ekleyin:
    - [Chrome WebDriver](https://developer.chrome.com/docs/chromedriver/downloads?hl=tr)

## Kullanım
1. Script'i çalıştırın:
   ```bash
   python main.py
   ```
2. İlan bağlantısını girin:
   ```bash
    Ürün bağlantısını girin: https://www.sahibinden.com/emlak-konut
    ```
3. İlan bilgilerini görüntüleyin:
    ```bash
    ------------------------------
     İlan Başlığı: İstanbul Kadıköy Sahibinden Satılık Daire
     İlan Fiyatı: 1.000.000 TL
     İlan Konumu: İstanbul / Kadıköy
     ------------------------------
     ```

## İletişim
- [GitHub](https://github.com/ibrahim12651/Sahibindencom-Scraper/issues) (Hata ve öneriler için)

- [Discord-Support](https://discord.gg/hB47a96RGB) (İletişim için)

## Ekran Görüntüleri
![image](https://github.com/user-attachments/assets/76ea2ea6-fe1e-4d88-8327-08096ab7777c)




## Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.
