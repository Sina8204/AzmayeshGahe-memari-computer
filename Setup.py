import tkinter as tk
from objects import ready_command as rc
from objects import text_tools as tt
from tkinter import ttk
from datetime import datetime
import subprocess

pos_x = 10
pos_y = 100
distance = 35
default_entery_adress_text = "Enter your Repository adress"
default_entery_branch_text = "Enter your branch name"
default_entery_commitMessage_text = "Enter your commit"

can_write_in_commitEntry = False

cmd_ob = rc()
rep_ob = tt()


def on_combobox_select (event):
    selected = combobox_commitTools.get()
    DateTime = str(datetime.now()).split(' ')
    calender = DateTime[0]
    clock = DateTime[1]
    if 'https://github.com/' in entry_address.get() or '.git' in entry_address.get():
        rep_name = rep_ob.repName(entry_address.get())
    else : pass
    if entry_CommitMessage.get() != default_entery_commitMessage_text or can_write_in_commitEntry:
        match selected:
            
            case "Repository name" : 
                if entry_CommitMessage.get() == default_entery_commitMessage_text and can_write_in_commitEntry:
                    entry_CommitMessage.delete(0 , tk.END)
                    entry_CommitMessage.config(fg = 'black')
                entry_CommitMessage.insert(tk.END , f'{rep_name} ')
            case "Branch name" :
                if entry_CommitMessage.get() == default_entery_commitMessage_text and can_write_in_commitEntry:
                    entry_CommitMessage.delete(0 , tk.END)
                    entry_CommitMessage.config(fg = 'black')
                entry_CommitMessage.insert(tk.END , f'{entry_branch.get()} ')
            case "Calender" :
                if entry_CommitMessage.get() == default_entery_commitMessage_text and can_write_in_commitEntry:
                    entry_CommitMessage.delete(0 , tk.END)
                    entry_CommitMessage.config(fg = 'black')
                entry_CommitMessage.insert(tk.END , f'{calender} ')
            case "Time" :
                if entry_CommitMessage.get() == default_entery_commitMessage_text and can_write_in_commitEntry:
                    entry_CommitMessage.delete(0 , tk.END)
                    entry_CommitMessage.config(fg = 'black')
                entry_CommitMessage.insert(tk.END , f'{clock} ')

def entry_events (entry_name):
    # For better management of these functions , I placed them inside a function 
    # so that I can hide them in VS cod when I don't need them.
    def on_entryAdress_click (event): #when clicked on address entry , its text will be delete
        if entry_address.get() == default_entery_adress_text :
            entry_address.delete(0 , tk.END)
            entry_address.config(fg = 'black')
    #
    def on_entryBranch_click (event): #when clicked on entry Branch entry , its text will be delete
        if entry_branch.get() == default_entery_branch_text :
            entry_branch.delete(0 , tk.END)
            entry_branch.config(fg = 'black')
    #
    def on_entryCommitMessage_click (event): #when clicked on Commit messege entry , its text will be delete
        if entry_CommitMessage.get() == default_entery_commitMessage_text :
            entry_CommitMessage.delete(0 , tk.END)
            entry_CommitMessage.config(fg = 'black')
        global can_write_in_commitEntry
        can_write_in_commitEntry = True
    #
    # Focus out function :
    # These functions check the entry text boxes. if they contain any value , they do nothing ,
    # but if they are empty , they write the initial text in gray color inside them. 
    def on_focus_out_adress(event):
        if entry_address.get() == '':
            entry_address.insert(0 , default_entery_adress_text)
            entry_address.config(fg = 'grey')
    #
    def on_focus_out_branch(event):
        if entry_branch.get() == '':
            entry_branch.insert(0 , default_entery_branch_text)
            entry_branch.config(fg = 'grey')
    #
    def on_focus_out_commit(event):
        if entry_CommitMessage.get() == '':
            entry_CommitMessage.insert(0 , default_entery_commitMessage_text)
            entry_CommitMessage.config(fg = 'grey')
    #
    match entry_name :
        #if click in entry box to writing , entry box will be empty
        case 'adress' : return on_entryAdress_click
        case 'branch' : return on_entryBranch_click
        case 'commit' : return on_entryCommitMessage_click
        #if entry box be empty , these cases will write the gray texts
        case 'adress_out' : return on_focus_out_adress
        case 'branch_out' : return on_focus_out_branch
        case 'commit_out' : return on_focus_out_commit



def git_init():
    answer = cmd_ob.git_init()
    Termina_textBox.insert(tk.END , str(answer) + '\n')
    return str(answer)

def delet_origin():
    answer = cmd_ob.delet_origin()
    Termina_textBox.insert(tk.END , str(answer) + '\n')
    return str(answer)

def add_origin ():
    address = str(entry_address.get())
    answer = cmd_ob.add_origin(address) #
    Termina_textBox.insert(tk.END , str(answer) + '\n')
    return str(answer)

def git_pull ():
    Branch = str(entry_branch.get())
    answer = cmd_ob.git_pull(Branch) #Branch is master at default
    Termina_textBox.insert(tk.END , str(answer) + '\n')
    answer = cmd_ob.creat_LocalBranch()
    return str(answer)

def git_add():
    answer = cmd_ob.git_add()
    Termina_textBox.insert(tk.END , str(answer) + '\n')
    return str(answer)

def git_commit():
    Message = str (entry_CommitMessage.get())
    answer = cmd_ob.git_commit(Message) # 
    Termina_textBox.insert(tk.END , str(answer) + '\n')
    return str(answer)

def git_push(): 
    #Branch = str(entry_branch.get())
    answer = cmd_ob.git_push()
    if answer[1].returncode == 0:
        print("Push operation was successful :)")
        Termina_textBox.insert(tk.END , str(answer[1]) + f'\n\nPush to "{cmd_ob.branch}" branch operation was successful :)\n')
        cmd_ob.delete_git()
        print ("git folder deleted ;)")
    else:
        print("we take an error")
        print (answer[0])
        Termina_textBox.insert(tk.END , str(answer[1]) + '\n')
    return str(answer)

def project_size ():
    Termina_textBox.insert(tk.END , cmd_ob.project_size(unit = combobox_unit.get()) + '\n')


def set_window_size(root, width_ratio, height_ratio): # this take our monitor siza and make a window with our monitor details 
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = int(screen_width * width_ratio)
    window_height = int(screen_height * height_ratio)

    root.geometry(f"{window_width}x{window_height}")

def Readme_window():
    rep_name = rep_ob.repName(entry_address.get())
    if not write_project_size_check.get():
        if 'https://github.com/' in entry_address.get():
            with open ('README.md' , 'a' , encoding='utf-8') as file:
                file.write(f'# {rep_name}\nSize: {cmd_ob.project_size(unit = combobox_unit.get())} \n')
        else :
            Termina_textBox.insert(tk.END , 'Pleas insert your repository name in the address entry \n')
            print('Pleas insert your repository name in the address entry')
    else :
        def write_project_size():
            editor_textBox.insert(tk.END , cmd_ob.project_size(unit = combobox_unit.get()) + '\n')
        def save_readMe_file ():
            with open ('README.md' , 'a' , encoding='utf-8') as file:
                file.write(f'{editor_textBox.get(1.0 , tk.END)} \n')
        root2 = tk.Tk()
        root2.title("Readme editor")
        pos_x = 10
        pos_y = 10
        distance = 10
        set_window_size(root2, width_ratio=0.385, height_ratio=0.5)
        #
        addSizeProject_button = tk.Button (root2, text="Write project size", command=write_project_size)
        addSizeProject_button.place (x = pos_x , y = pos_y)
        #
        saveReadmeFile_button = tk.Button (root2, text="Save Readme file", command=save_readMe_file)
        saveReadmeFile_button.place (x = pos_x , y = pos_y + distance * 3)
        #
        editor_textBox = tk.Text(root2, width=70 , height=21)
        editor_textBox.place (x = pos_x , y = pos_y + (distance * 7))
        with open ('README.md' , '+r' , encoding='utf-8') as file:
            content = file.read()
            editor_textBox.insert(tk.END , content+'\n')
        root2.mainloop()

root = tk.Tk()
root.title("Transmitter to GitHub")

set_window_size(root, width_ratio=0.385, height_ratio=0.8)

entry_address = tk.Entry (root, width=50) #text box to enter files adress
entry_address.insert(0 , default_entery_adress_text)
entry_address.bind('<FocusIn>' , entry_events('adress'))
entry_address.bind('<FocusOut>' , entry_events('adress_out'))
entry_address.place (x = pos_x , y = pos_y - 90)

entry_branch = tk.Entry (root, width=50) #text box to enter files adress
entry_branch.insert(0 , default_entery_branch_text)
entry_branch.bind('<FocusIn>' , entry_events('branch'))
entry_branch.bind('<FocusOut>' , entry_events('branch_out'))
entry_branch.place (x = pos_x , y = pos_y - 60)

entry_CommitMessage = tk.Entry (root, width=50) #text box to enter files adress
entry_CommitMessage.insert(0 , default_entery_commitMessage_text)
entry_CommitMessage.bind('<FocusIn>' , entry_events('commit'))
entry_CommitMessage.bind('<FocusOut>' , entry_events('commit_out'))
entry_CommitMessage.place (x = pos_x , y = pos_y - 30)


combobox_commitTools = ttk.Combobox (root , values= ["Repository name" , "Branch name" , "Calender" , "Time"] , state='readonly' , width= 22)
combobox_commitTools.place (x = pos_x + (distance * 5) + 140 , y = pos_y - 31)
combobox_commitTools.set ("Select an item to write it")
combobox_commitTools.bind("<<ComboboxSelected>>" , on_combobox_select)

button_GitInit = tk.Button (root, text=" git init          ", command=git_init)
button_GitInit.place (x = pos_x , y = pos_y)

button_DeletOrigin = tk.Button (root, text="Delete origin", command=delet_origin)
button_DeletOrigin.place (x = pos_x , y = pos_y + distance)

button_AddOrigin = tk.Button (root, text="Add origin    ", command=add_origin)
button_AddOrigin.place (x = pos_x , y = pos_y + (distance * 2))

button_GitPull = tk.Button (root, text="git pull          ", command=git_pull)
button_GitPull.place (x = pos_x , y = pos_y + (distance * 3))

button_GitAdd = tk.Button (root, text="git add          ", command=git_add)
button_GitAdd.place (x = pos_x , y = pos_y + (distance * 4))

button_GitCommit = tk.Button (root, text=" git commit  ", command=git_commit)
button_GitCommit.place (x = pos_x , y = pos_y + (distance * 5))

button_GitPush = tk.Button (root, text=" git push       ", command=git_push)
button_GitPush.place (x = pos_x , y = pos_y + (distance * 6))

button_projectSize = tk.Button (root, text=" Project size", command= project_size)
button_projectSize.place (x = pos_x + (distance * 3) , y = pos_y)

button_readME_window = tk.Button (root, text="Open Readme", command= Readme_window)
button_readME_window.place (x = pos_x + (distance * 3) , y = pos_y + distance)

write_project_size_check = tk.BooleanVar()
checkBox_write_project_size_check = tk.Checkbutton(text="Open Readme editor" , variable= write_project_size_check , font=('' , 12))
checkBox_write_project_size_check.place (x = pos_x + (distance * 6) - 15 , y = pos_y + distance )

Termina_textBox = tk.Text(root, width=70 , height=20)
Termina_textBox.place (x = pos_x , y = pos_y + (distance * 7))

combobox_unit = ttk.Combobox (root , values= ["Kb" , "Mb" , "Gb" , "Byte"] , state='readonly' , width= 5)
combobox_unit.place (x = pos_x + (distance * 5) + 10 , y = pos_y + 3)
combobox_unit.set ("Mb")


root.mainloop()