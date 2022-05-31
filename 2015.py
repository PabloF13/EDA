import pandas as pd
from selenium import webdriver
import seaborn as sns
from Functions import clean_df

#Inicializar
driver = r'C:\Users\clfs\Downloads\chromedriver_win32\chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=driver, options=options)
url = 'https://www.procyclingstats.com/race/tour-de-france/2015'
driver.get(url)

#DataFrame vacio
france=pd.DataFrame([])
spain=pd.DataFrame([])
italy=pd.DataFrame([])

# Obtener datos France
nombres = []
valores = []
cabecera = driver.find_element_by_xpath(
    "/html/body/div[2]/div[1]/div[8]/div[1]/div[1]/div[5]/table/thead").find_elements_by_tag_name('tr')
ciclistas = driver.find_element_by_xpath(
    "/html/body/div[2]/div[1]/div[8]/div[1]/div[1]/div[5]/table/tbody").find_elements_by_tag_name('tr')

for elemento in cabecera:
    etiquetas = elemento.find_elements_by_tag_name('th')

for ciclista in ciclistas:
    datos = ciclista.find_elements_by_tag_name('td')
    for dato in datos:
        valores.append(dato.text)
    for etiqueta in etiquetas:
        nombres.append(etiqueta.text)

    diccionario = dict(zip(nombres, valores))
    france = france.append(diccionario, ignore_index=True)

# Obtener datos Spain
nombres = []
valores = []
cabecera = driver.find_element_by_xpath(
    "/html/body/div[2]/div[1]/div[8]/div[1]/div[1]/div[5]/table/thead").find_elements_by_tag_name('tr')
ciclistas = driver.find_element_by_xpath(
    "/html/body/div[2]/div[1]/div[8]/div[1]/div[1]/div[5]/table/tbody").find_elements_by_tag_name('tr')

for elemento in cabecera:
    etiquetas = elemento.find_elements_by_tag_name('th')

for ciclista in ciclistas:
    datos = ciclista.find_elements_by_tag_name('td')
    for dato in datos:
        valores.append(dato.text)
    for etiqueta in etiquetas:
        nombres.append(etiqueta.text)

    diccionario = dict(zip(nombres, valores))
    spain = spain.append(diccionario, ignore_index=True)

# Obtener datos Italy
nombres = []
valores = []
cabecera = driver.find_element_by_xpath(
    "/html/body/div[2]/div[1]/div[8]/div[1]/div[1]/div[5]/table/thead").find_elements_by_tag_name('tr')
ciclistas = driver.find_element_by_xpath(
    "/html/body/div[2]/div[1]/div[8]/div[1]/div[1]/div[5]/table/tbody").find_elements_by_tag_name('tr')

for elemento in cabecera:
    etiquetas = elemento.find_elements_by_tag_name('th')

for ciclista in ciclistas:
    datos = ciclista.find_elements_by_tag_name('td')
    for dato in datos:
        valores.append(dato.text)
    for etiqueta in etiquetas:
        nombres.append(etiqueta.text)

    diccionario = dict(zip(nombres, valores))
    italy = italy.append(diccionario, ignore_index=True)

#Limpiar DataFrames
clean_df(france)
clean_df(spain)
clean_df(italy)

#Columna año y minutos
france["Year"]=2015
spain["Year"]=2015
italy["Year"]=2015
france["Country"]="France"
spain["Country"]="Spain"
italy["Country"]="Italy"
#france.iat[0,3]=0

tour2015=pd.concat([france, spain, italy], ignore_index=True )
