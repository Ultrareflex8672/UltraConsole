import os
import importlib.util
from application.ayar_okuyucu import ConfigHandler

class ModuleLoader(ConfigHandler):
    @staticmethod
    def call_function(func_name, selection=None):
        module_path = os.path.join("modules", f"{func_name}.py")

        if not os.path.exists(module_path):
            message = f"Modül dosyası bulunamadı: {func_name}.py"
            print(message)
            return message
        
        spec = importlib.util.spec_from_file_location(func_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, func_name):
            func = getattr(module, func_name)
            return func(selection)
        else:
            message = f"{func_name} fonksiyonu {func_name}.py modülü içinde tanımlı değil."
            print(message)
            return message