import csv

def fn_question(question):
    return input(question)

def fn_encode(gamename, gameeditor, gamegenre, gamereleasedate, gameplatforms, gamereviews):
    file_csv = "jeux_du_grenier.csv"
    with open(file_csv,"w",encoding="utf-8", newline="") as fichier:
        header = ["Nom du jeu", "Editeur du jeu", "Genre du jeu", "Date de sortie du jeu", "Plateforme", "(Critique /100) du jeu"]
        data = [gamename, gameeditor, gamegenre, gamereleasedate, gameplatforms, gamereviews]
        writer = csv.writer(fichier)
        writer.writerow(header)
        writer.writerow(data)

q_gamename = "Entrez le nom du jeu : "
gamename = fn_question(q_gamename)
q_gameeditor = "Entrez l'editeur du jeu : "
gameeditor = fn_question(q_gameeditor)
q_gamegenre = "Entrez le genre du jeu : "
gamegenre = fn_question(q_gamegenre)
q_gamereleasedate = "Entrez la date de sortie du jeu : "
gamereleasedate = int(fn_question(q_gamereleasedate))
q_gameplatforms = "Entrez la plateforme utilisée : "
gameplatforms = fn_question(q_gameplatforms)
q_gamereviews = "Entrez la note du jeu (sur 100) : "
gamereviews = int(fn_question(q_gamereviews))

def fn_oldschool(gamereleasedate):
    if gamereleasedate < 2006:
        return True
    else:
        False

if fn_oldschool(gamereleasedate):
    True
    print("Le jeu", gamename,"est oldschool")
else:
    print("Le jeu", gamename,"n'est pas oldschool")

def fn_oldschool(gamereviews):
    if gamereviews <= 80:
        return True
    else:
        False

if fn_oldschool(gamereviews):
    True
    print("Le jeu", gamename,"provient et reviendra a la poubelle mais n'est pas aussi merdique que League Of Legends")
else:
    print("Le jeu", gamename,"n'est pas aussi bon que Super Mario Galaxy")

fn_encode(gamename, gameeditor, gamegenre, gamereleasedate, gameplatforms, gamereviews)