from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Object3D:

    def __init__ (self, color, isSolid, translateX, translateY, translateZ):

        self.color = color
        self.isSolid = isSolid
        self.translateX = translateX
        self.translateY = translateY
        self.translateZ = translateZ
        
class Teapot (Object3D):
    
    def __init__ (self, color, isSolid, translateX, translateY, translateZ, size):
        
        super().__init__(color, isSolid, translateX, translateY, translateZ)
        self.size = size

class Cube (Object3D):
    
    def __init__ (self, color, isSolid, translateX, translateY, translateZ, size):
        
        super().__init__(color, isSolid, translateX, translateY, translateZ)
        self.size = size

class Shere (Object3D):
    
    def __init__ (self, color, isSolid, translateX, translateY, translateZ, radius, slices, stacks):
        
        super().__init__(color, isSolid, translateX, translateY, translateZ)
        self.radius = radius
        self.slices = slices
        self.stacks = stacks

class Cone (Object3D):
    
    def __init__ (self, color, isSolid, translateX, translateY, translateZ, radius, height, slices, stacks):
        
        super().__init__(color, isSolid, translateX, translateY, translateZ)
        self.radius = radius
        self.height = height
        self.slices = slices
        self.stacks = stacks

class Torus (Object3D):
    
    def __init__ (self, color, isSolid, translateX, translateY, translateZ, innerRadius, outerRadius, sides, rings):
        
        super().__init__(color, isSolid, translateX, translateY, translateZ)
        self.innerRadius = innerRadius
        self.outerRadius = outerRadius
        self.sides = sides
        self.rings = rings

# variaveis globais
r = 0
g = 0
b = 1
isSolid = False
angle = 45
posX = 0.0
posY = 0.0
posZ = 0.0
objects = []

# Callback de desenho
def draw():
    
    global objects

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for obj in objects:
        
        glColor3f(obj.color[0], obj.color[1], obj.color[2])
        glPushMatrix()
        glTranslatef(obj.translateX, obj.translateY, obj.translateZ)
        
        if (isinstance(obj, Teapot)):
            
            if(obj.isSolid):

                glutSolidTeapot(obj.size)
            else:

                glutWireTeapot(obj.size)
            
        elif (isinstance(obj, Cube)):
            
            if(obj.isSolid):

                glutSolidCube(obj.size)
            else:

                glutWireCube(obj.size)

        elif(isinstance(obj, Shere)):
            
            if(obj.isSolid):

                glutSolidSphere(obj.radius, obj.slices, obj.stacks)
            else:

                glutWireSphere(obj.radius, obj.slices, obj.stacks)

        elif(isinstance(obj, Cone)):
            
            if(obj.isSolid):

                glutSolidCone(obj.radius, obj.height, obj.slices, obj.stacks)
            else:

                glutWireCone(obj.radius, obj.height, obj.slices, obj.stacks)

        elif(isinstance(obj, Torus)):

            if(obj.isSolid):

                glutSolidTorus(obj.innerRadius, obj.outerRadius, obj.sides, obj.rings)
            else:

                glutWireTorus(obj.innerRadius, obj.outerRadius, obj.sides, obj.rings)
        glPopMatrix()
    
    glutSwapBuffers()

# Especifica o volume de visualização
def setViewParams():
    
    global fAspect, angle

    # Especifica o sistema de coordenadas de projeção
    glMatrixMode(GL_PROJECTION)

    # Inicializa sistema de coordenadas de projeção
    glLoadIdentity()

    # Especifica a projeção perspectiva
    gluPerspective(angle, fAspect, 0.1, 500)

    # Especifica sistema de coordenadas do modelo
    glMatrixMode(GL_MODELVIEW)

    # Inicializa sistema de coordenadas do modelo
    glLoadIdentity()

    # Especifica a posição do observador e do alvo
    gluLookAt(0,80,200,0,0,0,0,1,0)

# Callback chamada quando o tamanho da janela é alterado
def changeWindowSize(w, h):
    
    global fAspect

    # Previne a divisão por 0
    h = 1 if h == 0 else h

    # Especifica o tamanho da viewport
    glViewport(0, 0, w, h)

    # Calcula a correção de aspectro
    fAspect = w/h

    setViewParams()

# Menu de tipos
def menuType(choice):
    
    global isSolid

    # wireframe
    if(choice == 0):
        
        isSolid = False

    # solid
    elif (choice == 1):
        
        isSolid = True
    
    glutPostRedisplay()

    return 0

# Menu de cores
def menuColor(choice):
    
    global r, g, b

    # vermelho
    if(choice == 0):
        r = 1.0
        g = 0.0
        b = 0.0

    # verde
    elif (choice == 1):
        r = 0.0
        g = 1.0
        b = 0.0
    
    # azul
    elif(choice == 2):
        r = 0.0
        g = 0.0
        b = 1.0
    
    glutPostRedisplay()

    return 0

# Menu de formas
def menuShape(choice):

    # teapot
    if(choice == 0):
        drawTeapot()

    # cubo
    elif (choice == 1):
        drawCube()
    
    # esfera
    elif(choice == 2):
        drawShere()

    # cone
    elif(choice == 3):
        drawCone()
    
    # torus
    elif(choice == 4):
        drawTorus()

    glutPostRedisplay()

    return 0

# função que desenha um teapot
def drawTeapot():
    global objects, r, g, b, isSolid, posX, posY, posZ

    teapot = Teapot([r, g, b], isSolid, posX, posY, posZ, 50.0)
    objects.append(teapot)

# função que desenha um cubo
def drawCube():
    
    global objects, r, g, b, isSolid, posX, posY, posZ

    cube = Cube([r, g, b], isSolid, posX, posY, posZ, 50.0)
    objects.append(cube)

# função que desenha uma esfera
def drawShere():
    
    global objects, r, g, b, isSolid, posX, posY, posZ

    shere = Shere([r, g, b], isSolid, posX, posY, posZ, 50.0, 10, 10)
    objects.append(shere)

# função que desenha uma cone
def drawCone():

    global objects, r, g, b, isSolid, posX, posY, posZ

    cone = Cone([r, g, b], isSolid, posX, posY, posZ, 50.0, 100.0, 10, 10)
    objects.append(cone)

# função que desenha um torus
def drawTorus():

    global objects, r, g, b, isSolid, posX, posY, posZ

    torus = Torus([r, g, b], isSolid, posX, posY, posZ, 50.0, 20.0, 10, 10)
    objects.append(torus)

# Menu principal
def menuMain():
    pass

# Cria o menu
def menu():

    subMenuType = glutCreateMenu(menuType)
    glutAddMenuEntry("Wireframe", 0)
    glutAddMenuEntry("Solid", 1)

    subMenuColor = glutCreateMenu(menuColor)
    glutAddMenuEntry("Vermelho", 0)
    glutAddMenuEntry("Verde", 1)
    glutAddMenuEntry("Azul", 2)

    subMenuShape = glutCreateMenu(menuShape)
    glutAddMenuEntry("Teapot", 0)
    glutAddMenuEntry("Cubo", 1)
    glutAddMenuEntry("Esfera", 2)
    glutAddMenuEntry("Cone", 3)
    glutAddMenuEntry("Torus", 4)

    menu = glutCreateMenu(menuMain)
    glutAddSubMenu("Tipos", subMenuType)
    glutAddSubMenu("Cores", subMenuColor)
    glutAddSubMenu("Formas", subMenuShape)

    glutAttachMenu(GLUT_RIGHT_BUTTON)

    return 0

# Trata os eventos do mouse
def mouseHandler(button, state, x, y):

    if(button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN):

        menu()
    
    glutPostRedisplay()

# callback chamada sempre que o mouse é movimentado sobre a janela GLUT
def getMousePosition(x, y):

    global posX, posY, posZ

    modelView = glGetDoublev(GL_MODELVIEW_MATRIX)
    projection = glGetDouble(GL_PROJECTION_MATRIX)
    viewPort = glGetInteger(GL_VIEWPORT)

    winX = x
    winY = viewPort[3] - y
    winZ = glReadPixels(x, int(winY), 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT, None)
    posX, posY, posZ = gluUnProject(winX, winY, winZ, modelView, projection, viewPort)

def init():

    glClearColor(0.0, 0.0, 0.0, 1.0)

def main():

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1024, 768)
    glutInitWindowPosition(20,20)
    glutCreateWindow("Projeto Final")
    glutDisplayFunc(draw)
    glutReshapeFunc(changeWindowSize)
    glutPassiveMotionFunc(getMousePosition)
    glutMouseFunc(mouseHandler)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main() 