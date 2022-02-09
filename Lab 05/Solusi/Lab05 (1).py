import sys
import re
from os import path

SMILE_EMOJI = "\U0001f603"
SAD_EMOJI = "\U0001f622"
ANGRY_EMOJI = "\U0001f621"

happiness = 50
sadness = 50
anger = 50

def process_happy():
    global happiness, sadness
    happiness = happiness + 9 if happiness + 9 < 100 else 100
    sadness = sadness - 6 if sadness - 6 > 0 else 0

def process_sad():
    global sadness, anger
    sadness = sadness + 10 if sadness + 10 < 100 else 100
    anger = anger - 8 if anger - 8 > 0 else 0

def process_anger():
    global anger, happiness
    anger = anger + 13 if anger + 13 < 100 else 100
    happiness = happiness - 5 if happiness - 5 > 0 else 0

def output_result():
    global happiness, sadness, anger
    print("\nMengukur suasana hati....\n")
    print("##### Hasil Pengukuran #####")
    print(f"Happiness = {happiness} | Sadness = {sadness} | Anger = {anger}\n")
    print("##### Kesimpulan #####")
    
    if happiness == sadness == anger:
        print("Kesimpulan tidak ditemukan.")
    else:
        print("Pak Chanek sedang ", end='')
        if anger <= happiness >= sadness:
            print("bahagia", end='')
            if happiness == sadness:
                print(" atau sedih", end='')
            if happiness == anger:
                print(" atau marah", end='')
            print(".")
        elif anger <= sadness > happiness:
            print("sedih", end='')
            if anger == sadness:
                print(" atau marah", end='')
            print(".")
        else:
            print("marah.")

def main():
    filename = input("Masukkan nama file input: ")
    if not path.exists(filename):
        print("File input tidak ada :(")
        sys.exit()
    lines = open(filename, "r").readlines()
    if not lines:
        print("File input ada tapi kosong :(")
        sys.exit()
    for line in lines:
        line = line.rstrip()
        if re.match(r'^pak chanek', line, re.IGNORECASE):
            for i in range(len(re.findall(r'\(smile\)', line, re.IGNORECASE))):
                process_happy()
            for i in range(len(re.findall(r'\(sad\)', line, re.IGNORECASE))):
                process_sad()
            for i in range(len(re.findall(r'\(angry\)', line, re.IGNORECASE))):
                process_anger()
        line = re.sub(re.compile(r'\(smile\)', re.IGNORECASE), SMILE_EMOJI, line)
        line = re.sub(re.compile(r'\(sad\)', re.IGNORECASE), SAD_EMOJI, line)
        line = re.sub(re.compile(r'\(angry\)', re.IGNORECASE), ANGRY_EMOJI, line)
        print(line)
    output_result()

if __name__ == '__main__':
    main()