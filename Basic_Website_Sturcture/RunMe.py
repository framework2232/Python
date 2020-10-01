import os


# if the folder doesn't exist, the folder is made, 
# else exit() script so nothing gets accidently overwritten.
def makeMyFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print('Made your folder: ' + folder)
    else:
        print('** CAUTION **            This folder already exists: ' + folder)
        print('** SCRIPT TERMINATED **  Check the path is correct')
        print('')
        exit()

# changes directory and makes file in opened directory. 
# Careful, the f.write will clear any existing data. 
# This is why the script exit() is included when checking if the folder exists.
def makeMyFile(folder, file):
    os.chdir(folder)
    with open(file,'w') as f:
        f.write('')
        print('Built: '+ file)

# makes folder "webSite" and makes empty file "index.html"
folder = '/webSite/'
file = 'index.html'
makeMyFolder(folder)
makeMyFile(folder, file)

# makes folder "css" inside webSite folder and makes empty file "style.css"
folder = '/webSite/css'
file = 'style.css'
makeMyFolder(folder)
makeMyFile(folder, file)

# makes an empty folder "img" inside Website folder
folder = '/webSite/img'
makeMyFolder(folder)
