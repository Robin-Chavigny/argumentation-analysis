import csv
import time
from openai import OpenAI

client = OpenAI()

dataset = "C:/Users/robin/Documents/Stage Japon/argumentation-analysis/python/result_svm_aaf.csv"

try:
    with open(dataset, 'r+', newline='', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)
        # Stocker toutes les lignes du fichier dans une liste
        lignes = list(lecteur_csv)
        l=0
        for ligne in lignes[1:]:
            l=l+1
            print('ligne ',l)
            relation = ligne[2]
            context = ligne[4]
            sentences1 = ligne[5]
            sentences2 = ligne[6]
            speaker1 = ligne[7]
            speaker2 = ligne[8]
            topic = ligne[9]

            # Construire le message de l'utilisateur
            user_content = f"""Context: {context}

Argument 1: {sentences1}
Speaker 1: {speaker1}

Argument 2: {sentences2}
Speaker 2: {speaker2}

Topic: {topic}
Relation: {relation}"""

            try:
                completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You will be given two arguments, the context in which these arguments are taking place, and the relation they are in. Your goal is to explain the type of relation."},
                        {"role": "user", "content": user_content}
                    ]
                )
                ligne[3] = completion.choices[0].message.content
            except Exception as e:
                print(f"Erreur lors de l'appel à l'API : {e}")
                ligne[3] = "Erreur API"
            
            # Pause pour éviter de dépasser les limites de taux
            time.sleep(1)

        # Revenir au début du fichier et réécrire les données mises à jour
        fichier_csv.seek(0)
        writer = csv.writer(fichier_csv)
        writer.writerows(lignes)
        fichier_csv.truncate()

except FileNotFoundError:
    print(f"Le fichier {dataset} n'a pas été trouvé. Vérifie le chemin du fichier.")
