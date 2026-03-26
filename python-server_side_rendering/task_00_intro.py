import os

def generate_invitations(template, attendees):
    # 1. Vérification des types d'entrée
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # 2. Gestion des entrées vides
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Traitement de chaque invité
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Liste des placeholders à remplacer
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            # On récupère la valeur. Si elle est None ou absente, on met "N/A"
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # Remplacement dans le texte
            target = "{" + key + "}"
            processed_template = processed_template.replace(target, str(value))
        
        # 4. Génération du fichier de sortie
        filename = f"output_{index}.txt"
        
        # Optionnel : vérifier si le fichier existe déjà
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists. Overwriting...")

        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")