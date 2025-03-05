from application.ultraconsole import UltraConsole as UC

def _ornek_modul_alt_fonkisyon(**kwargs):
    
    if UC.selected_key(1, **kwargs):
        input("ornek_modul_alt_fonkisyon.py' dosyası, 'ornek_modul_alt_fonkisyon' fonksiyonu çalıştı ve 'Seçenek 1' seçildi")
    if UC.selected_key(2, **kwargs):
        input("ornek_modul_alt_fonkisyon.py' dosyası, 'ornek_modul_alt_fonkisyon' fonksiyonu çalıştı ve 'Seçenek 2' seçildi")