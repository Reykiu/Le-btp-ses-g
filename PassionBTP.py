# Importation   #HUGO , sully , mathias
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
    reponse['numero'] = numero
    reponse['nombre'] = random.randint(1, 5)
    return reponse
 
# Fonctions d'interface graphique
 
def dessiner_facade(informations):
    facade = {}
    facade['écriture'] = 'black'
    facade['fond'] = informations['couleur_facade']
    facade['épaisseur'] = 2
    x = informations['numero']*180 - 300
    y = informations['numero']*0
    rectangle(140, random.choice([160, 240, 320, 400, 480]), facade, (x,y))
    
def dessiner_porte(informations):
    porte = {}
    porte['écriture'] = 'black'
    porte['fond'] = informations['couleur_facade']
    porte['épaisseur'] = 2
    
def dessiner_immeuble(informations:dict):
    dessiner_facade(informations)
    
def stockX(numero):
    '''Prends la clé 'numero' dans le dictionnaire reponse de la fonction determiner_immeuble'''
    x0 = numero * 200 - 200
    y0 = 0
    return (x0, y0)
    
# Programme principal
 
for x in range(4):
    informations = determiner_immeuble(x)
    dessiner_immeuble(informations)







   
   
   
   
   
   
   
   
   
   
   
   
   
   
   Le rp ces geniale






Nékuva la salope









