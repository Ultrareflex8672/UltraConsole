from application.ultraconsole import UltraConsole as UC

def _ornek_modul(**kwargs):
    if UC.selected_key(1, **kwargs):
        UC.create_frame("Örnek Modül 1. Alt Fonksiyon", "Örnek Modül 1. Alt Fonksiyon Çlıştı")
    if UC.selected_key(2, **kwargs):
        UC.create_frame("Örnek Modül 2. Alt Fonksiyon", "Örnek Modül 2. Alt Fonksiyon Çlıştı")
    del kwargs["menu_data"]
    del kwargs["module_path"]
    UC.go_main_menu(**kwargs)
