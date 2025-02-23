from application.ultraconsole import UltraConsole as UC

def oyunlar(**kwargs):
    if UC.from_main_menu(**kwargs):
        root_key, root_index, file, path = UC.module_configs("games_menu_root", "games_menu_file", "games_module_path")
        UC.go_custom_menu(root_index, menu_data=file, module_path=path)