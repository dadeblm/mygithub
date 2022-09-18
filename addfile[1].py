import os
import shutil
import csv
import argparse

# Per lo step 2 bisogna creare un eseguibile dotato di interfaccia a linea di comando, che posso creare tramite il modulo argparse che
# ho scelto di utilizzare

def elaborate(file_name, directory, filetype):
    print("{} type:{} size:{}B".format(file_name.split(".")[0], filetype, os.path.getsize(os.path.join(directory,file_name))))
    
    new_writer.writerow([file_name.split(".")[0], filetype, os.path.getsize(os.path.join(directory, file_name))])
    
    if not os.path.isfile(os.path.join(directory, filetype, file_name)):
        shutil.move(os.path.join(directory, file_name), os.path.join(directory, filetype))

os.chdir("./files/") 
directory = os.getcwd()
files = os.listdir(directory)        
        
# All'interno del codice dello step 1 inserisco il parser con una piccola descrizione, di modo che se da terminal si chiama la funzione -h
# si otterranno le informazioni necessarie per operare dalla command line
parser = argparse.ArgumentParser(description="Semplice organizzatore di file all'interno delle cartelle di competenza, con aggiornamento del file di recap.")
parser.add_argument("file_name", type=str, choices=files, help="Nome del file da spostare") #inserisco l'unico argomento richiesto, ossia il nome del file da spostare, potendo scegliere tra quelli presenti nelle directory di lavoro
args = parser.parse_args()
file_name = args.file_name
        

# Se il nome del file inserito non esiste, da terminal verrà stampato il seguente messaggio
if not os.path.isfile(os.path.join(directory, file_name)):
    print("Il file non esiste all'interno della directory")
else: # altrimenti tutto procederà come previsto all'interno dello step 1
    for dirname in ["audio", "images", "docs"]:
        if not os.path.isdir(os.path.join(directory, dirname)):
            os.makedirs(os.path.join(directory, dirname))
        
    audio_ext = [".mp3"]
    images_ext = [".jpg", ".jpeg", ".png"]
    docs_ext = [".txt", ".odt"]

    if not os.path.isfile(os.path.join(directory, "recap.csv")):
        with open(os.path.join(directory, "recap.csv"), "w", newline="") as my_csv:
            csv_writer = csv.writer(my_csv)
            csv_writer.writerow(["name", "type", "size(B)"])
        
    open_csv = open(os.path.join(directory, "recap.csv"), "a", newline="")
    new_writer = csv.writer(open_csv)



    name, extension = os.path.splitext(file_name)
    
    if extension in audio_ext:
        elaborate(file_name, directory, "audio")
    elif extension in images_ext:
        elaborate(file_name, directory, "images")
    elif extension in docs_ext:
        elaborate(file_name, directory, "docs")
    else:
        print("Formato file non supportato")
        
    open_csv.close()

