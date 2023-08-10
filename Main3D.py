from gl import Renderer, V2, V3, color
import shaders

# Tamaño del Frame para la pantalla
width = 800
height = 800 

# Create Render
rend = Renderer(width, height)

# Shaders a utilizar
rend.vertexShader=shaders.vertexShader
rend.fragmentShader=shaders.fragmentShader

# ---------------------------------------Creación Medium Shot---------------------------------------

# Especificaciones camara para el Shot
rend.glLookAt(camPos=(0,0,3),
         eyePos=(0,0,0))

# Especificaciones Basicas y fijas del modelo para mostrar en pantalla
rend.glLoadModel(filename="model.obj", 
                 textureName="model.bmp", 
                 translate=(240, 175, 0),
                 scale=(22,22,22), 
                 rotate=(0,180,0))

rend.glRender()

rend.glFinish('MediumShot.bmp')

# ---------------------------------------Creación Low-Angle Shot---------------------------------------

# Especificaciones camara para el Shot
rend.glLookAt(camPos=(0, 1, 3),
             eyePos=(0, -2, -3))

# Corre y va de nuevo..
rend.glClear()  


rend.glRender()
rend.glFinish('LowAngleShot.bmp')

# --------------------------------------- Creación High-Angle Shot---------------------------------------

# Especificaciones camara para el Shot
rend.glLookAt(camPos=(0, 3, 1),
            eyePos=(0, 0, 0))

# Corre y va de nuevo..
rend.glClear()


rend.glRender()
rend.glFinish('HighAngleShot.bmp')

# ---------------------------------------Creación Dutch-Angle Shot---------------------------------------

# Especificaciones camara para el Shot
rend.glLookAt(camPos=(5, 1, 3), eyePos=(0, 0, 0))

# Corre y va de nuevo..
rend.glClear()

rend.glRender()
rend.glFinish('DutchAngleShot.bmp')