
import os
import torch
from PIL import Image
import folder_paths
import random
import string
import glob

current_folder = os.path.dirname(os.path.abspath(__file__))

def list_files_names(input_dir, ext):  
    # 确保目录存在，如果不存在则创建  
    if not os.path.exists(input_dir):  
        os.makedirs(input_dir)  
      
    # 使用glob查找指定扩展名的文件  
    file_paths = glob.glob(os.path.join(input_dir, '*' + ext))  
      
    # 初始化一个空列表来存储文件名（不带扩展名）  
    file_names = []  
      
    # 遍历文件路径，提取文件名并去除扩展名  
    for file_path in file_paths:  
        # os.path.splitext() 返回文件名和扩展名，我们只需要文件名部分  
        filename, _ = os.path.splitext(os.path.basename(file_path))  
        file_names.append(filename)  
      
    # 返回文件名列表  
    return file_names 

class CXH_Local_Prompt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        input_dir =  os.path.join(current_folder,"folder","prompt")
        if not os.path.exists(input_dir):
            os.makedirs(input_dir)
            # 创建文件并写入内容
            file_path = os.path.join(input_dir, "prompt.txt")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("write prompt")
        FILE_LIST = list_files_names(input_dir,".txt")
        return {
            "required": {
                "prompt":  (FILE_LIST,), 
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("out",)
    FUNCTION = "gen"
    OUTPUT_NODE = False
    CATEGORY = "CXH/LLM"

    def gen(self, prompt):
        file_path =  os.path.join(current_folder,"folder","prompt",prompt+".txt")
        new_string = ""
        # 打开文件  
        with open(file_path, 'r', encoding='utf-8') as file:  
            # 读取文件全部内容  
            new_string = file.read()  
        return (new_string,)