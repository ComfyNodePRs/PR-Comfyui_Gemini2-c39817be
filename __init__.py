from .cxh_gemini import CXH_Gemini2_TX, CXH_Gemini2_Vision
from .cxh_prompt import CXH_Local_Prompt
# Other
from .local_api import register_routes

NODE_CLASS_MAPPINGS = {
    "CXH_Gemini2_TX":CXH_Gemini2_TX,
    "CXH_Gemini2_Vision":CXH_Gemini2_Vision,
    "CXH_Local_Prompt":CXH_Local_Prompt
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CXH_Gemini2_TX":"CXH_Gemini2_TX",
    "CXH_Gemini2_Vision":"CXH_Gemini2_Vision",
    "CXH_Local_Prompt":"CXH_Local_Prompt"
}

WEB_DIRECTORY = "./web"

# 注册api
register_routes()