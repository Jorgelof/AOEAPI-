import requests
import json

class API(object):
    
    def __init__(self):
        self.ENDPOINT = 'https://age-of-empires-2-api.herokuapp.com/api/v1'

    def getCiv(self):
        civ = f'{self.ENDPOINT}/civilizaciones'
        r = requests.get(civ)
        data = r.json()
        civilizaciones = []
        for i in data.get("civilizaciones"):
            civilizaciones.append({
                "nombre":i.get("nombre"),
                "expansion": i.get("expansion"),
                "tipo": i.get("tipo_armadura")
            })
        return civilizaciones
    
    def getUni(self):
        uni = f'{self.ENDPOINT}/unidades'
        r = requests.get(uni)
        data = r.json()
        unidades = []
        for i in data.get("unidades"):
            unidades.append({
                "nombre":i.get("nombre"),
                "descripcion": i.get("descripcion"),
                "expansion": i.get("expansion"),
                "edad": i.get("edad"),
                "rango": i.get("rango"),
                "ataque": i.get("ataque")
            })
        return unidades
    
    def getEst(self):
        est = f'{self.ENDPOINT}/estructuras'
        r = requests.get(est)
        data = r.json()
        estructuras = []
        for i in data.get("estructuras"):
            estructuras.append({
                "nombre": i.get("nombre"),
                "expansion": i.get("expansion"),
                "edad": i.get("edad"),
                "tiempo": i.get("tiempo")
            })
        return estructuras
    
    def getTec(self):
        tec = f'{self.ENDPOINT}/tecnologias'
        r= requests.get(tec)
        data = r.json()
        tecnologias = []
        for i in data.get("tecnologias"):
            tecnologias.append({
                "nombre": i.get("nombre"),
                "descripcion": i.get("descripcion"),
                "expansion": i.get("expansion"),
                "edad": i.get("edad")
            })
        return tecnologias
