import argparse
import logging

logging.basicConfig(filename='fichier_de.log', level=logging.DEBUG)

parser = argparse.ArgumentParser()
    
# Arguments obligatoire
parser.add_argument("temps", type=int, help="informer la duree en minutes")
parser.add_argument("nom", help="indiquer le nom du fichier de sortie")
parser.add_argument("format", choices=['M3U', 'XSPF', 'PLS'], help=("Choisir entre le format M3U et XSPF"))

# Arguments optionnel
parser.add_argument("-g", "--genre", nargs=2, help="indiquer le genre")
parser.add_argument("-a", "--artiste", nargs=2, help="indiquer l'artiste")
parser.add_argument("-A", "--album", nargs=2, help="indiquer l'album")
parser.add_argument("-t", "--titre", help="indiquer le titre")

args=parser.parse_args()

# On affiche les arguments obligatoire
logging.info(args.temps)
logging.info(args.nom)
logging.info(args.format)

# Fonction pour controler si les arguments sont correctement renseigner 
def verifArguments(arg, nomArg):
    try:
        int(arg[1])
        if int(arg[1]) > 0 and int(arg[1]) <= 100: 
            logging.info(str(int(arg[1])))
            setattr(agrs,nomArg, [arg[0],nb])
            return True
            logging.error('Veuillez recommencer')
    except ValueError:
        logging.error('Veuillez saisir un entier')

if args.genre:
    logging.info('Genre : ' +args.genre[0])
    logging.info('Temps : ' +args.genre[1])

if args.artiste:
    logging.info('Artiste : ' +args.artiste[0])
    logging.info('Temps : ' +args.artiste[1])

if args.album:
    logging.info('Album : ' +args.album[0])
    logging.info('Temps : ' +args.album[1])
    
#variable de poucentage

#pourcentage = args.temps-(1-args.genre[1]/100)
