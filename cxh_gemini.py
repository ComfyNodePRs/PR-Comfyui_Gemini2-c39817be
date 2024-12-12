
import os
import torch
from PIL import Image
import folder_paths
import json
import google.generativeai as genai
import numpy as np
import cv2 as cv

current_folder = os.path.dirname(os.path.abspath(__file__))

def get_gemini_key():
    try:
        config_path = os.path.join(current_folder, 'key.txt')
        # 读取整个文件内容
        with open(config_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except:
        print("Error: Gemini API key is required")
        return ""

def tensor2pil(t_image: torch.Tensor)  -> Image:
    return Image.fromarray(np.clip(255.0 * t_image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image:Image) -> torch.Tensor:
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


class CXH_Gemini2_TX:

    def __init__(self):
        self.gemini_key = get_gemini_key()
        if self.gemini_key:
            genai.configure(api_key=self.gemini_key, transport='rest')

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": (["gemini-2.0-flash-exp","gemini-1.5-pro", "gemini-1.5-flash", "gemini-1.5-flash-8b","learnlm-1.5-pro-experimental","gemini-exp-1114","gemini-exp-1121"],),
                "prompt":   ("STRING", {"multiline": True, "default": ""},), # forceInput 让节点直接显示在连接处
            }
        }

    RETURN_TYPES = ("STRING",) 
    RETURN_NAMES = ("out",)
    FUNCTION = "gen"
    OUTPUT_NODE = False 
    CATEGORY = "CXH/gemini"

    def gen(self, model,prompt):
        if not self.gemini_key:
            raise ValueError("Gemini API key is required")

        model = genai.GenerativeModel(model)
            
        response = model.generate_content(prompt)
        print(response.text)
        # 将结果列表中的张量连接在一起
        return (response.text,)

class CXH_Gemini2_Vision:

    def __init__(self):
        self.gemini_key = get_gemini_key()
        if self.gemini_key:
            genai.configure(api_key=self.gemini_key, transport='rest')

    @classmethod
    def INPUT_TYPES(s):
        return {  
            "required": {
                "image": ("IMAGE",{"forceInput": True},),
                "model": (["gemini-2.0-flash-exp","gemini-1.5-pro", "gemini-1.5-flash", "gemini-1.5-flash-8b","learnlm-1.5-pro-experimental","gemini-exp-1114","gemini-exp-1121"],),
                "prompt":   ("STRING", {"multiline": True, "default": ""},), # forceInput 让节点直接显示在连接处
            }
        }

    RETURN_TYPES = ("STRING",) 
    RETURN_NAMES = ("out",)
    FUNCTION = "gen"
    OUTPUT_NODE = False 
    CATEGORY = "CXH/gemini"

    def gen(self,image, model,prompt):
        if not self.gemini_key:
            raise ValueError("Gemini API key is required")

        model = genai.GenerativeModel(model)
        pil_image = tensor2pil(image)     
        response = model.generate_content([prompt, pil_image])
        print(response.text)
        # 将结果列表中的张量连接在一起
        return (response.text,)

