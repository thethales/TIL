import sys
import os 
import shutil 
import json
import glob


def main():
    source      = ".META/readmebasefile.md"
    destination = "README.md"
    dest = shutil.copyfile(source, destination) 
    addItens2()

def addItens2():
    arr_ignore = ['References']
    directoryList =[]
    fReadme = open("README.md", "a")
    fReadme.write('\n')

    for path, subdirs, files in os.walk('src', topdown=True):
        for name in files:
            file = os.path.join(path,name)
            directory = os.path.dirname(file).replace('src\\','')
            if(directory not in directoryList):
                fReadme.write(mdHeader3(directory))
                directoryList.append(directory)
            with open(file) as tempf:
                lines = tempf.readlines()
                for line in lines:
                    if line.startswith('# ') and line.replace('#', '').strip() not in arr_ignore:
                        fReadme.write(mdBullet1Link(line.replace('#', '').strip(),file))
                    if line.startswith('## ') and line.replace('#', '').strip() not in arr_ignore:
                        fReadme.write(mdBullet2Link(line.replace('#', '').strip(),file))
    
    return


def mdHeader2(desc):
    return "## " + desc.replace('.md','') + ' \n';
def mdHeader3(desc):
    return "### " + desc.replace('.md','') + ' \n';
def mdHeader3Link(desc,ref):
    return "### [" + desc.replace('.md','') +'](<'+ ref.replace('\\','/') +'>) \n';
def mdBullet1Link(desc,ref):
    return "* [" + desc.replace('.md','') +'](<'+ ref.replace('\\','/') +'>) \n';
def mdBullet2Link(desc,ref):
    return "  * [" + desc.replace('.md','') +'](<'+ ref.replace('\\','/') +'>) \n';

if __name__ == '__main__':
    sys.exit(main())