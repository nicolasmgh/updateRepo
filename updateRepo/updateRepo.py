import subprocess
import sys
import msvcrt

def cmd(cmd):
    response = subprocess.run(cmd, shell=True)
    return response

print()
cmd('git pull')

print()
cmd('git add .')

print()
cmd('git commit -m "updated via updateRepo"')

print()
cmd('git push origin main')

print("Press any key to exit.")
msvcrt.getch()
sys.exit()
