import subprocess
# import os

# subprocess.run("ls -al", shell=True)
# os.system("ls")
r = subprocess.run("lsa", shell=True)
print(r.returncode())
print("#######")