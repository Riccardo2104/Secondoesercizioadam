import subprocess
import re

command = r"cd C:\Users\Riccardo\Desktop\Esercizioadam; git log"


result = subprocess.run(["powershell.exe", command], capture_output=True, text=True) 

stringa = result.stdout

# creazione del file dalla stringa
text_file = open(r"C:\Users\Riccardo\Desktop\Progetti\Secondoesercizioadam\commit.txt", "w")

# write string to file
text_file.write(stringa)

text_file.close()