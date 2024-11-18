import subprocess
import re

command = r"cd C:\Users\Riccardo\Desktop\Esercizioadam; git log"


result = subprocess.run(["powershell.exe", command], capture_output=True, text=True) 

stringa = result.stdout

