# import de mes librairies
import csv
from bs4 import BeautifulSoup
import requests
import re

with open('saved_data.csv','w', newline='') as file :
    writer = csv.writer(file)
    headers = ['Nom','Prénom','Adresse','Téléphone','Email']
    writer.writerow(headers)

    for index in range(1,51):
        url = f'https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={index}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content,"html.parser")
        print(url)

        avocats = soup.find_all('div', class_='callout secondary annuaire-single')

        for avocat in avocats :
            chaine = avocat.find('h3',class_='nom-prenom').text.strip()

            indice_espace = chaine.index(" ")
            nom = chaine[:indice_espace].strip()
            prenom = chaine[indice_espace+1:].strip()
            # print(nom + " " + prenom)

            adresse = avocat.find('span', class_='adresse').text.strip()
            adresse = re.sub(r'\s+',' ',adresse).replace(',', '')
            # print(adresse)

            telephone = avocat.find('span', class_='telephone').text.strip().split('. ')[1]
            telephone = re.sub(r'\s+',' ',telephone)
            # print(telephone)

            span_email = avocat.find('span', class_='email')
            if span_email is not None :
                email = span_email.find('a').text.strip()
            else :
                email = 'Introuvable'
            # print(email)
            ligne = [nom, prenom, adresse, telephone, email]
            writer.writerow(ligne)