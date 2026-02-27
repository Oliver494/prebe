import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import socket

app = FastAPI()

# 1. Calculamos la ruta base para que no se pierda en Windows
# Esto busca la carpeta donde está 'static' y 'templates'
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 2. Conexión con la carpeta 'static' (CSS, JS, Imágenes)
app.mount("/static", StaticFiles(directory=os.path.join(base_dir, "static")), name="static")

# 3. Conexión con la carpeta 'templates' (HTML)
templates = Jinja2Templates(directory=os.path.join(base_dir, "templates"))

# Ruta Principal para PalenkeVision
@app.get("/")
async def read_root(request: Request):
    # El diccionario {"request": request} es OBLIGATORIO en FastAPI
    return templates.TemplateResponse("index.html", {"request": request})

# Ruta de ejemplo para los videos (opcional por ahora)
@app.get("/video/{video_id}")
async def get_video(video_id: str, request: Request):
    return {"status": "reproduciendo", "id": video_id}

# Este código detecta la IP de tu computadora automáticamente
def obtener_mi_url():
    nombre_equipo = socket.gethostname()
    direccion_ip = socket.gethostbyname(nombre_equipo)
    return f"http://{direccion_ip}:8000"

if __name__ == "__main__":
    import uvicorn
    # Obtenemos tu URL personalizada (ejemplo: http://192.168.1.15:8000)
    mi_url = obtener_mi_url()
    
    print(f"\n" + "="*50)
    print(f"🚀 PROYECTO PALENQUE VISIÓN ACTIVO")
    print(f"🌍 Tu URL personalizada es: {mi_url}")
    print(f"🏠 También puedes usar: http://localhost:8000")
    print(f"="*50 + "\n")
    
    # Ejecutamos el servidor
    uvicorn.run(app, host="0.0.0.0", port=8000)