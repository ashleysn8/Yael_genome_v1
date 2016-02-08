import os
import glob
from Yael_genomes_param.py import *

resultPath = currentPath + "\Results"
if not os.path.exists(result):
    os.makedirs("Results")

for folder in myFolders:
    os.mkdir(resultPath + '\\' + folder, 0777)