import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "CXH_Local_Prompt", // Extension name
    async nodeCreated(node) {
       
        // 开头做一个小隔离
        if(!node.comfyClass.startsWith("CXH")) {
			return;
		}
        node.color = "#1b4669";
        // node.bgcolor = "#0198cb";
        
        if(node.comfyClass === "CXH_Local_Prompt"){
            node.setSize([600, 120]);
            const dir_pathWidget = node.widgets.find(w => w.name === "prompt");
            dir_pathWidget.hidden = false;
            let dir = dir_pathWidget.value;
            node.addWidget("button", "openFile", null, () => {
                    let file = dir_pathWidget.value;
                    // api方式获取路径
                    fetch('/api/cxh/cmf/gemini/open/file', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ path: file })
                    }).then(response => response.json())
                    .then(data => {
                }).catch(error => console.error("API请求失败:", error));
            });
            node.addWidget("button", "OpenDir", null, () => {
                console.log("点击")
                // api方式获取路径
                fetch('/api/cxh/cmf/gemini/open')
                .then(response => response.json())
                .then(data => {})
                .catch(error => console.error("API请求失败:", error));
            });
        }
    }
});
