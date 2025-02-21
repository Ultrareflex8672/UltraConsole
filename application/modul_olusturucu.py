import os
import importlib.util
from application.ayar_okuyucu import ConfigHandler

class ModuleLoader(ConfigHandler):
    
    @staticmethod
    def call_function(modul_path=[], module_name="", class_name=None, init_data=None, func_name="", **kwargs):
        module_path = modul_path
        if module_path == []:
            module_path_config = ConfigHandler.read_config()["module_path"]
            module_path = os.path.join(module_path_config, f"{module_name}.py")
        else:
            module_path = os.path.join(module_path, f"{module_name}.py")

        if not os.path.exists(module_path):
            message = f"Modül dosyası bulunamadı: {func_name}.py"
            print(message)
            return message

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if class_name:
            if hasattr(module, class_name):
                if init_data:
                    class_ = getattr(module, class_name)
                    instance = class_(init_data)
                    func = getattr(instance, func_name)
                    return func(**kwargs)
                else:
                    class_ = getattr(module, class_name)
                    instance = class_()
                    func = getattr(instance, func_name)
                    return func(**kwargs)
            else:
                message = f"{class_name} sınıfı {module_name}.py modülü içinde tanımlı değil."
                print(message)
                return message
        else:
            if hasattr(module, func_name):
                func = getattr(module, func_name)
                return func(**kwargs)
            else:
                message = f"{func_name} fonksiyonu {func_name}.py modülü içinde tanımlı değil."
                print(message)
                return message