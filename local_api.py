import folder_paths
import os
import nodes
from server import PromptServer
from aiohttp import web


comfy_path = os.path.dirname(folder_paths.__file__)
custom_nodes_path = os.path.join(comfy_path, "custom_nodes")

mode_path = folder_paths.models_dir
current_folder = os.path.dirname(os.path.abspath(__file__))

prompt_dir =os.path.join(current_folder,"folder","prompt")

def register_routes():

    @PromptServer.instance.routes.get("/cxh/cmf/gemini/open")
    async def get_comfyui_folderInfo(request):
        os.startfile(prompt_dir)
        return web.json_response({"success": "ok"},status=200)
    
    @PromptServer.instance.routes.post("/cxh/cmf/gemini/open/file")
    async def open_tag_folder(request):
        data = await request.json()
        path = data.get("path", "./")

        file = os.path.join(prompt_dir,path + ".txt")
        print(file)
        

        os.startfile(file) 
        return web.json_response({"success": "ok"},status=200)