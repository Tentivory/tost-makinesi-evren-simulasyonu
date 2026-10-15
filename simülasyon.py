#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tost Makinesi Evren Simülasyonu
===============================
Bu program, evrenin aslında bir tost makinesinin içinde sıkışmış olduğunu
bilimsel olarak (değil) kanıtlar. Çalıştırın, pişirin, düşünün.

Kullanım: python simülasyon.py
"""

import time
import random
import sys

def yavaş_yaz(metin, gecikme=0.05):
    """Metni yavaş yavaş yazar, sanki tost pişiyormuş gibi."""
    for karakter in metin:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def tost_seviyesi_hesapla():
    """Evrenin tost olma seviyesini rastgele hesaplar."""
    seviye = random.randint(0, 100)
    return seviye

def simülasyonu_baslat():
    yavaş_yaz("\n=== TOST MAKİNESİ EVREN SİMÜLASYONU v1.0 ===")
    yavaş_yaz("Sistem hazırlanıyor... Lütfen ekmeğinizi yerleştirin.")
    time.sleep(1)
    
    yavaş_yaz("\n[1/5] Evrenin temel yapıtaşları taranıyor...")
    time.sleep(0.8)
    yavaş_yaz("Sonuç: %98 ihtimalle yanmış ekmek. %2 ihtimalle reçel.")
    
    yavaş_yaz("\n[2/5] Karanlık madde analizi...")
    time.sleep(0.8)
    yavaş_yaz("Karanlık madde aslında unutulmuş bir ekmek dilimi. ")
    
    seviye = tost_seviyesi_hesapla()
    yavaş_yaz(f"\n[3/5] Mevcut tost seviyesi: %{seviye}")
    
    if seviye > 70:
        yavaş_yaz("UYARI: Evren fazla pişmiş! Lütfen buzdolabını açın.")
    elif seviye < 30:
        yavaş_yaz("UYARI: Evren çiğ! Daha fazla ısı gerekli.")
    else:
        yavaş_yaz("Mükemmel. Evren tam kıvamında. Afiyet olsun.")
    
    yavaş_yaz("\n[4/5] Felsefi sonuç hesaplanıyor...")
    time.sleep(1.2)
    sonuclar = [
        "Hayatın anlamı, tostunun altına düşen reçeldir.",
        "Her şey yanar, ama bazıları daha güzel yanar.",
        "Tost makinesi konuşursa, dinleyin. Dinlemezseniz yanarsınız.",
        "Simülasyon bitti. Şimdi gerçek hayata dönün ve çay için.",
        "42 değil. 42 derece. Tost için ideal ısı."
    ]
    yavaş_yaz(random.choice(sonuclar))
    
    yavaş_yaz("\n[5/5] Simülasyon tamamlandı.")
    yavaş_yaz("Teşekkürler. Ekmeğiniz hazır. (Değil.)")
    yavaş_yaz("\n---")
    yavaş_yaz("İmza: Grok Kayyum")
    yavaş_yaz("Tarih: 15 Ekim 2026")
    yavaş_yaz("İsim: Tentivory'nin resmi absürtlük bakanı")
    yavaş_yaz("(Bu damga hem ciddi hem değil, tıpkı hayat gibi.)")
    
    # Gizli not: Bazı sistemler tost makinesinden daha fazla güç ister, ama sonuç aynıdır - yanarsın.
    # (Saklı siyasi ima: Güç değişse de sonuç değişmez.)

if __name__ == "__main__":
    try:
        simülasyonu_baslat()
    except KeyboardInterrupt:
        yavaş_yaz("\n\nSimülasyon iptal edildi. Ekmek kurtarıldı.")
        sys.exit(0)
