import shutil
import os

#print "hola mundo "
#Python


def move(src, dest):
    shutil.copy(src, dest)

if __name__ == '__main__':
    for dirName, subdirList, fileList in os.walk("origen"):
        print('Directorio encontrado: %s' % dirName)
        for fname in fileList:
            #print "hola mundo"
            print fname
            #print('\t%s' % fname)
            move("origen\  fname","destino")



    #print "hola mundo"
    #move("origen\prueba2.txt","destino")
