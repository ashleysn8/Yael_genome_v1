import os
import bz2
import sys
import shutil
import subprocess

species = input("What is the Species? ")
genome = input("What is the genome path? ")
umiLength = input("What is the UMI length? ")
currentPath = input("What is the current path? ")

fileHandle = open(os.path.realpath(genome), 'r+')
genomeSize = os.path.getsize(genome)
uncompressedData = bz2.BZ2File(genome).read(genomeSize)

def copyFile(genome, currentPath):
    try:
        shutil.copy(genome, currentPath)
    except shutil.Error as e:
        print('Error: %s' % e)
    except IOError as e:
        print('Error: %s' % e.strerror)

    
if "Human" in species or "human" in species:
    os.system("runScript_human.sh " + genome)
    subprocess.call(['./liRNAseq_pipeline_2_mouse.sh '] + genome + " "+ umiLength)
elif "mouse" in species or "Mouse" in species:
    os.system("runScript_mouse.sh " + genome)
    subprocess.call(['./liRNAseq_pipeline_2_mouse.sh '] + genome + " " + prefix + " " + umiLength)
else :
    print ("Please try again")
    
myFolders = []  #list of files in folder
        
for root, dirs, files in os.walk(genome):
    myFolders.extend(files) #add files name into list
    for d in myFolders:
        folder_name = d.rsplit('.',1)[0]        #If file calls abc.txt , so takes abc
        folderNames.extend(folder_name)
        newpath = os.path.join(genome,folder_name)   
        if not os.path.exists(newpath): #check if folder exists
            os.makedirs(newpath)    #create folder based on the filenames
        file_original_path = os.path.join(genome,d)
        shutil.copy(file_original_path,newpath) #copy the corresponding files to the folder

print ("Part I succesful!")