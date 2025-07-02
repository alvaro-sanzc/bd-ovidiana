import subprocess
import os
import shutil

# Ruta al directorio del proyecto
project_path = r".\\prototipo_web"
data_path = r"data"

# Cambiar al directorio del proyecto
os.chdir(project_path)

# Apagar contenedores (no necesitas --volumes porque usas bind mounts)
print("🛑 Apagando y eliminando contenedores...")
subprocess.run(["docker", "compose", "down"], check=True)

# Reconstruir e iniciar contenedores
print("🚀 Reconstruyendo e iniciando contenedores...")
subprocess.run(["docker", "compose", "up", "--build"], check=True)
