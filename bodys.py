#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

# Création d'un corps
class Body():
    
    def __init__(self, name, distance, speed, inclination, equ_inclination, equ_speed, mass, radius, color, atractors):
        self.name = name
        try:
            self.posx, self.posy, self.posz = distance[0], distance[1], distance[2]
        except:
            self.posx, self.posy, self.posz = distance*cos(radians(inclination)), distance*sin(radians(inclination)), 0
        self.vx, self.vy, self.vz = speed[0], speed[1], speed[2]
        self.ax, self.ay, self.az = 0, 0, 0
        self.rotation = 0
        self.vrotation = equ_speed/radius
        self.m = mass
        self.r = radius
        self.color = color
        self.atractors = atractors
        self.inclination = inclination
        self.equ_inclination = equ_inclination
        self.equ_speed = equ_speed
        
    # Affichage des informations
    def getInfo(self):
        return "Informations de {} :\nAttracteur(s) : {}\na   = {} m.s-2 \nax = {} m.s-2 \nay = {} m.s-2 \naz = {} m.s-2 \nv = {} m.s-1 \nvx = {} m.s-1 \nvy = {} m.s-1 \nvz = {} m.s-1 \nx   = {} m \ny   = {} m\nz   = {}m".format( 
        self.getName(), 
        [(object.getName(), self.getDistance(object)) for object in self.getAtractors()],
        self.getA(),
        self.getAx(), 
        self.getAy(),
        self.getAz(),
        self.getV(),
        round(self.getVx()), 
        round(self.getVy()),
        round(self.getVz()),
        round(self.getX()), 
        round(self.getY()),
        round(self.getZ()))
                                                                                                            
    def getName(self):
        return self.name
    
    def getM(self):
        return self.m
    
    def getRadius(self):
        return self.r

    def getInclination(self):
        return self.inclination
    
    def getEquInclination(self):
        return self.equ_inclination
    
    def getEquSpeed(self):
        return self.equ_speed
    
    def getAtractors(self):
        return self.atractors
    
    def getColor(self):
        return self.color

    def getX(self):
        return self.posx
    
    def getY(self):
        return self.posy
    
    def getZ(self):
        return self.posz
    
    def getVx(self):
        return self.vx
    
    def getVy(self):
        return self.vy
    
    def getVz(self):
        return self.vz
            
    def getV(self):
        return sqrt(self.getVx()**2 + self.getVy()**2 + self.getVz()**2)
    
    def getAx(self):
        return self.ax
    
    def getAy(self):
        return self.ay
    
    def getAz(self):
        return self.az
    
    def getA(self):
        return sqrt(self.getAx()**2 + self.getAy()**2 + self.getAz()**2)
    
    def getRotation(self):
        return self.rotation
    
    def getVRotation(self):
        return self.vrotation
    
    def setX(self, dx):
        self.posx = dx
        
    def setY(self, dy):
        self.posy = dy
        
    def setZ(self, dz):
        self.posz = dz
        
    def setVx(self, vx):
        self.vx = vx
        
    def setVy(self, vy):
        self.vy = vy
        
    def setVz(self, vz):
        self.vz = vz
    
    def setAx(self, ax):
        self.ax = ax
        
    def setAy(self, ay):
        self.ay = ay
        
    def setAz(self, az):
        self.az = az
        
    def setRotation(self, dr):
        self.rotation = dr
    
    def getDistance(self, object):
        return sqrt((self.getX()-object.getX())**2 + (self.getY()-object.getY())**2 + (self.getZ()-object.getZ())**2)
    
    def calculNewPos(self, t, G = 6.67*10**(-11)):
        
        Ax, Ay, Az = 0, 0, 0

        for object in self.getAtractors():
            champ = object.getM()*G/self.getDistance(object)**3
            Ax += champ*(object.getX()-self.getX())
            Ay += champ*(object.getY()-self.getY())
            Az += champ*(object.getZ()-self.getZ())
            
        self.setX((1/2)*Ax*(t**2) + self.getVx()*t + self.getX())
        self.setY((1/2)*Ay*(t**2) + self.getVy()*t + self.getY())
        self.setZ((1/2)*Az*(t**2) + self.getVz()*t + self.getZ())
        
        self.setVx(Ax*t + self.getVx())
        self.setVy(Ay*t + self.getVy())
        self.setVz(Az*t + self.getVz())
        
        self.setAx(Ax)
        self.setAy(Ay)
        self.setAz(Az)
        
        self.setRotation(self.getRotation()+float(self.getVRotation())*float(t))
        
"""
distance par rapport au foyer de la périapside = a(1-e)
vitesse au périapse : sqrt(((1+e)*mu)/(a(1-e)))

distance par rapport au foyer de l'apoapside = a(1+e)
vitesse à l'apoapse : sqrt(((1-e)*mu)/(a(1+e)))

avec mu, le paramètre gravitationnel standard (produit de la constante de gravitation G par la masse M du corps central).
"""

def getApoapse(a, e):
    return a*(1+e)

def getVApoapse(a, e, m, G = 6.67*10**(-11)):
    return sqrt(((1-e)*m.getM()*G)/(a*(1+e)))

def getThetaPrime(theta, distSunAttractor, distAttractor):
    theta*=PI/180 # Angle formé avec l'orbite de l'attracteur en radian
    
    dprime = sqrt((distSunAttractor+distAttractor*cos(theta))**2+(distAttractor*sin(theta))**2) # Distance Soleil-Lune
    
    thetaprime = asin((distAttractor*sin(theta)/dprime))*180/PI # Angle avec le soleil en degrés

    return thetaprime

objects_ = []
                
nligne = 1
with open('bodys_infos.csv', 'r') as csvfile:
    
    obj = csv.reader(csvfile, delimiter=';')

    for ligne in obj:
            
        if nligne > 2: # Cas des planètes
            
            attractors = tuple(map(int, ligne[9].split(',')))
            print(len(ligne[9]))
            if len(attractors) == 1: # Cas des planètes avec 1 attracteur
                        
                objects_.append(Body(ligne[0], 
                                    getApoapse(float(ligne[1]), float(ligne[2])),
                                    [0, 0, -getVApoapse(float(ligne[1]), float(ligne[2]), objects_[0])],
                                    float(ligne[3]),
                                    float(ligne[4]),
                                    float(ligne[5]), 
                                    float(ligne[6]),
                                    float(ligne[7])/float(2),
                                    tuple(map(int, ligne[8].split(','))),
                                    [objects_[int(ligne[9])]]))
    
            elif len(attractors) >= 2: # Cas des objets à >= 2 attracteurs
                
                objects_.append(Body(ligne[0], 
                                    objects_[attractors[0]].getDistance(objects_[attractors[1]])+getApoapse(float(ligne[1]), float(ligne[2])),
                                    [0, 0, -objects_[attractors[1]].getV()-getVApoapse(float(ligne[1]), float(ligne[2]), objects_[attractors[1]])],
                                    getThetaPrime(float(ligne[3]), objects_[attractors[0]].getDistance(objects_[attractors[1]]), getApoapse(float(ligne[1]), float(ligne[2]))),
                                    float(ligne[4]),
                                    float(ligne[5]), 
                                    float(ligne[6]),
                                    float(ligne[7])/float(2),
                                    tuple(map(int, ligne[8].split(','))),
                                    [objects_[obj] for obj in tuple(map(int, ligne[9].split(',')))] ))
                            
        elif nligne == 2: # Cas du soleil (astre central)
            objects_.append(Body(ligne[0], 
                [0, 0, 0], 
                [0, 0, 0], 
                0, 
                float(ligne[4]), 
                float(ligne[5]), 
                float(ligne[6]), 
                float(ligne[7])/float(2), 
                tuple(map(int, ligne[8].split(','))), 
                list(ligne[9])))
        
        nligne+=1

"""
Body(name, 
     distance, 
     speed, 
     inclination, 
     equ_inclination, 
     equ_speed, 
     mass, 
     radius, 
     color, 
     atractors)
"""

al = 9.461*10**15      # Valeur d'une année lumière
facteur = 10**8        # Facteur d'échelle

def u_to_m(d):
    return (d*al)/facteur

obj1 = Body("OBJ1", 
       [u_to_m(-500), 0, u_to_m(-10)], 
       [0, 0, 0], 
       0, 
       0, 
       0, 
       0, 
       u_to_m(8), 
       (255, 170, 100), 
       [objects_[0]])

#objects_.append(obj1)
