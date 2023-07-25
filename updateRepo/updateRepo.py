import subprocess
import sys
import msvcrt
import os

cwd = os.getcwd()
cwd = str(cwd)

def cmd(cmd):
    response = subprocess.run(cmd, shell=True)
    return response

response = cmd('git add .')

if response == 128:
    print("\nERROR")
    print("Presiona una tecla para finalizar el programa...")
    sys.exit()

cmd('git commit -m "."')
cmd('git push origin main')