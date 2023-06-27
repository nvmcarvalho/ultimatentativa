import sys
from cx_Freeze import setup, Executable

# Dependências do programa
build_exe_options = {"packages": ["pygame", "json", "tkinter", "winsound"],
                     "include_files": ["space.png", "bg.jpg", "somDeEspaço.mp3"]}

# Configuração do executável
exe = Executable(script="main.py",
                 base="Win32GUI" if sys.platform == "win32" else None,
                 icon="space.png")

setup(name="SpaceMarker",
      version="1.0",
      description="Space Marker Application",
      options={"build_exe": build_exe_options},
      executables=[exe])