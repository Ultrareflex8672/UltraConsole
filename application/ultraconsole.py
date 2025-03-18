from application.menu_olusturucu import MenuSystem as MS
import getpass
import os

class UltraConsole(MS):

    def module_configs(menu_root_key = None, menu_file_key = None, module_path_key = None):
        configs = MS.read_config()
        if menu_file_key:
            menu_file = configs.get(menu_file_key)
        else:
            menu_file = configs.get("menu_file")

        if menu_root_key:
            menu_root = configs.get(menu_root_key)
        else:
            menu_root = configs.get("menu_root")

        if module_path_key:
            module_path = configs.get(module_path_key)
        else:
            module_path = configs.get("module_path")

        MS.check_and_create_config(menu_file)                   # Menü dosyasını kontrol et ve oluştur
        menu_data = MS.load_json(menu_file)
        root_key = list(menu_data.keys())[int(menu_root)]

        return root_key, int(menu_root), menu_data, module_path
    
    def go_main_menu(**kwargs):
        root, root_index, menu_data, module_path = UltraConsole.module_configs()
        ms = MS(menu_data[root], **kwargs)                                    # Menü sistemini başlat (init fonksiyonu çalışır ancak henüz menü gösterilmez)
        ms.show_menu(root)                                          # Menüyü göster

    # def go_main_menu():
    #     all_config = MS.read_config()                               # Tüm ayarları oku (Şuanda burada bir işlevi yok ancak ileride kullanılabilir)
    #     modules_path = all_config.get("module_path")                # Modül yolu al (Şuanda burada bir işlevi yok ancak ileride kullanılabilir)
    #     menu_root_config = MS.read_config("menu_root")              # Menü kökünü al
    #     MS.check_and_create_config(MS.read_config("menu_file"))     # Menü dosyasını kontrol et ve oluştur
    #     menu_data = MS.load_json(MS.read_config("menu_file"))       # Menü verilerini yükle
    #     root = list(menu_data.keys())[int(menu_root_config)]        # İlk menüyü al (menu.cfg Dosyasındaki JSon da 1. Seviyede Birden Fazla Menü varsa İlk Menüyü Alır)                          # Menü başlığını al
    #     ms = MS(menu_data[root])                                    # Menü sistemini başlat (init fonksiyonu çalışır ancak henüz menü gösterilmez)
    #     ms.show_menu(root)                                          # Menüyü göster

    def go_custom_menu(menu_root, **kwargs):
        # input(kwargs)
        if kwargs.get("menu_data"):
            menu_data_ = kwargs.get("menu_data")
            if isinstance(menu_data_, dict):
                menu_data = menu_data_
                if menu_root != None:
                    if isinstance(menu_root, int):
                        root = list(menu_data.keys())[int(menu_root)]
                    else: 
                        raise  "Menü root verisi INTEGER formatında değil!"
                else:
                    raise "Menü root verisi eksik!"
            else:
                raise  "Menü verisi DICT formatında değil!"
        elif menu_root:
            if isinstance(menu_root, int):
                MS.check_and_create_config(MS.read_config("menu_file"))
                menu_data = MS.load_json(MS.read_config("menu_file"))
                root = list(menu_data.keys())[int(menu_root)]
            else:
                raise  "Menü root verisi INTEGER formatında değil!"
        else:
            raise "Özel menü oluşturma parametrelerinden hiç biri girilmdi - menu_data_ = LIST, menu_root_ = STR"
        
        if kwargs.get("module_name"):
            module_name = kwargs.get("module_name")
        else:
            module_name = None

        if kwargs.get("func_name"):
            func_name = kwargs.get("func_name")
        else:
            func_name = None

        if kwargs.get("module_path") and isinstance(kwargs.get("module_path"), str):
            module_path=kwargs.get("module_path")
        else:
            module_path=MS.read_config("module_path")

        if kwargs.get("class_name"):
            class_name = kwargs.get("class_name")
        else:
            class_name = None

        if kwargs.get("init_data"):
            init_data = kwargs.get("init_data")
        else:
            init_data = None
        # input(kwargs)
        ms = MS(menu_data[root], 1, module_path, module_name, class_name, init_data, func_name, **kwargs)
        ms.show_menu(root)
    
    def selected_key(key=None, **kwargs):
        key_ = kwargs.get("selected_key")
        if key:
            if key_  == key:
                return True
            else:
                return None
        else:
            return key_

    
    def from_main_menu(**kwargs):
        if int(kwargs.get("menu_type")) == 0:
            return True
        else:
            return None
        
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear') 

    def get_pass(i):
        if i == 1:
            return getpass.getpass("Şifrenizi girin: ")
        if i == 2:
            return getpass.getpass("Şifrenizi tekar girin: ")


from colorama import Fore, Back, Style
import colorama
from gtts import gTTS
from datetime import datetime
from playsound import playsound
from bs4 import BeautifulSoup
# import mediapipe
# import speech_recognition
import webbrowser
import pytz
import wasabi
import mdurl
import requests
import regex
import wrapt
import zipp
import murmurhash
import preshed
import six
import packaging
import cycler
import catalogue
import jiter
import kiwisolver
import urllib3
import turtle
from html.parser import HTMLParser
import urllib.request
import zipfile
import shutil
import os
import time
import sys
import psutil
import signal
import uuid
import win32com.client


# Boyut Kontrolü Yapılmamış Kütüphaneler

# import annotated_types
# import anyio
# import certifi
# import cymem
# import h11
# import idna
# import joblib
# import tqdm
# import distro
# import sniffio
# import wheel
# import click
# import exceptiongroup
# import pefile
# import shellingham
# import smart_open
# import srsly
# import typer
# import tzdata
# import langcodes
# import language_data
# import psutil
# import pyparsing
# import typing_extensions
# import httpcore
# import httpx
# import termcolor
# import colorama
# import altgraph
# import confection
# import contourpy




#Büyük Boyutlu Kütüphaneler

# import cv2
# import mediapipe
# import weasel
# import rich
# import thinc
# import blis
# import pydantic_core
# import pydantic
# import numpy
# import pandas
# import nltk
# import seaborn
# import charset_normalizer
