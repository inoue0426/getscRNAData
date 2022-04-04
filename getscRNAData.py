import os
import subprocess

t = !ls ../bash/*

for i in t:
    l = i.split('/')[2][:-3]

    try:
        os.mkdir(l)
    except OSError as e:
        pass
    
    os.chdir(l)
#     os.system('sh {}'.format(i))
    subprocess.call(['sh', '../{}'.format(i)])
    os.chdir('/Users/yoshitakainoue/code/scRNAData/data')
