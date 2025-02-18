import json
import os

class FileLoader:
    @staticmethod
    def load_json(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
        
    @staticmethod
    def create_file(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("")
        
    @staticmethod
    def load_file(file_path):     
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    
    @staticmethod
    def load_lines(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.readlines()
    
    @staticmethod
    def write_file(file_path, content):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)