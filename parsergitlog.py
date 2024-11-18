import subprocess
import re

#creazione della stringa 
command = r"cd C:\Users\Riccardo\Desktop\Progetti\Secondoesercizioadam; git log"
#percorson2 = r"cd C:\Users\Riccardo\Desktop\Progetti\Secondoesercizioadam; git log"

result = subprocess.run(["powershell.exe", command], capture_output=True, text=True) 

stringa = result.stdout

# creazione del file dalla stringa
text_file = open(r"C:\Users\Riccardo\Desktop\Progetti\Secondoesercizioadam\commit.txt", "w")


text_file.write(stringa)

text_file.close()

#estrazione dei commit dal file commit.txt  
commit = []
secondo_percorso =r"C:\Users\Riccardo\Desktop\Progetti\Secondoesercizioadam\commit.txt"
with open(secondo_percorso) as myfile:
    for line in myfile.readlines():
        if re.search(r'^commit [A-Za-z0-9]+$', line):                
            commit.append(line.replace("\n", ""))



print(commit)