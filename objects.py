import os
import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        print(f">>>  {stderr.decode()}")
    return [stdout.decode() , process]

class ready_command ():
    def __init__(self):
        self.branch = ''
        self.size_project = 0
        self.unit = "Mb" # Mb = Megabyte ; Kb : Kilobyte ; Gb : Gigabyte
        self.paw = 1
    #
    def git_init (self):
        return run_command("git init")[0]
    #
    def delet_origin (self):
        return run_command("git remote remove origin")[0]
    #
    def add_origin (self , gitHub_address : str):
        self.gitHub_address = gitHub_address
        return run_command(f"git remote add origin {self.gitHub_address}")[0]
    #
    def git_pull (self , branch : str = "master" ):
        self.branch = branch
        return run_command (f"git pull origin {self.branch} --allow-unrelated-histories")[0]
        #after pulling , creat local branch to name self.branch in your VS code at Source Control
    #
    def creat_LocalBranch (self):
        return run_command (f'git checkout -b {self.branch}')[0]

    def git_add (self):
        return run_command("git add .")[0]
    #
    def git_commit (self , message : str):
        self.message = message
        return run_command (f'git commit -m "{self.message}"')[0]
    #
    def git_push (self):
        return run_command (f"git push -u origin {self.branch}")
    #
    def delete_git (self):
        return run_command ("Remove-Item -Recurse -Force .git")
    #
    def project_size (self, start_path='.' , unit = "Mb"):
        # بررسی سایز پروژه
        #"Get-ChildItem -Recurse | Measure-Object -Property Length -Sum" >>>> a cmd command to get project size that give you with Byte
        self.unit = unit
        match self.unit :
            case "Kb" : self.paw = 1
            case "Mb" : self.paw = 2
            case "Gb" : self.paw = 3
            case _ : self.paw , self.unit = 0 , 'Byte'
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        size_in_megabytes = total_size / (1024 ** self.paw)
        print(f"Project size: {size_in_megabytes:.2f} {self.unit}")
        return f"{size_in_megabytes:.2f} {self.unit}"


class text_tools :
    def repName (self , rep_link : str):
        rep_link = rep_link.split('/')
        rep_name = rep_link.pop()
        rep_name = rep_name.replace('.git', '')
        return rep_name