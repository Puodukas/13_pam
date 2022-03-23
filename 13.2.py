import math , logging
logging.basicConfig(filename='norimas1.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
def skaiciai(*args):
    return (args)
ar = skaiciai(2,3,4,5,6)

def saknis(*args):
    try :
        s = math.sqrt(z)
    except TypeError:
        logging.exception("Iveskite skaiciu")
    else:
        return s
z = "stringas"
def ilgis(sarasas):
    b = len(sarasas)
    return b
def dalyba(x,y):
    return x/y

x= 15
y= 5
padalintas = dalyba(x,y)
sarasas = ["Vienas","Du","Trys"]
bc= ilgis(sarasas)
sak = saknis(25)
if sak != None:
    logging.info(f"saknis: {z} = {sak}")