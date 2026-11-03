import time
import sys
import random
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    # colorama yüklü değilse düz metin olarak çalışır
    class Empty:
        def __getattr__(self, name): return ""
    Fore = Style = Empty()

def yavas_yaz(metin, hiz=0.03):
    """Metni ekrana daktilo efektiyle yavaşça yazdırır."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def uzay_gemisi_ciz():
    gemi = f"""
    {Fore.CYAN}          /\\
         /  \\
        |    |
       /|====|\\
      / |    | \\
     |  |    |  |
     {Fore.RED}   /__\\__/\\__\\
        (____/\\____)
         (  )(  )
          (  )(  )
           ()()
    """
    print(gemi)

def oyun():
    print("\n" + "="*50)
    uzay_gemisi_ciz()
    yavas_yaz(f"{Fore.YELLOW}🚀 DERİN UZAY MACERASI: KANATLI YILDIZ", 0.05)
    print("="*50 + "\n")

    yavas_yaz(f"{Fore.WHITE}Yıl 2154. Uzay gemin 'Starlight' ile bilinmeyen bir gezegenin yörüngesindesin.")
    yavas_yaz(f"{Fore.WHITE}Aniden kırmızı alarmlar çalmaya başladı! Geminin yakıtı tükeniyor.")
    
    yazilim_modulu = input(f"\n{Fore.GREEN}Gemi bilgisayarını yeniden başlatmak ister misin? (e/h): ").strip().lower()
    
    if yazilim_modulu == 'e':
        yavas_yaz(f"\n{Fore.CYAN}[SYSTEM] Sistemler taranıyor...", 0.04)
        time.sleep(1)
        print(f"{Fore.GREEN}✔ Motorlar stabilize edildi! Güvenli bir şekilde gezegene iniş yapıyorsun.")
        
        yavas_yaz(f"\nGezegenin yüzeyinde gizemli bir parıltı gördün.")
        secim = input(f"{Fore.YELLOW}1- Parıltıyı araştır\n2- Gemide kalıp yardım sinyali gönder\nKararın (1/2): ").strip()

        if secim == '1':
            yavas_yaz(f"\n{Fore.MAGENTA}✨ Harika! Eski bir uzay medeniyetine ait sonsuz enerji kristalini buldun.")
            yavas_yaz(f"{Fore.GREEN}🎉 TEBRİKLER! Görevi başarıyla tamamladın ve evrenin kahramanı oldun!")
        else:
            yavas_yaz(f"\n{Fore.BLUE}📡 Sinyal yaydın... Bir dost kurtarma gemisi seni buldu!")
            yavas_yaz(f"{Fore.GREEN}👍 Güvenle eve döndün. Tebrikler!")
            
    else:
        yavas_yaz(f"\n{Fore.RED}❌ Karar vermekte geç kaldın! Gemi atmosferde süzülmeye başladı...")
        yavas_yaz(f"{Fore.YELLOW}⚠️ Acil durum kapsülü Otomatik Fırlatıldı!")
         sans = random.randint(1, 2)
         if sans == 1:
             yavas_yaz(f"\n{Fore.GREEN}🪂 Kapsül güvenli bir yere indi. Kurtuldun!")
         else:
             yavas_yaz(f"\n{Fore.RED}💥 Kapsül bir meteora çarptı... Oyun Bitti.")

if __name__ == "__main__":
    oyun()
