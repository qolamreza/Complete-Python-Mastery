import subprocess


try:
    # completed = subprocess.run(["python", "other.py"],
    completed = subprocess.run("false",
                               shell=True,
                               capture_output=True,
                               text=True)
    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.ChildProcessError as ex:
   print(ex)