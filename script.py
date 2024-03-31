import os

def ouvrir_invite_commande():
    if os.name == "nt":  # Vérifie si le système d'exploitation est Windows
        os.system("cmd")  # Ouvre l'invite de commande Windows
    else:
        os.system("bash")  # Ouvre l'invite de commande bash pour les autres systèmes

if __name__ == "__main__":
    ouvrir_invite_commande()