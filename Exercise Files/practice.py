import subprocess # library to use the command line

for i in range(5):
    subprocess.check_call(["python3", "example.py"]) # Executing the terminal command for running example.py 5 times on the termminal