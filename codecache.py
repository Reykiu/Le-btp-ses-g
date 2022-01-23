'''Ce fichier permet de dessiner deux formes à l'aide des deux fonctions suivantes
 
+ triangle(cote, infos, coordonnees)
+ arc_de_cercle(rayon, angle, infos, coordonnees)
 
Exemples d'utilisation :
>>> divers1 = {'écriture':'blue', 'fond':'#FF88FF', 'épaisseur':5}
>>> triangle(50, divers1, (50,100))
>>> arc_de_cercle(75, 360, divers1, (200,-200))
 
'''
 
# Importation
 
import turtle as trt
import random as rd
 
# Pas de classes
 
# Déclaration des fonctions qui ne sont pas dans l'interface-programmation
 
def nouveau_stylo(ecriture, fond, largeur):
    '''Renvoie la référence d'un stylo configuré
 
    :: param ecriture(str)  :: la couleur d'écriture ('red', '#FF0000')
    :: param fond(str)      :: la couleur de fond pour ce stylo
    :: param largeur(int)   :: la largeur du trait
    :: return (Turtle)      :: renvoie un objet de la classe Turtle
 
    '''
    feutre = trt.Turtle()
    feutre.color(ecriture)
    feutre.fillcolor(fond)
    feutre.pensize(largeur)
    feutre.speed(5)
    return feutre
 
def deplacer(feutre, x, y):
    '''Lève le feutre, déplace le feutre et abaisse le feutre
 
    :: param feutre(Turtle) :: la référence du crayon
    :: param x(int)         :: coordonnée horizontale (abscisse)
    :: param y(int)         :: coordonnée verticale (ordonnée)
    :: return (None)        :: c'est une fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    '''
    feutre.penup()       # On lève la pointe
    feutre.setpos(x, y)  # On déplace le crayon
    feutre.pendown()     # On abaisse la pointe
 
    
def trace_triangle(feutre, largeur, hauteur, x, y):
    feutre.begin_fill()
    feutre.goto(x+largeur, y)
    feutre.goto(x+largeur//2, y+hauteur)
    feutre.goto(x, y)
    feutre.end_fill()
    feutre.hideturtle()
    
def trace_carre(feutre, cote):
    feutre.begin_fill()
    for x in range(4):
        feutre.forward(cote)
        feutre.left(90)
    feutre.end_fill()
    feutre.hideturtle()
    
    
def trace_rectangle(feutre, largeur, hauteur):
    feutre.begin_fill()
    for x in range(2):
        feutre.forward(largeur)
        feutre.left(90)
        feutre.forward(hauteur)
        feutre.left(90)
    feutre.end_fill()
    feutre.hideturtle()
    
def trace_rectangle2(feutre, largeur, hauteur):
    feutre.begin_fill()
    for x in range(2):
        feutre.forward(largeur)
        feutre.left(90)
        feutre.forward(hauteur)
        feutre.left(90)
    feutre.end_fill()
    feutre.hideturtle()
    
def trace_arc(feutre, rayon, angle):
    '''Trace un arc de cercle à l'aide du crayon feutre
 
    :: param ftr(Turtle)    :: la référence du crayon
    :: param rayon(int)     :: la valeur en pixel du rayon
    :: param angle(int)     :: l'angle à tracer (360 pour un cercle)
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de ftr
 
    '''
    feutre.begin_fill()
    feutre.left(90)
    feutre.circle(rayon, angle)
    feutre.end_fill()
    feutre.hideturtle()
 
# Déclarations des fonctions d'interface-programmation
 
 
def arc_de_cercle(rayon, angle, infos, coordonnees):
    '''Trace un arc de triangle à partir des infos et aux bonnees coordonnées
 
    :: param rayon(int)                    :: la valeur en pixel du rayon
    :: param angle(int)                    :: la valeur en ° de l'angle
    :: param infos(dict)                   :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple (int,int) ) :: un tuple (x,y)
 
    '''
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_arc(feutre, rayon, angle)
 
    return feutre


def carre(cote, infos, coordonnees):
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
    
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_carre(feutre, cote)
    
    
def rectangle(largeur, hauteur, infos, coordonnees):
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
    
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_rectangle(feutre, largeur, hauteur)
    
    
def rectangle2(largeur, hauteur, infos, coordonnees):
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
    
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_rectangle2(feutre, largeur, hauteur)


def triangle(largeur, hauteur, infos, coordonnees):
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
    
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_triangle(feutre, largeur, hauteur, x, y)
    
    
 
# Programme principal
 
if __name__ == '__main__':
 
    divers1 = {'écriture':'blue', 'fond':'#FF88FF', 'épaisseur':5}
    arc_de_cercle(75, 180, divers1, (200,-200))
    
    divers2 = {'écriture':'black', 'fond':'blue', 'épaisseur':2}
    carre(30, divers2, (25,50))
    
    divers3 = {'écriture':'black', 'fond':'lime', 'épaisseur':2}
    rectangle(50, 100, divers3, (-120,100))

    divers4 = {'écriture':'black', 'fond':'#f8ff00', 'épaisseur':2}
    triangle(70, 80, divers4, (50,100))
    
    divers5 = {'écriture':'black', 'fond':'brown', 'épaisseur':2}
    rectangle2(30, 50, divers5, (100,100))
