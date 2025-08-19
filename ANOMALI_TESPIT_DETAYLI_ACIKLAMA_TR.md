# 🔍 ANOMALİ TESPİT YÖNTEMLERİNİN DETAYLI AÇIKLAMASI

## 📚 **Genel Bakış**
Bu doküman, mobilite verilerinde anomali tespiti için kullanılan 5 farklı yöntemi, oylama sistemini, model değerlendirme metriklerini ve model açıklanabilirliğini detaylı olarak açıklar.

---

## 🎯 **ANOMALİ YÖNTEMLERİNİN DETAYLI AÇIKLAMASI**

### **1. Z-Score Yöntemi**
**Nasıl Çalışır?**
- Her özellik için ortalama ve standart sapma hesaplanır
- Her değer için: `Z = (değer - ortalama) / standart sapma`
- `|Z| > 3` olan değerler anomali kabul edilir

**Örnek:**
- Yolculuk süresi ortalaması: 30 dakika, standart sapma: 7 dakika
- 120 dakikalık yolculuk için: `Z = (120-30)/7 = 12.86`
- `|12.86| > 3` olduğu için → ANOMALİ

**Neden 3?** Normal dağılımda verilerin %99.7'si ±3 standart sapma içinde kalır

**Avantajları:**
- Hızlı hesaplama
- İstatistiksel olarak sağlam
- Aşırı değerleri iyi yakalar

**Dezavantajları:**
- Sadece normal dağılım varsayımı
- Çok büyük veri setlerinde yavaş olabilir

### **2. IQR (Interquartile Range) Yöntemi**
**Nasıl Çalışır?**
- Q1 (25. persentil) ve Q3 (75. persentil) hesaplanır
- IQR = Q3 - Q1
- Alt sınır = Q1 - 1.5×IQR
- Üst sınır = Q3 + 1.5×IQR
- Bu sınırlar dışındaki değerler anomali

**Örnek:**
- Yolculuk süresi: Q1=26.5, Q3=33.3, IQR=6.8
- Alt sınır = 26.5 - 1.5×6.8 = 16.3 dakika
- Üst sınır = 33.3 + 1.5×6.8 = 43.5 dakika
- 1 dakika < 16.3 → ANOMALİ
- 120 dakika > 43.5 → ANOMALİ

**Avantajları:**
- Dağılım bağımsız
- Aykırı değerlere karşı dayanıklı
- Anlaşılması kolay

**Dezavantajları:**
- Çok büyük veri setlerinde yavaş
- Çok küçük veri setlerinde güvenilmez

### **3. Isolation Forest Yöntemi**
**Nasıl Çalışır?**
- Rastgele özellikler seçilir
- Rastgele eşik değerleri belirlenir
- Veri noktaları ağaç yapısında bölünür
- Normal noktalar daha derin seviyelerde izole edilir
- Anomaliler daha yüzeysel seviyelerde izole edilir

**Örnek:**
- Normal yolculuk (30 dakika): 8-10 bölme sonra izole edilir
- Anormal yolculuk (120 dakika): 2-3 bölme sonra izole edilir
- Daha az bölme = daha anormal

**Avantajları:**
- Büyük veri setlerinde hızlı
- Çok boyutlu verilerde etkili
- Parametre ayarı kolay

**Dezavantajları:**
- Rastgelelik nedeniyle sonuçlar değişebilir
- Çok küçük veri setlerinde zayıf

### **4. PCA (Principal Component Analysis) Yöntemi**
**Nasıl Çalışır?**
- Veriyi 2 boyuta sıkıştırır (500×2 → 2×2)
- Sıkıştırılmış veriyi tekrar orijinal boyuta çıkarır
- Orijinal veri ile yeniden oluşturulan veri arasındaki fark hesaplanır
- Bu fark (reconstruction error) yüksek olanlar anomali

**Örnek:**
- Normal veri: Düşük reconstruction error
- Anormal veri: Yüksek reconstruction error
- 95. persentil üzerindeki hatalar anomali kabul edilir

**Avantajları:**
- Boyut azaltma ile birlikte anomali tespiti
- Lineer ilişkileri yakalar
- Gürültüye karşı dayanıklı

**Dezavantajları:**
- Sadece lineer ilişkileri yakalar
- Non-lineer anomalileri kaçırabilir

### **5. DBSCAN (Density-Based Spatial Clustering) Yöntemi**
**Nasıl Çalışır?**
- Her nokta için belirli yarıçapta (eps=0.5) komşu sayısı hesaplanır
- Minimum komşu sayısı (min_samples=5) altında kalan noktalar anomali
- Yoğun bölgelerdeki noktalar normal, seyrek bölgelerdeki anomali

**Örnek:**
- Normal nokta: 5+ komşu bulur
- Anormal nokta: 5'ten az komşu bulur → ANOMALİ

**Avantajları:**
- Yoğunluk tabanlı yaklaşım
- Küme şeklini önemsemez
- Gürültüye karşı dayanıklı

**Dezavantajları:**
- Parametre seçimi zor
- Farklı yoğunluktaki kümelerde zayıf

---

## 🗳️ **3+ OY SİSTEMİNİN DETAYLI AÇIKLAMASI**

### **Oylama Sistemi:**
Her yöntem 0 veya 1 oy verir:
- **Z-Score**: Anomali bulursa 1, bulamazsa 0
- **IQR**: Anomali bulursa 1, bulamazsa 0  
- **Isolation Forest**: Anomali bulursa 1, bulamazsa 0
- **PCA**: Anomali bulursa 1, bulamazsa 0
- **DBSCAN**: Anomali bulursa 1, bulamazsa 0

### **Toplam Oy Dağılımı:**
- **0 oy**: Hiçbir yöntem anomali bulamadı → Normal
- **1 oy**: Sadece 1 yöntem anomali buldu → Şüpheli
- **2 oy**: 2 yöntem anomali buldu → Muhtemelen anomali
- **3+ oy**: 3+ yöntem anomali buldu → Kesin anomali

### **Örnek Senaryo:**
Bir yolculuk verisi için:
- Z-Score: 0 (normal aralıkta)
- IQR: 1 (çit dışında)
- Isolation Forest: 1 (izole edildi)
- PCA: 1 (yüksek reconstruction error)
- DBSCAN: 0 (yoğun bölgede)

**Toplam: 3 oy → ANOMALİ**

### **Oylama Sisteminin Avantajları:**
1. **Güvenilirlik**: Tek yöntemin hatası telafi edilir
2. **Kapsamlılık**: Farklı yaklaşımlar birleştirilir
3. **Esneklik**: Farklı anomali tipleri yakalanır
4. **Şeffaflık**: Her yöntemin katkısı görülür

---

## 📊 **MODEL DEĞERLENDİRMESİNİN DETAYLI AÇIKLAMASI**

### **1. Accuracy (Doğruluk)**
**Ne Ölçer?** Tüm tahminlerin doğru olma oranı
**Formül:** `(Doğru Pozitif + Doğru Negatif) / Toplam`
**Örnek:** 100 tahmin, 90'ı doğru → Accuracy = 90%

**Problem:** Sınıf dengesizliğinde yanıltıcı olabilir
- 95 normal, 5 anomali varsa
- "Hepsi normal" dersek → Accuracy = 95% (ama hiç anomali bulamadık!)

**Ne Zaman Kullanılır?**
- Sınıflar dengeli olduğunda
- Genel performans değerlendirmesi için
- Hızlı karşılaştırma için

### **2. Precision (Kesinlik)**
**Ne Ölçer?** "Anomali dediğim gerçekten anomali mi?"
**Formül:** `Doğru Pozitif / (Doğru Pozitif + Yanlış Pozitif)`
**Örnek:** 10 anomali tahmini, 8'i gerçek anomali → Precision = 80%

**Yüksek Precision:** Az yanlış alarm (false positive)

**Pratik Anlamı:**
- Yüksek precision = Az gereksiz uyarı
- Düşük precision = Çok yanlış alarm
- Maliyetli işlemlerde önemli

### **3. Recall (Geri Çağırma)**
**Ne Ölçer?** "Gerçek anomalilerin kaçını yakaladım?"
**Formül:** `Doğru Pozitif / (Doğru Pozitif + Yanlış Negatif)`
**Örnek:** 20 gerçek anomali, 16'sını buldum → Recall = 80%

**Yüksek Recall:** Az kaçırılan anomali (false negative)

**Pratik Anlamı:**
- Yüksek recall = Az kaçırılan anomali
- Düşük recall = Çok anomali kaçırıldı
- Güvenlik kritik uygulamalarda önemli

### **4. F1-Score**
**Ne Ölçer?** Precision ve Recall'ın harmonik ortalaması
**Formül:** `2 × (Precision × Recall) / (Precision + Recall)`
**Neden?** Precision ve Recall arasında denge kurar

**Örnek:**
- Precision = 0.8, Recall = 0.6
- F1 = 2 × (0.8 × 0.6) / (0.8 + 0.6) = 0.69

**Avantajları:**
- Tek metrik ile performans değerlendirmesi
- Precision ve Recall arasında denge
- Sınıf dengesizliğinde daha güvenilir

### **5. ROC-AUC (Receiver Operating Characteristic - Area Under Curve)**
**Ne Ölçer?** Modelin sınıfları ayırt etme yeteneği
**Değer Aralığı:** 0.5 (rastgele) - 1.0 (mükemmel)

**Yorum:**
- 0.5-0.6: Zayıf
- 0.6-0.7: Orta
- 0.7-0.8: İyi
- 0.8-0.9: Çok iyi
- 0.9-1.0: Mükemmel

**Ne Zaman Kullanılır?**
- Model karşılaştırması için
- Genel performans değerlendirmesi için
- Eşik değer seçimi için

### **6. Average Precision (AP)**
**Ne Ölçer?** Precision-Recall eğrisinin altındaki alan
**Neden Önemli?** Sınıf dengesizliğinde ROC-AUC'dan daha güvenilir
**Değer Aralığı:** 0.0 - 1.0

**Avantajları:**
- Sınıf dengesizliğinde güvenilir
- Precision-Recall dengesini gösterir
- Anomali tespitinde özellikle önemli

---

## 🧠 **MODEL AÇIKLANABİLİRLİĞİNİN DETAYLI AÇIKLAMASI**

### **1. Permutation Importance (Permütasyon Önem)**
**Ne Ölçer?** Bir özelliğin model performansına ne kadar katkı sağladığı

**Nasıl Çalışır?**
1. Model normal veriyle eğitilir
2. Bir özellik rastgele karıştırılır (permütasyon)
3. Model performansı tekrar ölçülür
4. Performans düşüşü hesaplanır
5. Bu işlem 20 kez tekrarlanır
6. Ortalama performans düşüşü hesaplanır

**Örnek:**
- Normal performans: F1 = 0.8
- Hız özelliği karıştırıldıktan sonra: F1 = 0.6
- Performans düşüşü: 0.2
- **Sonuç:** Hız özelliği çok önemli

**Neden Önemli?** 
- Hangi özelliklerin anomali tespitinde kritik olduğunu gösterir
- Model kararlarının güvenilirliğini artırır
- Alan uzmanlarına güven verir

### **2. Partial Dependence Plot (PDP)**
**Ne Gösterir?** Bir özelliğin değeri değişince model tahmininin nasıl değiştiği

**Nasıl Çalışır?**
1. Bir özelliğin değeri sistematik olarak değiştirilir
2. Diğer özellikler sabit tutulur
3. Her değer için model tahmini alınır
4. Grafik çizilir

**Örnek Senaryo:**
```
Yolculuk Süresi → Anomali Olasılığı
10 dakika     → %5 (normal)
20 dakika     → %10 (normal)
30 dakika     → %15 (normal)
60 dakika     → %70 (anomali!)
90 dakika     → %95 (anomali!)
120 dakika    → %99 (anomali!)
```

**Yorum:**
- 30 dakikaya kadar: Normal
- 60+ dakika: Anomali riski yüksek
- 90+ dakika: Kesin anomali

### **3. PDP'nin Pratik Faydaları**
**1. Eşik Değer Belirleme:**
- Hangi yolculuk süresi anomali kabul edilmeli?
- PDP'ye bakarak %50 eşiği belirlenebilir

**2. İş Kuralları:**
- "60 dakikadan uzun yolculuklar incelensin"
- "90 dakikadan uzun yolculuklar otomatik reddedilsin"

**3. Alan Uzmanı Onayı:**
- İstatistikçi: "Bu eşik mantıklı mı?"
- Ulaşım uzmanı: "Bu süreler gerçekçi mi?"

**4. Risk Değerlendirmesi:**
- Hangi değerler kritik?
- Hangi aralıklar güvenli?
- Hangi eşikler kullanılmalı?

### **4. PDP vs Permutation Importance**
**Permutation Importance:**
- Hangi özellik daha önemli?
- Sayısal değer verir
- Karşılaştırma yapılabilir
- Genel önem sıralaması

**PDP:**
- Özelliğin nasıl etki ettiği?
- Görsel analiz
- Eşik değer belirleme
- Detaylı davranış analizi

---

## 🎯 **PRATİK UYGULAMA ÖRNEKLERİ**

### **Senaryo 1: Yolculuk Süresi Anomalisi**
**Veri:** 120 dakika yolculuk
**Z-Score:** 1 (anomali)
**IQR:** 1 (anomali)  
**Isolation Forest:** 1 (anomali)
**PCA:** 1 (anomali)
**DBSCAN:** 0 (normal)

**Toplam:** 4 oy → **KESİN ANOMALİ**

**Açıklama:** 4/5 yöntem anomali buldu, bu yolculuk gerçekten anormal

**Pratik Uygulama:**
- Otomatik uyarı sistemi
- Manuel inceleme için işaretleme
- Rota optimizasyonu önerisi

### **Senaryo 2: Şüpheli Hız**
**Veri:** 80 km/s hız
**Z-Score:** 0 (normal)
**IQR:** 1 (anomali)
**Isolation Forest:** 0 (normal)
**PCA:** 0 (normal)
**DBSCAN:** 0 (normal)

**Toplam:** 1 oy → **ŞÜPHELİ**

**Açıklama:** Sadece IQR anomali buldu, diğer yöntemler normal dedi

**Pratik Uygulama:**
- Düşük öncelikli inceleme
- Geçici işaretleme
- Daha fazla veri toplama

### **Senaryo 3: Normal Yolculuk**
**Veri:** 35 dakika yolculuk
**Z-Score:** 0 (normal)
**IQR:** 0 (normal)
**Isolation Forest:** 0 (normal)
**PCA:** 0 (normal)
**DBSCAN:** 0 (normal)

**Toplam:** 0 oy → **NORMAL**

**Açıklama:** Hiçbir yöntem anomali bulamadı, bu yolculuk normal

**Pratik Uygulama:**
- Otomatik onay
- Hızlı işlem
- Kaynak tasarrufu

---

## 🔧 **SİSTEM KURULUMU VE PARAMETRE AYARLARI**

### **Z-Score Parametreleri:**
- **Eşik değeri:** 3 (varsayılan), 2.5 (daha hassas), 3.5 (daha az hassas)
- **Özellik seçimi:** Tüm sayısal özellikler
- **Normalizasyon:** Gerekli değil

### **IQR Parametreleri:**
- **Çarpan:** 1.5 (varsayılan), 1.0 (daha hassas), 2.0 (daha az hassas)
- **Özellik seçimi:** Tüm sayısal özellikler
- **Normalizasyon:** Gerekli değil

### **Isolation Forest Parametreleri:**
- **n_estimators:** 100 (varsayılan), 50-200 arası
- **contamination:** 0.1 (varsayılan), 0.05-0.2 arası
- **max_samples:** 'auto' (varsayılan), 100-200 arası

### **PCA Parametreleri:**
- **n_components:** 2 (varsayılan), 1-3 arası
- **Eşik:** 95. persentil (varsayılan), 90-99 arası
- **Normalizasyon:** Gerekli

### **DBSCAN Parametreleri:**
- **eps:** 0.5 (varsayılan), 0.1-1.0 arası
- **min_samples:** 5 (varsayılan), 3-10 arası
- **Normalizasyon:** Gerekli

---

## 📈 **PERFORMANS OPTİMİZASYONU**

### **Veri Ön İşleme:**
1. **Eksik Veri:** Median imputation
2. **Normalizasyon:** StandardScaler
3. **Özellik Seçimi:** Sayısal özellikler
4. **Veri Temizliği:** Aykırı değer kontrolü

### **Model Seçimi:**
1. **Isolation Forest:** Hızlı, genel amaçlı
2. **Random Forest:** Doğru, açıklanabilir
3. **Ensemble:** Güvenilir, kapsamlı

### **Hiperparametre Optimizasyonu:**
1. **Grid Search:** Sistematik arama
2. **Cross Validation:** 3-fold CV
3. **Metrik:** F1-score, ROC-AUC
4. **Paralel İşlem:** n_jobs=-1

---

## 🚀 **SONUÇ VE ÖNERİLER**

### **Sistem Avantajları:**
1. **Çok Yöntemli:** Farklı yaklaşımlar birleştirilir
2. **Güvenilir:** Ensemble kararlar daha sağlam
3. **Açıklanabilir:** Model kararları anlaşılır
4. **Esnek:** Farklı veri tiplerine uyarlanabilir

### **Kullanım Alanları:**
1. **Ulaşım Sistemleri:** Yolculuk anomalileri
2. **Finans:** İşlem anomalileri
3. **Sağlık:** Tıbbi veri anomalileri
4. **Üretim:** Kalite kontrol anomalileri

### **Gelecek Geliştirmeler:**
1. **Derin Öğrenme:** LSTM, Autoencoder
2. **Gerçek Zamanlı:** Streaming veri analizi
3. **Otomatik Eşik:** Adaptif parametre ayarı
4. **Çok Boyutlu:** Zaman serisi analizi

---

## 📚 **KAYNAKLAR VE REFERANSLAR**

1. **Z-Score:** Standard Score, Normal Distribution
2. **IQR:** Tukey's Method, Box Plot
3. **Isolation Forest:** Liu et al. (2008)
4. **PCA:** Principal Component Analysis, Reconstruction Error
5. **DBSCAN:** Density-Based Clustering, Ester et al. (1996)
6. **Ensemble Methods:** Voting Systems, Majority Decision
7. **Model Evaluation:** Classification Metrics, ROC-AUC
8. **Explainability:** Permutation Importance, Partial Dependence

---

*Bu doküman, mobilite verilerinde anomali tespiti için geliştirilen sistemin detaylı teknik açıklamasını içerir. Sorularınız için lütfen iletişime geçin.*
