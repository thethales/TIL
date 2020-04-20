import sys
import os 
import shutil 
import json


def main():

    source      = ".META/readmebasefile.md"
    destination = "README.md"

    dest = shutil.copyfile(source, destination) 
    
    #addCategorias()
    addItens()


def addCategorias():
    arr_ignore = ['.git','.meta']
    
    folders = [f for f in os.listdir('.') if os.path.isdir(f)]
    
    f = open("README.md", "a")
    f.write(mdHeader2("Categories") + '\n')
    for category in folders:
        if (category not in arr_ignore):
            f.write('* ' + category + '\n')  
    
    f.close()
    return;

def addItens():
    arr_ignore = ['.git','.meta']
    jFolder = {}

    diretorio = [f for f in os.listdir('.') if os.path.isdir(f)]
    
    for category in diretorio:
        if (category not in arr_ignore):
            diretorioFiles = os.listdir('./'+category+'/') 
            jFolder[category] = diretorioFiles

    #Keeps a copy of the JSON on the directory
    meta_file_content = jFolder
    file_meta_json = open('.meta/meta.json', "w")
    json.dump(jFolder, file_meta_json)
    file_meta_json.close()



    f = open("README.md", "a")
    f.write('<!-- index starts -->' + '\n')
    f.write(mdHeader2("Categories") + '\n')
    for category in jFolder:
        f.write(mdHeader2(category) + '\n')
        for categoryFile in jFolder[category]:
            f.write(mdBullet2Link(categoryFile,categoryFile) + '\n')
    f.write('<!-- index ends -->'+ '\n')    
    
    
    
    f.close()
    return;

def mdHeader2(desc):
    return "## " + desc;
def mdHeader2Link(desc,ref):
    return "## [" + desc +'](/'+ ref +')';
def mdBullet1Link(desc,ref):
    return "- [" + desc +'](/'+ ref +')';
def mdBullet2Link(desc,ref):
    return "-- [" + desc +'](/'+ ref +')';

if __name__ == '__main__':
    sys.exit(main())