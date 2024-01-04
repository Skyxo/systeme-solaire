from math import *
import bodys

add_library("peasycam")
add_library("controlP5")

width = 1820
height = 980

al = 9.461*10**15      # Valeur d'une année lumière
facteur = 10**8        # Facteur d'échelle
facteur_dessin = 1
objects_ = bodys.objects_

# Convertisseurs mètres -> unités
def m_to_u(d):
    return (d*facteur)/al

def settings():
    size(width, height, P3D)

    global pw
    pw = ParametersWindow()
    switches = '--sketch-path=' + sketchPath(), ''
    PApplet.runSketch(switches, pw)
    
# Initialisation de la fenêtre
def setup():
    global cam, objects_, xls
    this.surface.setTitle("Simulation")

    perspective(PI/3.0, float(width)/float(height), 0.001, 100000000)
    
    cam = PeasyCam(this, 1000)
    
# Caméra
x, y, z = 0, 0, 0                   # Position de la caméra
camera_velocity = 1                 # Vitesse de déplacement de la caméra
pov = 3                             # Point de vue
lock = True                         # Lock caméra

# Graphique
HUD = True                          # Affichage du HUD (texte)
pause = True                        # Pause
ref = False                         # référentiel choisi lors de l'affichage des trajectoires
focus = False                       # Se mettre à la place de la planète
showNames = True                    # Affichage des noms
traj = []                           # Affichage des trajectoires
dess = [i for i in range(len(objects_))]                           # Affichage des objets de la liste

#Trajectoires des objets
pos_objects_ = [[objects_[i].getColor()] for i in range(len(objects_))]
    
# Temps
step = 3600*4                       # Pas de temps entre les actualisations
time_total = 0                      # Temps total
increase_step_value = 1000          # Augmentation du pas de temps
precision = 100                     # Précision du calcul

alpha = 0

def draw():
    global x, y, z
    global HUD, lock, focus
    global step, time_total, precision, pause, pos_objects_, alpha
    
    background(0)
    
    # Contrôles
    if keyPressed:
        if key == 'z': # Haut
            cam.rotateX(-float(camera_velocity*PI/180))
        if key == 's': # Bas
            cam.rotateX(float(camera_velocity*PI/180))
        if key == 'q': # Gauche
            cam.rotateY(float(camera_velocity*PI/180))
        if key == 'd': # Droite
            cam.rotateY(-float(camera_velocity*PI/180))
        if key == 'a': # Gauche
            cam.rotateZ(float(camera_velocity*PI/180))
        if key == 'e': # Droite
            cam.rotateZ(-float(camera_velocity*PI/180))
        if key == ' ': # Zoom avant
            cam.setDistance(cam.getDistance()-camera_velocity*100)
        if keyCode == CONTROL: # Zoom arrière
            cam.setDistance(cam.getDistance()+camera_velocity*100)
        if keyCode == UP: # Augmenter le pas de temps
                step += increase_step_value
        if keyCode == DOWN: # Réduire le pas de temps
                step = step-increase_step_value if step-increase_step_value > precision else precision
        if keyCode == RIGHT: # Augmenter la précision
            precision = precision+1 if precision < step-1 else step
        if keyCode == LEFT: # Réduire la précision
            precision = precision-1 if precision > 1 else 1
    
    # Actualise les astres
    if not pause:
        #m1 = (objects_[1].getY()-objects_[0].getY())/(objects_[1].getX()-objects_[0].getX()) # Coeff directeur de la droite Soleil-Terre à l'instant T
        i = 0
        newstep = step/precision
        while i <= step:
            for object in objects_:
                object.calculNewPos(newstep) # Calcul de la nouvelle position
            i+=newstep
        #m2 = (objects_[1].getY()-objects_[0].getY())/(objects_[1].getX()-objects_[0].getX()) # Coeff directeur de la droite Soleil-Terre à l'instant T+1
        #alpha += atan(abs((m2-m1)/(1+m1*m2))) # Angle de révolution
        
        time_total+=step
        
        for j in range(len(objects_)):
            pos_objects_[j].append((objects_[j].getX(), objects_[j].getY(), objects_[j].getZ()))
        
    if lock:
        x = -m_to_u(objects_[pov].getX())
        y = -m_to_u(objects_[pov].getY())
        z = -m_to_u(objects_[pov].getZ())
            
    translate(x, y, z)  
    
    for i in dess: # Affiche les corps
        
        push()
        translate(m_to_u(objects_[i].getX()), m_to_u(objects_[i].getY()), m_to_u(objects_[i].getZ()))
        strokeWeight(2)
        stroke(objects_[i].getColor()[0], objects_[i].getColor()[1], objects_[i].getColor()[2])  
        rotateZ(radians(objects_[i].getEquInclination()))
        line(0, -m_to_u(objects_[i].getRadius())*facteur_dessin*3, 0, 0, m_to_u(objects_[i].getRadius())*facteur_dessin*3, 0)
        
        rotateY(radians(objects_[i].getRotation()))
        stroke(0)
        strokeWeight(0.1)
        fill(objects_[i].getColor()[0], objects_[i].getColor()[1], objects_[i].getColor()[2])
        sphere(m_to_u(objects_[i].getRadius())*2*facteur_dessin)
        
        """
        rotateZ(-radians(objects_[i].getEquInclination()))
        stroke(0, 255, 0)  
        line(m_to_u(objects_[i].getRadius())*cos(radians(90-objects_[i].getEquInclination()))*facteur_dessin*3, 
             -m_to_u(objects_[i].getRadius())*sin(radians(90-objects_[i].getEquInclination()))*facteur_dessin*3, 
             0,
             -m_to_u(objects_[i].getRadius())*cos(radians(90-objects_[i].getEquInclination()))*facteur_dessin*3, 
             m_to_u(objects_[i].getRadius())*sin(radians(90-objects_[i].getEquInclination()))*facteur_dessin*3, 
             0)
        """
        pop()
        
        if showNames:
            push()
            translate(m_to_u(objects_[i].getX()), m_to_u(objects_[i].getY()), m_to_u(objects_[i].getZ()))
            textAlign(CENTER)
            noStroke()
            fill(objects_[i].getColor()[0], objects_[i].getColor()[1], objects_[i].getColor()[2])
            a = sqrt(((-x+cam.getPosition()[0])-m_to_u(objects_[i].getX()))**2 + ((-y+cam.getPosition()[1])-m_to_u(objects_[i].getY()))**2 + ((-z+cam.getPosition()[2])-m_to_u(objects_[i].getZ()))**2)
            textSize((cam.getDistance()+a)/50)
            rotateX(cam.getRotations()[0])
            rotateY(cam.getRotations()[1])
            rotateZ(cam.getRotations()[2])
            text("{}".format(objects_[i].getName()), 0, -m_to_u(objects_[i].getRadius())*2.5*facteur_dessin)    
            pop()
                
    # Trace les trajectoires
    afficheTrajectoire(pos_objects_, ref)
        
    #if alpha >= PI:
    #    pause = True
    
    gui()
    
class ParametersWindow(PApplet):
    
    def settings(p): p.size(len(objects_)*50, 300)

    def setup(p):
        global showNames
        p.surface.setTitle("Parametres")
        
        p.settings()
        
        cp = ControlP5(p)
        
        for i in range(len(objects_)):
            cp.addButton(objects_[i].getName())\
            .setPosition(50*i, 0)\
            .setSize(50, 50)\
            .setValue(i)\
            .onClick(ChangePOV)
            
            cp.addToggle(str(i))\
            .setPosition(15+50*i, 70)\
            .setSize(20, 20)\
            .onClick(SelectTraj)
        
        cp.addButton("Switch Ref")\
        .setPosition(10, 120)\
        .setSize(60, 40)\
        .onClick(SwitchRef)
        
        cp.addButton("Clear Paths")\
        .setPosition(80, 120)\
        .setSize(60, 40)\
        .onClick(ClearPaths)
        
        cp.addButton("Exit")\
        .setPosition(150, 120)\
        .setSize(60, 40)\
        .onClick(Exit)
        
        cp.addToggle("Names")\
        .setPosition(15, 250)\
        .setSize(30, 30)\
        .setValue(showNames)\
        .onClick(ShowNames)
        
        cp.addToggle("HUD")\
        .setPosition(75, 250)\
        .setSize(30, 30)\
        .setValue(HUD)\
        .onClick(ShowHUD)
        
        cp.addToggle("Lock")\
        .setPosition(135, 250)\
        .setSize(30, 30)\
        .setValue(lock)\
        .onClick(Lock)
        
        cp.addToggle("Focus")\
        .setPosition(195, 250)\
        .setSize(30, 30)\
        .setValue(focus)\
        .onClick(Focus)
        
        cp.addToggle("Pause")\
        .setPosition(255, 250)\
        .setSize(30, 30)\
        .setValue(pause)\
        .onClick(Pause)
        
        cp.addTextfield("posx")\
        .setPosition(225, 120)\
        .setSize(100, 20)\
        .setValue(str(objects_[pov].getX()))\
        .setFont(createFont("arial", 12))\
        .setLabel("PosX")\
        .setAutoClear(False)
        
        cp.addTextfield("posy")\
        .setPosition(340, 120)\
        .setSize(100, 20)\
        .setValue(str(objects_[pov].getY()))\
        .setFont(createFont("arial", 12))\
        .setLabel("PosY")\
        .setAutoClear(False)
        
        cp.addTextfield("posz")\
        .setPosition(455, 120)\
        .setSize(100, 20)\
        .setValue(str(objects_[pov].getZ()))\
        .setFont(createFont("arial", 12))\
        .setLabel("PosZ")\
        .setAutoClear(False)
        
        """
        cp.addButton("Submit")\
        .setPosition(570, 120)\
        .setSize(60, 40)\
        .onClick(Submit)
        """
        
    def draw(p):
        p.background(0)
    
def gui(): # Affichage du texte (HUD)
    
    cam.beginHUD()
    translate(width/2, height/2)
    fill(255)
    stroke(0)
    if HUD:
        textSize(20)
        textAlign(CENTER)
        text("Temps ecoule: {}j".format(round(float(time_total)/3600/24,2)), 0, height/2-20)
        #text("Rotation: {} degres".format(round(alpha*180/PI,2)), 0, height/2-50)
        
        textAlign(LEFT)
        text("Intervalle: {}".format(round(float(step)/float(precision), 2)), -width/2+20, height/2-20)
        text("Pas de temps: {}s".format(step), -width/2+20, height/2-50)
        text("Precision : {}".format(precision), -width/2+20, height/2-80)
        text(objects_[pov].getInfo(),-width/2+20,-height/2+40)
        
        textAlign(RIGHT) 
        text("Vitesse de deplacement camera: {}".format(camera_velocity), width/2-20, height/2-20) 
        text("x: {} y: {} z: {}".format(round(x), round(y), round(z)), width/2-20, height/2-50) 
        text("Pov {} ({})".format(objects_[pov].getName(), 'Lock' if lock else 'Unlock'), width/2-20, height/2-80) 
        text("{}".format("PAUSE" if pause else ""), width/2-20, -height/2+70)
    
    textAlign(RIGHT)
    text("{}fps".format(round(frameRate, 1)), width/2-20, -height/2+40)
    
    cam.endHUD()

def keyPressed(): # Commande du clavier
    global facteur, camera_velocity
        
    if key == '+': # Augmenter le facteur affichage
        facteur*=1.2
    
    if key == '-': # Diminuer le facteur affichage
        facteur/=1.2
    
    if key == 'c': # Augmente la velocité de la caméra
        camera_velocity+=0.5
    
    if key == 'w': # Diminue la velocité de la caméra
        camera_velocity = camera_velocity-0.5 if camera_velocity > 0 else 0

def afficheTrajectoire(pos_objects_, ref): # Affiche la trajectoire des corps
    
    noFill()
    strokeWeight(1)
    for i in traj:
        beginShape()
        for o in range(1, len(pos_objects_[i])):
            stroke(pos_objects_[i][0][0], pos_objects_[i][0][1], pos_objects_[i][0][2])
            if ref:
                vertex(m_to_u(pos_objects_[i][o][0]+objects_[pov].getX()-pos_objects_[pov][o][0]), m_to_u(pos_objects_[i][o][1]+objects_[pov].getY()-pos_objects_[pov][o][1]), m_to_u(pos_objects_[i][o][2]+objects_[pov].getZ()-pos_objects_[pov][o][2]))
            else:
                vertex(m_to_u(pos_objects_[i][o][0]), m_to_u(pos_objects_[i][o][1]), m_to_u(pos_objects_[i][o][2]))
        endShape()

def SelectTraj(event):
    global traj

    if int(event.getController().getValue()) and int(event.getController().getName()) not in traj:
        traj.append(int(event.getController().getName()))
    elif not int(event.getController().getValue()) and int(event.getController().getName()) in traj:
        traj.remove(int(event.getController().getName()))
        
def ChangePOV(event):
    global pov
    pov = int(event.getController().getValue())
        
def SwitchRef(event):
    global ref
    ref = False if ref else True
    
def Focus(event):
    global dess 
    if int(event.getController().getValue()):
        cam.setDistance(0)
        try:
            dess.remove(objects_.index(objects_[pov]))
        except:
            pass
    else:
        cam.setDistance(1000)
        dess.append(objects_.index(objects_[pov]))
        
def Pause(event):
    global pause
    pause = event.getController().getValue()
        
def ShowNames(event):
    global showNames
    showNames = event.getController().getValue()
      
def Lock(event):
    global lock
    lock = event.getController().getValue()
       
def ClearPaths(event):
    global pos_objects_
    pos_objects_ = [[objects_[i].getColor()] for i in range(len(objects_))]
       
def ShowHUD(event):
    global HUD
    HUD = int(event.getController().getValue())
    
def Exit(event):
    global pw
    exit()
    pw.exit()
    
def Submit(event):
            
    print("the following text was submitted :")
    url1 = get(Textfield.class,"posx").getText()
    url2 = get(Textfield.class,"posy").getText()
    url3 = get(Textfield.class,"posz").getText()
    print(" textInput 1 = " + url1)
    print(" textInput 2 = " + url2) 
    print(" textInput 3 = " + url3)    
