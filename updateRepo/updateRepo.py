import subprocess
import sys
import msvcrt

def cmd(cmd):
    response = subprocess.run(cmd, shell=True)
    return response

response = cmd('git add .')
cmd('git commit -m "updated via updateRepo"')
cmd('git push origin main')

print(response)

if int(response) != 0:
    print("Press any key to exit.")
    msvcrt.getch()
    sys.exit()
