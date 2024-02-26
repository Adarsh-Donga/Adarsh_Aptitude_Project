import os
import subprocess

def get_maigret_data(username):

    command = f"python ./../git/maigret/maigret.py {username} --html --pdf"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    return result.stdout


def get_yesitsme_data(fname , lname, email, contact):

    command = f'python ./../git/yesitsme/yesitsme.py -s YOUR_INSTA_SESSION -n "{fname} {lname}" -e "{email}" -p "+39 {contact}" -t 10'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    return result.stdout


def get_daprofiler_data(fname, lname):
    command = f'python ./../git/DaProfiler/profiler.py -n "{fname} {lname}"'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    return result.stdout
