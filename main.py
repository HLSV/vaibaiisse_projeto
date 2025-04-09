import os
import time

def emitir_som():
    print("Emitindo som de frequência simbólica...")
    os.system("termux-media-player play som_simbolico.mp3")

def vibrar():
    print("Ativando vibração simbólica...")
    os.system("termux-vibrate -d 500")

if __name__ == "__main__":
    vibrar()
    time.sleep(1)
    emitir_som()
