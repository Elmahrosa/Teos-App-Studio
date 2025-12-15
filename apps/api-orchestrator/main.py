from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ModuleAction(BaseModel):
    id: str

@app.post("/modules/install")
def install_module(action: ModuleAction):
    # TODO: add real logic (DB, registry, etc.)
    return {"ok": True, "module": action.id, "status": "installed"}

@app.post("/modules/uninstall")
def uninstall_module(action: ModuleAction):
    return {"ok": True, "module": action.id, "status": "removed"}

@app.get("/modules/{module_id}")
def get_module(module_id: str):
    return {"ok": True, "module": module_id, "details": "Mock details"}
