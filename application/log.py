import logging

def get_logging_stat():
    from application.ayar_okuyucu import ConfigHandler as C
    return C.read_config("logging")

# Log dosyası ayarları
logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def log_ekle(mesaj, seviye="info"):
    if int(get_logging_stat()) == 1:
        if seviye.lower() == "info":
            logging.info(mesaj)
        elif seviye.lower() == "warning":
            logging.warning(mesaj)
        elif seviye.lower() == "error":
            logging.error(mesaj)
        elif seviye.lower() == "debug":
            logging.debug(mesaj)
        elif seviye.lower() == "critical":
            logging.critical(mesaj)
