#projet d'Hugo, Sullyvan et Mathias

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
    reponse = {}
    reponse['couleur_facade'] = 'red'
    reponse['couleur_porte'] = 'brown'
    reponse['couleur_toit'] = 'lime'
    reponse['numero'] = numero
    reponse['hauteur_batiment'] = random.choice([160, 240, 320, 400, 480])
    return reponse
 
# Fonctions d'interface graphique
 
def dessiner_facade(informations):
    facade = {}
    facade['écriture'] = 'black'
    facade['fond'] = informations['couleur_facade']
    facade['épaisseur'] = 2
    hauteur_batiment = random.choice([160, 240, 320, 400, 480])
    x = informations['numero']*180 - 300
    y = informations['numero']*0
    cc.rectangle(140, informations['hauteur_batiment'], facade, (x,y))
    
def dessiner_porte(informations):
    porte = {}
    porte['écriture'] = 'black'
    porte['fond'] = informations['couleur_porte']
    porte['épaisseur'] = 2
    taille_batiment = informations['numero']*180
    distance_porte = random.choice([300,245,190])
    x = taille_batiment - distance_porte
    y = informations['numero'] * 0
    cc.rectangle(30, 50, porte, (x,y))
    
def dessiner_toit(informations):
    toit = {}
    toit['écriture'] = 'black'
    toit['fond'] = informations['couleur_toit']
    toit['épaisseur'] = 2
    taille_batiment = informations['numero']*180 - 300
    forme_toit = random.randint(0, 1)
    x = taille_batiment
    y = informations['hauteur_batiment']
    if forme_toit == 0:
        cc.triangle(140, 180,toit, (x,y))
    else:
        cc.arc_de_cercle(-70, 180, toit, (x,y))
    
def dessiner_immeuble(informations:dict):
    dessiner_facade(informations)
    dessiner_porte(informations)
    dessiner_toit(informations)
    
def stockX(numero):
    '''Prends la clé 'numero' dans le dictionnaire reponse de la fonction determiner_immeuble'''
    x0 = numero * 200 - 200
    y0 = 0
    return (x0, y0)
    
# Programme principal
 
for x in range(4):
    informations = determiner_immeuble(x)
    dessiner_immeuble(informations
