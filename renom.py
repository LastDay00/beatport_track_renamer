import os
from tinytag import TinyTag, TinyTagException
import re

# Chemin du dossier contenant les fichiers musicaux
dossier_musique = '/Users/xxx/Downloads/Music'

# Parcourir tous les fichiers dans le dossier et sous-dossiers
for root, dirs, files in os.walk(dossier_musique):
    for filename in files:
        if filename.endswith((".mp3", ".aiff", ".wav")):
            chemin_complet = os.path.join(root, filename)
            try:
                tag = TinyTag.get(chemin_complet)
                
                # Vérifier que l'audio a bien les métadonnées nécessaires
                if tag.artist and tag.title:
                    # Créer le nouveau nom
                    nouveau_nom = f"{tag.artist.replace(' ', '_')}__{tag.title.replace(' ', '_')}{os.path.splitext(filename)[1]}"
                    # Remplacer les caractères non autorisés
                    nouveau_nom = nouveau_nom.replace("/", "-").replace("\\", "-").replace(":", "-").replace("*", "-").replace("?", "-").replace('"', "-").replace("<", "-").replace(">", "-").replace("|", "-")
                    nouveau_chemin = os.path.join(root, nouveau_nom)

                    # Renommer le fichier
                    os.rename(chemin_complet, nouveau_chemin)
                else:
                    # Vérifier si le nom du fichier commence par 2 chiffres suivis d'un underscore, ou s'il contient une longue séquence d'underscores
                    if re.match(r'^\d{2}_', filename) or '_____________________________' in filename:
                        # Créer le nouveau nom en supprimant les 2 chiffres et l'underscore ou la longue séquence d'underscores
                        nouveau_nom = re.sub(r'^\d{2}_', '', filename).replace('_____________________________', '')
                        nouveau_chemin = os.path.join(root, nouveau_nom)

                        # Renommer le fichier
                        os.rename(chemin_complet, nouveau_chemin)
            except TinyTagException:
                print(f"Impossible de lire le fichier : {chemin_complet}")
