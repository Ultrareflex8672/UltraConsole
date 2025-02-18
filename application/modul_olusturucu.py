import os
import importlib.util
from application.ayar_okuyucu import ConfigHandler

class ModuleLoader(ConfigHandler):
    @staticmethod
    def call_function(func_name):
        module_path = os.path.join("modul", f"{func_name}.py")

        if not os.path.exists(module_path):
            print(f"Fonksiyon bulunamadı: {func_name}.py")
            return
        
        spec = importlib.util.spec_from_file_location(func_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, func_name):
            getattr(module, func_name)()
        else:
            print(f"{func_name} fonksiyonu {func_name}.py içinde tanımlı değil.")