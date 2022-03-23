import math , logging
logger = logging.getLogger(__name__)
file_handler =  logging.FileHandler('norimas2.log')
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

formater = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formater)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formater)
logger.addHandler(stream_handler)

def skaiciai(*args):
    return (args)
ar = skaiciai(2,3,4,5,6)

def saknis(*args):
    try:
        s = math.sqrt(z)
    except TypeError:
        logger.exception("Iveskite skaiciu")
    else:
        return s
z = "wa"
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
    logger.info(f"saknis: {z} = {sak}")