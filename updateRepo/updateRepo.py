import subprocess
import sys
import msvcrt

def cmd(cmd):
    response = subprocess.run(cmd, shell=True)
    return response

cmd('git pull')

cmd('git add .')
cmd('git commit -m "updated via updateRepo"')
cmd('git push origin main')

print("Press any key to exit.")
msvcrt.getch()
sys.exit()
