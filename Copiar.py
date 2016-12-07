import shutil
import os
import time



def move(src, dest):
    shutil.copy(src, dest)

if __name__ == '__main__':
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Directorio encontrado: %s' % dirName)
        for fname in fileList:
            if fname != "Copiar.py":
                print fname
                move(fname,"..\destino")
                time.sleep(2)



    #print "hola mundo"
    #move("origen\prueba2.txt","destino")
