import sys, getopt
import os


def main(argv):
   inputfile = ''
   outputfile = ''
   #print(len(sys.argv))
   tam = len(sys.argv)

   try:
      print("Katherine Mazariegos")
      if (tam == 1):
          #print("Sin argumento")
          os.system("python Portal.py")
          os.system("python Estudios.py")
          os.system("python Cs.py")
          os.system("python Directorio.py")
          #os.system("python Directorio.py")
      else:
          opts = int(sys.argv[1])
          #print(type(opts))
          if(opts ==1):
              os.system("python Portal.py")
          elif(opts ==2):
              os.system("python Estudios.py")
          elif(opts == 3):
              os.system("python Cs.py")
          elif(opts == 4):
              os.system("python Directorio.py")
          else:
              print("No se puede ejecutar nada")

   except getopt.GetoptError:
      print ('test.py -i <inputfile>' )
      sys.exit(2)


if __name__ == "__main__":
   main(sys.argv)