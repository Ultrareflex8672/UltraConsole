import os
import importlib.util
from application.ayar_okuyucu import ConfigHandler

class ModuleLoader(ConfigHandler):
    
    @staticmethod
    def call_function(modul_path_=[], module_name="", class_name_=None, init_data_=None, func_name_="", **kwargs):
        module_path = modul_path_
        if module_path == []:
            module_path_config = ConfigHandler.read_config()["module_path"]
            module_path = os.path.join(module_path_config, f"{module_name}.py")
        else:
            module_path = os.path.join(module_path, f"{module_name}.py")

        if not os.path.exists(module_path):
            message = f"Modül dosyası bulunamadı: {func_name_}.py"
            print(message)
            return message

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if class_name_:
            if hasattr(module, class_name_):
                if init_data_:
                    class_ = getattr(module, class_name_)
                    instance = class_(**init_data_)
                    func = getattr(instance, func_name_)
                    return func(**kwargs)
                else:
                    class_ = getattr(module, class_name_)
                    instance = class_()
                    func = getattr(instance, func_name_)
                    return func(**kwargs)
            else:
                message = f"{class_name_} sınıfı {module_name}.py modülü içinde tanımlı değil."
                print(message)
                return message
        else:
            if hasattr(module, func_name_):
                func = getattr(module, func_name_)
                return func(**kwargs)
            else:
                message = f"{func_name_} fonksiyonu {func_name_}.py modülü içinde tanımlı değil."
                print(message)
                return message