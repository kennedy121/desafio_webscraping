# %%
import time
import requests
import pandas as pd
from openpyxl import load_workbook
from bs4 import BeautifulSoup
from selenium import webdriver
import json


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

action = ActionChains(driver)
tabela = pd.read_excel("Base.xlsx")
for i, CNPJ in enumerate(tabela["CNPJ"]):
    driver.get("http://www.cnd.der.pr.gov.br/cnd") 
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[5]/form/div[1]/label[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[5]/form/div[4]/div/input').send_keys(CNPJ)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[5]/form/button').click()  
    time.sleep(2)
    driver.find_element_by_xpath("//button[@id='visualize-positive-button']").click()
    time.sleep(20)
    raz = driver.find_element_by_class_name("field-data-search")
    html_raz = raz.get_attribute('innerHTML')
    print(html_raz)
    cpf = driver.find_element_by_class_name("data-cnpj")
    html_cpf = cpf.get_attribute('innerHTML')
    print(html_cpf)
    element = driver.find_element_by_class_name("ng-scope") 
    html_content = element.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find(name='table')
    df_full = pd.read_html(str(table))[0].head(1000)
    df = df_full[['Número do auto/Placa', 'Número da CR/Ano da CR', 'Data da infração/Documento']]
    #df.to_excel(r'C:\Users\Kennedy\Desktop\Untitled Folder\export_dataframe.xlsx',index=True,header=True,startrow=len(df_full)+1)
    print(df)

driver.quit()

# %%


# %%


# %%



