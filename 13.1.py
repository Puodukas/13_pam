"""Sukurti funkcijas, kurios:

•Gražintų visų paduotų skaičių sumą (su *args argumentu)
•Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
•Gražintų paduoto sakinio simbolių kiekį (su len())
•Gražintų rezultatą, skaičių x padalinus iš y
Nustatyti standartinį logerį (logging) taip, kad jis:

•Saugotų pranešimus į norimą failą
•Saugotų INFO lygio žinutes
•Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė
Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko, pvz.:"""

import math , logging

logging.basicConfig(filename='norimas.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
def skaiciai(*args):
    return (args)
ar = skaiciai(2,3,4,5,6)

def saknis(*args):
    s = math.sqrt(z)
    return s

def ilgis(sarasas):
    b = len(sarasas)
    return b
def dalyba(x,y):
    return x/y
z = 25
x= 15
y= 5
padalintas = dalyba(x,y)
sarasas = ["Vienas","Du","Trys"]
bc= ilgis(sarasas)
sak = saknis(z)
logging.info(f"skaiciai = {ar}")
logging.info(f"saknis: {z} = {sak}")
logging.info(f"dalyba: {x} / {y} = {padalintas}")
logging.info(f"ilgis: {sarasas} ={bc}")