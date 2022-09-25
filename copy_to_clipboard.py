import subprocess

def copy2clip(txt: str):
    cmd='echo '+txt+'|clip'
    return subprocess.check_call(cmd, shell=True)

