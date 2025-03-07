from application.ultraconsole import UltraConsole as UC

# root_key, root_index, file, path = UC.module_configs("games_menu_root", "games_menu_file", "games_module_path")

def oyunlar(**kwargs):
    if UC.from_main_menu(**kwargs):
        oyunlar_menu(**kwargs)

def oyunlar_menu(**kwargs):
    UC.go_custom_menu(2,**kwargs)
