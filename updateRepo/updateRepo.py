import subprocess
import sys
import msvcrt

def cmd(cmd):
    response = subprocess.run(cmd, shell=True)
    return response

cmd('git pull')

cmd('git add .')
print()

cmd('git commit -m "updated via updateRepo"')
print()

cmd('git push origin main')
print()

print("Press any key to exit.")
msvcrt.getch()
sys.exit()
