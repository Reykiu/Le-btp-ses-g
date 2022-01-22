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
''' Determine les informations de la facade, la porte le toit(couleur, forme, emplacement)'''
    reponse = {}
    couleur = ''
    if random.randint(0, 3) == 0:
        couleur = 'red'
    elif random.randint(0, 3) == 1:
        couleur = 'blue'
    elif random.randint(0, 3) == 2:
        couleur = 'green'
    elif random.randint(0, 3) == 3:
        couleur = 'yellow'
    reponse['couleur_facade'] = couleur
    reponse['couleur_porte'] = 'brown'
    reponse['couleur_toit'] = 'black'
    reponse['numero'] = numero
    reponse['hauteur_batiment'] = random.choice([160, 240, 320, 400, 480])
    return reponse
 
# Fonctions d'interface graphique
 
def dessiner_facade(informations):
'''Dessine la facade avec les informations contenu dans la fonction determiner_immeuble(numero)'''
    facade = {}
    facade['écriture'] = 'black'
    facade['fond'] = informations['couleur_facade']
    facade['épaisseur'] = 2
    hauteur_batiment = random.choice([160, 240, 320, 400, 480])
    x = informations['numero']*180 - 300
    y = informations['numero'] * 0
    cc.rectangle(140, informations['hauteur_batiment'], facade, (x,y))
    
def dessiner_porte(informations):
'''Dessine la porte avec les informations contenu dans la fonction determiner_immeuble(numero)'''
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
'''Dessine le toit avec les informations contenu dans la fonction determiner_immeuble(numero)'''
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
    
def dessiner_fenetre(informations):
    fenetre = {}
    h = 20 
    t = 0
    fenetre['ecriture'] =='black'
    fenetre['fond'] = informations['couleur_fenetre']
    fenetre['epaisseur'] = 2
    taille_batiment = informations['numero'] * 180 -300
    for d in range(100):
        while h < hauteur_batiment:
            while t < 140:
                x = informations['numero'] * 180 - 300 + t
                y = informations['numero'] * 0
                cc.carre(30, fenetre, (x, y))
                t = t + 10
        
        
    
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
