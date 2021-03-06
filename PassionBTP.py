#projet de Mathias, Sullyvan, Hugo

# Importation   
from dessin import codecache as cc
import random
from dessin.codecache import rectangle
from dessin.codecache import rectangle2
from dessin.codecache import triangle
from dessin.codecache import arc_de_cercle
from dessin.codecache import carre
  
 
# Fonction gestion des données
def determiner_immeuble(numero):
    '''Détermine les informations de chaque immeuble grace à leur numéro'''
    reponse = {}
  
    #Définit aléatoirement la couleur de la facade
    couleur_facade = random.randint(0, 14)
    if couleur_facade == 0:
        couleur_facade = 'darkorchid'
    elif couleur_facade == 1:
        couleur_facade = 'darksalmon'
    elif couleur_facade == 2:
        couleur_facade = 'mediumaquamarine'
    elif couleur_facade == 3:
        couleur_facade = 'wheat'
    elif couleur_facade == 4:
        couleur_facade = 'aqua'
    elif couleur_facade == 5:
        couleur_facade = 'peru'
    elif couleur_facade == 6:
        couleur_facade = 'palegreen'
    elif couleur_facade == 7:
        couleur_facade = 'darkslategrey'
    elif couleur_facade == 8:
        couleur_facade = 'olivedrab'
    elif couleur_facade == 9:
        couleur_facade = 'paleturquoise'
    elif couleur_facade == 10:
        couleur_facade = 'firebrick'
    elif couleur_facade == 11:
        couleur_facade = 'deeppink'
    elif couleur_facade == 12:
        couleur_facade = 'khaki'
    elif couleur_facade == 13:
        couleur_facade = 'dimgrey'
    elif couleur_facade == 14:
        couleur_facade = 'cadetblue'
      
    reponse['couleur_facade'] = couleur_facade
    #Définit aléatoirement la couleur de la porte
    couleur_porte = random.randint(0, 14)
    if couleur_porte == 0:
        couleur_porte = 'darkorchid'
    elif couleur_porte == 1:
        couleur_porte = 'darksalmon'
    elif couleur_porte == 2:
        couleur_porte = 'mediumaquamarine'
    elif couleur_porte == 3:
        couleur_porte = 'wheat'
    elif couleur_porte == 4:
        couleur_porte = 'aqua'
    elif couleur_porte == 5:
        couleur_porte = 'peru'
    elif couleur_porte == 6:
        couleur_porte = 'palegreen'
    elif couleur_porte == 7:
        couleur_porte = 'darkslategrey'
    elif couleur_porte == 8:
        couleur_porte = 'olivedrab'
    elif couleur_porte == 9:
        couleur_porte = 'paleturquoise'
    elif couleur_porte == 10:
        couleur_porte = 'firebrick'
    elif couleur_porte == 11:
        couleur_porte = 'deeppink'
    elif couleur_porte == 12:
        couleur_porte = 'khaki'
    elif couleur_porte == 13:
        couleur_porte = 'dimgrey'
    elif couleur_porte == 14:
        couleur_porte = 'cadetblue'
      
    reponse['couleur_porte'] = couleur_porte
    #Définit aléatoirement la couleur de la toit
    couleur_toit = random.randint(0, 14)
    if couleur_toit == 0:
        couleur_toit = 'darkorchid'
    elif couleur_toit == 1:
        couleur_toit = 'darksalmon'
    elif couleur_toit == 2:
        couleur_toit = 'mediumaquamarine'
    elif couleur_toit == 3:
        couleur_toit = 'wheat'
    elif couleur_toit == 4:
        couleur_toit = 'aqua'
    elif couleur_toit == 5:
        couleur_toit = 'peru'
    elif couleur_toit == 6:
        couleur_toit = 'palegreen'
    elif couleur_toit == 7:
        couleur_toit = 'darkslategrey'
    elif couleur_toit == 8:
        couleur_toit = 'olivedrab'
    elif couleur_toit == 9:
        couleur_toit = 'paleturquoise'
    elif couleur_toit == 10:
        couleur_toit = 'firebrick'
    elif couleur_toit == 11:
        couleur_toit = 'deeppink'
    elif couleur_toit == 12:
        couleur_toit = 'khaki'
    elif couleur_toit == 13:
        couleur_toit = 'dimgrey'
    elif couleur_toit == 14:
        couleur_toit = 'cadetblue'
    reponse['couleur_toit'] = couleur_toit
    
    reponse['numero'] = numero
    reponse['hauteur_batiment'] = random.choice([160, 240, 320, 400, 480])  #Definit aléatoirement la hauteur en pixel du batiment
    return reponse
 
# Fonctions d'interface graphique
 
def dessiner_facade(informations):
    '''Fonction servant à dessiner la façade des batiments'''
    facade = {}  #Stock les differentes informations dans un tuple
    facade['écriture'] = 'black'
    facade['fond'] = informations['couleur_facade']
    facade['épaisseur'] = 2
    x = informations['numero'] * 180 - 300
    y = informations['numero'] * 0 - 250
    cc.rectangle(140, informations['hauteur_batiment'], facade, (x,y))
    
def dessiner_porte(informations):
    '''Fonction servant à dessiner la porte des batiments'''
    porte = {}  #Stock les differentes informations dans un tuple
    porte['écriture'] = 'black'
    porte['fond'] = informations['couleur_porte']
    porte['épaisseur'] = 2
    taille_batiment = informations['numero']*180
    distance_porte = random.choice([300,245,190])
    x = taille_batiment - distance_porte
    y = informations['numero'] * 0 - 250
    cc.rectangle(30, 50, porte, (x,y))
    
def dessiner_toit(informations):
    '''Fonction servant à dessiner le toit des batiments'''
    toit = {}  #Stock les differentes informations dans un tuple
    toit['écriture'] = 'black'
    toit['fond'] = informations['couleur_toit']
    toit['épaisseur'] = 2
    taille_batiment = informations['numero']*180 - 300
    forme_toit = random.randint(0, 1)  #Tire aléatoirement la forme du toit
    x = taille_batiment - 1
    y = informations['hauteur_batiment'] - 250
    if forme_toit == 0:
        cc.triangle(141, 100,toit, (x,y))
    else:
        cc.arc_de_cercle(-71, 180, toit, (x,y))
    
        
def dessiner_fenetre(informations):
    '''Fonction servant à dessiner les fenetres des batiments'''
    fenetre = {}  #Stock les differentes informations dans un tuple
    fenetre['écriture'] = 'black'
    fenetre['fond'] = 'skyblue'
    fenetre['épaisseur'] = 2
    taille_batiment = informations['numero']*180 - 300  #Vas rechercher l'information "numero" dans "determiner_immeuble
    hauteur_batiment = informations['hauteur_batiment']  #Vas rechercher l'information "hauteur_batiment" dans "determiner_immeuble
    if hauteur_batiment == 160: #S'execute si la façade fais 160 pixels de haut
        h = 60
        for x in range(2):
            x = taille_batiment
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 55
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 110
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            h = h + 60
    if hauteur_batiment == 240: #S'execute si la façade fais 240 pixels de haut
        h = 65
        for x in range(3):
            x = taille_batiment
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 55
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 110
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            h = h + 65
    if hauteur_batiment == 320: #S'execute si la façade fais 320 pixels de haut
        h = 60
        for x in range(5):
            x = taille_batiment
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 55
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 110
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            h = h + 55
    if hauteur_batiment == 400: #S'execute si la façade fais 400 pixels de haut
        h = 60
        for x in range(6):
            x = taille_batiment
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 55
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 110
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            h = h + 60
    if hauteur_batiment == 480: #S'execute si la façade fais 480 pixels de haut
        h = 60
        for x in range(8):
            x = taille_batiment
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 55
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 110
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            h = h + 55
        
def dessiner_immeuble(informations:dict):
    '''Fonction qui vas servir à executer les differentes fonctions de dessin dans l'ordre (façade -> porte -> toit -> fenetre) afin de dessiner les batiments'''
    dessiner_facade(informations)
    dessiner_porte(informations)
    dessiner_toit(informations)
    dessiner_fenetre(informations)
 
# Fonctions d'interface graphique
 
def dessiner_facade(informations):
    '''Fonction servant à dessiner la façade des batiments'''
    facade = {}  #Stock les differentes informations dans un tuple
    facade['écriture'] = 'black'
    facade['fond'] = informations['couleur_facade']
    facade['épaisseur'] = 2
    x = informations['numero'] * 180 - 300
    y = informations['numero'] * 0 - 250
    cc.rectangle(140, informations['hauteur_batiment'], facade, (x,y))
    
def dessiner_porte(informations):
    '''Fonction servant à dessiner la porte des batiments'''
    porte = {}  #Stock les differentes informations dans un tuple
    porte['écriture'] = 'black'
    porte['fond'] = informations['couleur_porte']
    porte['épaisseur'] = 2
    taille_batiment = informations['numero']*180
    distance_porte = random.choice([300,245,190])
    x = taille_batiment - distance_porte
    y = informations['numero'] * 0 - 250
    cc.rectangle(30, 50, porte, (x,y))
    
def dessiner_toit(informations):
    '''Fonction servant à dessiner le toit des batiments'''
    toit = {}  #Stock les differentes informations dans un tuple
    toit['écriture'] = 'black'
    toit['fond'] = informations['couleur_toit']
    toit['épaisseur'] = 2
    taille_batiment = informations['numero']*180 - 300
    forme_toit = random.randint(0, 1)  #Tire aléatoirement la forme du toit
    x = taille_batiment - 1
    y = informations['hauteur_batiment'] - 250
    if forme_toit == 0:
        cc.triangle(141, 100,toit, (x,y))
    else:
        cc.arc_de_cercle(-71, 180, toit, (x,y))
        
def dessiner_fenetre(informations):
    '''Fonction servant à dessiner les fenetres des batiments'''
    fenetre = {}  #Stock les differentes informations dans un tuple
    fenetre['écriture'] = 'black'
    fenetre['fond'] = 'skyblue'
    fenetre['épaisseur'] = 2
    taille_batiment = informations['numero']*180 - 300  #Vas rechercher l'information "numero" dans "determiner_immeuble
    hauteur_batiment = informations['hauteur_batiment']  #Vas rechercher l'information "hauteur_batiment" dans "determiner_immeuble
    if hauteur_batiment == 160: #S'execute si la façade fais 160 pixels de haut
        h = 60
        for x in range(2):
            x = taille_batiment
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 55
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 110
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            h = h + 60
    if hauteur_batiment == 240: #S'execute si la façade fais 240 pixels de haut
        h = 65
        for x in range(3):
            x = taille_batiment
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 55
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 110
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            h = h + 65
    if hauteur_batiment == 320: #S'execute si la façade fais 320 pixels de haut
        h = 60
        for x in range(5):
            x = taille_batiment
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 55
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 110
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            h = h + 55
    if hauteur_batiment == 400: #S'execute si la façade fais 400 pixels de haut
        h = 60
        for x in range(6):
            x = taille_batiment
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 55
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 110
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            h = h + 60
    if hauteur_batiment == 480: #S'execute si la façade fais 480 pixels de haut
        h = 60
        for x in range(8):
            x = taille_batiment
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 55
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            x = taille_batiment + 110
            y = (hauteur_batiment * 0 + h) - 250
            cc.carre(30, fenetre, (x,y))
            h = h + 55
        
def dessiner_immeuble(informations:dict):
    '''Fonction qui vas servir à executer les differentes fonctions de dessin dans l'ordre (façade -> porte -> toit -> fenetre) afin de dessiner les batiments'''
    dessiner_facade(informations)
    dessiner_porte(informations)
    dessiner_toit(informations)
    dessiner_fenetre(informations)
    
# Programme principal
 
for x in range(4):
    '''Execution de la fonction dessiner_immeuble en boucle un nombre de fois définit dans le "range()"'''
    informations = determiner_immeuble(x)
    dessiner_immeuble(informations)
