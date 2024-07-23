import csv
import time
from openai import OpenAI

client = OpenAI()

dataset = "C:/Users/robin/Documents/Stage Japon/argumentation-analysis/python/result_svm_aaf.csv"
filename = "result_svm_aaf_processed.csv"

try:
    with open(dataset, 'r', newline='', encoding='utf-8') as fichier_csv:
        with open(filename, mode='w', newline='') as file:
            lecteur_csv = csv.reader(fichier_csv)
            file.write('_unit_id$,$pair_id$,$relation_gold$,$relation_gold_reason$,$sentence_1$,$sentence_2$,$speaker_1$,$speaker_2$,$topic\n')
        
            # Stocker toutes les lignes du fichier dans une liste
            lignes = list(lecteur_csv)
            l=0
            for ligne in lignes[1:]:
                l=l+1
                li = ''
                for a in ligne:
                    li = li +','+a
                print('ligne ',l)
                lili = li.split('$,$')
                relation = lili[2]
                context = lili[4]
                sentences1 = lili[5]
                sentences2 = lili[6]
                speaker1 = lili[7]
                speaker2 = lili[8]
                topic = lili[9]

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

                    st = '$,$'.join(['0', '0', relation, completion.choices[0].message.content.replace('\n\n',' ').replace("’","'").replace("…","...").replace("“","''").replace("”","''").replace('\n',' '), sentences1, sentences2, speaker1, speaker2, topic])+ '\n'
                    file.write(st)
                    st = ''
                except Exception as e:
                    print(f"Erreur lors de l'appel à l'API : {e}")
            
                # Pause pour éviter de dépasser les limites de taux
                time.sleep(1)

            
            writer = csv.writer(file)

except FileNotFoundError:
    print(f"Le fichier {dataset} n'a pas été trouvé. Vérifie le chemin du fichier.")
