kapasite_mah = 5000      
kullanilabilir = 0.8     
ortalama_akim_a = 18     
toplam_agirlik_g = 1600  
motor_itkisi_g = 950     
motor_sayisi = 4

sure_dk = kapasite_mah / 1000 * kullanilabilir / ortalama_akim_a * 60
itki_agirlik = motor_itkisi_g * motor_sayisi / toplam_agirlik_g

print(f"Yaklaşık uçuş süresi: {sure_dk:.1f} dk")
print(f"İtki/ağırlık oranı: {itki_agirlik:.2f} (en az 2 olmalı)")